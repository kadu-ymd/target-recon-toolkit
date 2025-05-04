from tools import *
import json


OPTIONS = {"indent": 4, "sort_keys": True}

def main() -> int:
    file_list = []

    print("Available tools for use:")

    print("1. DNS Lookup\n"
          "2. Portscan\n"
          "3. WHOIS\n"
          "4. WafW00f\n"
    )

    tool = int(input("Enter the number of the tool you want to use: "))
    print()

    if tool == 1:
        dns_dict = dnslookup.dnslookup("")
    elif tool == 2:
        pass
    elif tool == 3:
        pass
    elif tool == 4:
        print("Tool: WAFW00F")

        domains = input("Enter the domain(s) you want to inspect (separated by space): ")
        print()

        domains = domains.strip().split(" ")

        waf_dict = ("WAFW00F", wafwoof.wafwoof(domains))
        file_list.append(waf_dict)

    for f in file_list:
        with open(f"{f[0]}.json", "w") as file:
            json.dump(f[1], file, **OPTIONS)

    return 0

if __name__ == "__main__":
    main()
