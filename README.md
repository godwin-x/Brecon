# Brecon
Auto Recon Tool is an automated security reconnaissance tool designed to streamline the process of web application security testing. Works on on PowerShell. It integrates multiple tools to perform various security checks and identify potential vulnerabilities.
Features

    Subdomain enumeration using assetfinder
    Subdomain takeover check using subzy
    URL fetching from web archives using gau
    Parameter fuzzing using qsreplace
    Filtering live domains using httpx
    Open port scanning using naabu
    Vulnerability scanning using dalfox

Requirements

Ensure you have the following tools installed and available in your system's PATH:

    assetfinder
    subzy
    gau
    qsreplace
    httpx
    naabu
    dalfox
    PowerShell (for Windows users)

Installation

Clone this repository to your local machine:

bash

git clone [https://github.com/godwin-x/Brecon.git](https://github.com/godwin-x/Brecon.git)
cd Brecon

Usage

    Create a scope.txt file in the project directory and list your target domains, one per line.

    Run the script using Python:

bash

python auto_recon_tool.py

The script will perform the following steps:

    Read domains from scope.txt.
    Use assetfinder to find subdomains.
    Check for subdomain takeover using subzy.
    Fetch URLs with parameters using gau.
    Replace query parameters with FUZZ using qsreplace.
    Filter URLs that contain FUZZ using grep.
    Use httpx to filter live domains.
    Use naabu to check for open ports on live hosts.
    Use dalfox to check for vulnerabilities.

Output

All results will be saved in the output directory, which is created automatically by the script. The output files include:

    subdomains.txt: List of discovered subdomains.
    subzy_output.txt: Results of the subdomain takeover check.
    gau_urls.txt: URLs with parameters fetched using gau.
    fuzz_urls.txt: URLs with parameters replaced by FUZZ.
    fuzz_grep_urls.txt: Filtered URLs containing FUZZ.
    live_domains.txt: List of live domains.
    naabu_output.txt: Open port scan results.
    dalfox.txt: Vulnerability scan results.

Disclaimer

This tool is intended for educational purposes and lawful use only. Use this tool responsibly and only on domains you have explicit permission to test. The author is not responsible for any misuse or damage caused by this tool.
License

This project is licensed under the MIT License. See the LICENSE file for details.
Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
