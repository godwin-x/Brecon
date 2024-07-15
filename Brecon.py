import os
import argparse
import time 


alias = """  
=====================================================
*     Auto Recon Tool by :                          *
*                           X-Sec                   *
* (V1.0)                                            *
=====================================================

* JS-File
* CRLF Injection
* Cors Misconfiguration
* XSS + Blind XSS
* External Service Interaction
* CRLF Injection
* 
"""
print(alias)

#V1
jsfile = input(str(" [X] Part to the List of js-files to check for leaks..: "))
print()
print(" [X] Testing For Js-Leaks...!!!")
print()
os.system(f"type {jsfile} | jsleak -s")
print()
print(" [X] Done With Looking For Js-Leaks ..!!!")
print()
print(" [X] Done With Looking For Js-Leaks ..!!!")
print()
#v2
crlf = input(str(" [X] Part to the List of Resloved domains to check for CRLF Injection..: "))
print()
print(" [X] Testing For CRLF Injection...!!!")
print()
os.system(f"type {crlf} | crlfsuite --pipe")
