import os
import subprocess

alias = """  
=====================================================
*     Auto Recon Tool by :                          *
*                           godwin-X                *
* (V2.1)                                            *
=====================================================

* Find SubDomains
* Check For SubDomain TakeOver
* Check For Live Domains
* Check For Open Ports From Live Domain's
* Pull Parameters From Archieve 
* Grep For query Parameters And Replace With (FUZZ)
* Check For Injection Vulnerability (Htmli,XSS,SQLi,Reflection Parameters)
"""
print(alias)

def run_command(command):
    """Run a shell command using PowerShell and return the output."""
    result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True, shell=True)
    return result.stdout.strip()

def read_domains_from_scope(filename='scope.txt'):
    """Read domains from scope.txt file, attempting multiple encodings."""
    encodings = ['utf-8', 'utf-16', 'latin-1']
    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as f:
                return f.read().splitlines()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Failed to decode {filename} with available encodings.")

def create_output_directory(directory='output'):
    """Create an output directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def main():
    output_directory = 'output'
    create_output_directory(output_directory)

    # Step 1: Read domains from scope.txt
    domains = read_domains_from_scope()
    print("Read domains from scope.txt")

    # Step 2: Use assetfinder to get subdomains
    subdomains = set()
    for domain in domains:
        print(f"Finding subdomains for {domain}...")
        assetfinder_output = run_command(f"assetfinder --subs-only {domain}")
        subdomains.update(assetfinder_output.splitlines())

    print(f"Found {len(subdomains)} subdomains")

    # Step 3: Use subzy to check for subdomain takeover
    subdomains_file = os.path.join(output_directory, 'subdomains.txt')
    with open(subdomains_file, 'w', encoding='utf-8') as f:
        for subdomain in subdomains:
            f.write(f"{subdomain}\n")

    print("Checking for subdomain takeover with subzy...")
    subzy_output = run_command(f"subzy r --targets {subdomains_file}")
    subzy_output_file = os.path.join(output_directory, 'subzy_output.txt')
    with open(subzy_output_file, 'w', encoding='utf-8') as f:
        f.write(subzy_output + "\n")
    print(f"Subzy scan completed. Results saved in {subzy_output_file}")

    # Step 4: Use gau to fetch URLs with parameters
    print("Fetching URLs with parameters using gau...")
    gau_file = os.path.join(output_directory, 'gau_urls.txt')
    gau_command = "Get-Content scope.txt | gau --subs"
    gau_output = run_command(gau_command)
    with open(gau_file, 'w', encoding='utf-8') as f:
        f.write(gau_output + "\n")
    print(f"Gau completed. Results saved in {gau_file}")

    # Step 5: Use qsreplace to replace query parameters with 'FUZZ'
    print("Replacing query parameters with 'FUZZ' using qsreplace...")
    fuzz_urls_file = os.path.join(output_directory, 'fuzz_urls.txt')
    qsreplace_command = f"Get-Content {gau_file} | qsreplace FUZZ"
    qsreplace_output = run_command(qsreplace_command)
    with open(fuzz_urls_file, 'w', encoding='utf-8') as f:
        f.write(qsreplace_output + "\n")

    # Step 6: Use grep to filter URLs that contain 'FUZZ'
    print("Filtering URLs that contain 'FUZZ' using grep...")
    fuzz_grep_file = os.path.join(output_directory, 'fuzz_grep_urls.txt')
    fuzz_grep_command = f"Get-Content {fuzz_urls_file} | Select-String FUZZ"
    fuzz_grep_output = run_command(fuzz_grep_command)
    with open(fuzz_grep_file, 'w', encoding='utf-8') as f:
        f.write(fuzz_grep_output + "\n")

    # Step 7: Use httpx to filter live domains
    print("Filtering live subdomains with httpx...")
    live_domains_file = os.path.join(output_directory, 'live_domains.txt')
    httpx_command = f"Get-Content {subdomains_file} | httpx -silent"
    httpx_output = run_command(httpx_command)
    with open(live_domains_file, 'w', encoding='utf-8') as f:
        f.write(httpx_output + "\n")
    print(f"Found {len(httpx_output.splitlines())} live domains. Results saved in {live_domains_file}")

    # Step 8: Use naabu to check for open ports on live hosts
    print("Checking for open ports with naabu...")
    naabu_output_file = os.path.join(output_directory, 'naabu_output.txt')
    naabu_command = f"naabu -list {live_domains_file}"
    naabu_output = run_command(naabu_command)
    with open(naabu_output_file, 'w', encoding='utf-8') as f:
        f.write(naabu_output + "\n")
    print(f"Naabu scan completed. Results saved in {naabu_output_file}")

    # Step 9: Feed results to dalfox using pipe to check for vulnerabilities
    print("Checking for vulnerabilities with dalfox...")
    dalfox_output_file = os.path.join(output_directory, 'dalfox.txt')
    dalfox_command = f"Get-Content {fuzz_grep_file} | dalfox pipe -b godwin.bxss.in -o {dalfox_output_file}"
    run_command(dalfox_command)

    print("Dalfox scan completed. Results saved in 'output' directory.")

if __name__ == "__main__":
    main()
