import requests
import urllib3
import argparse
from colorama import Fore

banner = f"{Fore.RED}╦ ╦┌─┐┌─┐┌┬┐┌─┐┬─┐{Fore.RESET}{Fore.MAGENTA}╔═╗┬ ┬┌─┐┌─┐┬┌─{Fore.RESET}\n"\
         f"{Fore.RED}╠═╣├┤ ├─┤ ││├┤ ├┬┘{Fore.RESET}{Fore.MAGENTA}║  ├─┤├┤ │  ├┴┐{Fore.RESET}\n"\
         f"{Fore.RED}╩ ╩└─┘┴ ┴─┴┘└─┘┴└─{Fore.RESET}{Fore.MAGENTA}╚═╝┴ ┴└─┘└─┘┴ ┴{Fore.RESET}\n"
print (banner)

parser = argparse.ArgumentParser()
parser.add_argument('-l','--list', required=False,default='subdomain.txt' ,help='Masukan wordlist')
args = parser.parse_args()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers_to_check = ['X-Frame-Options', 'X-XSS-Protection', 'Content-Security-Policy']

with open(args.list, 'r') as subdomain_file:
    subdomains = subdomain_file.readlines()


for subdomain in subdomains:
    url = subdomain.strip()

    response = requests.get(url, verify=False)

    print(f"{Fore.BLUE}[+] Target: {url} {Fore.GREEN}{response.status_code}")

    missing_headers = [header for header in headers_to_check if header not in response.headers]
    if missing_headers:
        missing_headers_line = ', '.join([f"{Fore.RED}{header}: Missing" for header in missing_headers])
        print(f"{Fore.GREEN} [+] Headers: {missing_headers_line}\n")
    else:
        print(f"{Fore.GREEN} [+] All headers are present\n")
