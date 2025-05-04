from tools import *
import json
import socket


OPTIONS = {"indent": 4, "sort_keys": True}

def dns_type():
    
    return

def main() -> int:
    file_list = []

    print("Available tools for use:")

    print("1. DNS Lookup")
    print("2. Portscan")
    print("3. WafW00f")

    tool = int(input("Enter the number of the tool you want to use: "))
    print()

    if tool == 1:
        print("Tool: DNS Lookup")

        print("1. Type (Name-server, Start of Authority, Any, Pointer Records)")
        print("2. Query (Mail Exchanger)")
        print("3. Standard/reverse DNS Lookup")
        print("4. Go back")

        options = int(input("Enter the number of the option you want to use: "))
        print()

        while options > 4 or options < 1:
            print(f"{options} is not a valid number")
            options = int(input("Enter a valid number of the option you want to use: "))

        if options == 1:
            print("1. Name servers")
            print("2. Start of Authority")
            print("3. Any")
            print("4. Pointer Records")
            print("5. Go back")
            print()

            lookup_type = int(input("Enter the number of the type you want to use: "))
            print()

            while lookup_type > 5 or lookup_type < 1:
                print(f"{lookup_type} is not a valid number")
                lookup_type = int(input("Enter a valid number of the type you want to use: "))
                print()

            dns_lookup_type = dnslookup.DNSLookup.dns_type(lookup_type)

        elif options == 2:
            dns_lookup_query = dnslookup.DNSLookup.dns_query()

        elif options == 3:
            print("1. Standard/reverse DNS Lookup")
            print("2. Specific DNS Server")
            print("3. Go back")

            dns_lookup_std = int(input("Enter the number of the type you want to use: "))
            print()

            while dns_lookup_std > 3 or dns_lookup_std < 1:
                print(f"{dns_lookup_std} is not a valid number")
                dns_lookup_std = int(input("Enter a valid number of the type you want to use: "))

            server = None
            if dns_lookup_std == 1:
                pass
            elif dns_lookup_std == 2:
                server = input("Enter the DNS server you want to use: ")
            elif dns_lookup_std == 3:
                return main()
            
        elif options == 4:
            return main()
        
        domain = input("Enter the domain you want to inspect: ")

        dns_dict = dnslookup.dnslookup(domain,
                                       type=dns_lookup_type,
                                       query=dns_lookup_query,
                                       server=server)
        
        file_list.append(("DNSLookup", dns_dict))

    elif tool == 2:
        print("Tool: Portscan")

        print("1. TCP")
        print("2. UDP")
        print("3. Go back")

        kwargs = {}

        portscan_type = int(input("Enter the number of the type you want to use: "))
        print()

        while portscan_type > 3 or portscan_type < 1:
            print(f"{portscan_type} is not a valid number")
            portscan_type = int(input("Enter a valid number of the type you want to use: "))
            print()

        if portscan_type == 1:
            kwargs["protocol"] = "-t"
        elif portscan_type == 2:
            kwargs["protocol"] = "-u"
        elif portscan_type == 3:
            return main()
        
        print("1. IPv4")
        print("2. IPv6")
        print("3. Go back")

        ip_version = int(input("Enter the number of the type you want to use: "))
        print()

        while ip_version > 3 or ip_version < 1:
            print(f"{ip_version} is not a valid number")
            ip_version = int(input("Enter a valid number of the type you want to use: "))
            print()

        if ip_version == 1:
            kwargs["version"] = "-v4"
        elif ip_version == 2:
            kwargs["version"] = "-v6"
        elif ip_version == 3:
            return main()

        print("1. Network")
        print("2. Hostname")
        print("3. Go back")

        scan_type = int(input("Enter the number of the type you want to use: "))
        print()

        while scan_type > 3 or scan_type < 1:
            print(f"{scan_type} is not a valid number")
            scan_type = int(input("Enter a valid number of the type you want to use: "))
            print()

        if scan_type == 1:
            kwargs["type"] = "-n"
        elif scan_type == 2:
            kwargs["type"] = "-h"
        elif scan_type == 3:
            return main()

        if kwargs["type"] == "-n":
            network = input("Enter the network IP address you want to scan: ")
            kwargs["network"] = network
        elif kwargs["type"] == "-h":
            hostname = input("Enter the host IP address you want to scan: ")
            kwargs["hostname"] = hostname

        print("1. Port range")
        print("2. IP range")
        print("3. Continue (using default values)")
        print("4. Go back")

        range_num = int(input("Enter the number of the type you want to use: "))
        print()

        while range_num > 4 or range_num < 1:
            print(f"{range_num} is not a valid number")
            range_num = int(input("Enter a valid number of the type you want to use: "))
            print()

        if range_num == 1:
            kwargs["port_range"] = input("Enter the port range you want to scan (start_port,end_port): ")
            kwargs["port_range"] = kwargs["port_range"].split(",")
            try:
                start_port = int(kwargs["port_range"][0])
                end_port = int(kwargs["port_range"][1])
            except:
                raise Exception("Invalid syntax: check if the values of the port_range are integers")
            kwargs["port_range"] = (start_port, end_port)

        elif range_num == 2:
            kwargs["ip_range"] = input("Enter the IP range you want to scan (start_ip,end_ip): ")
            kwargs["ip_range"] = kwargs["ip_range"].split(",")
            try:
                start_ip = int(kwargs["ip_range"][0])
                end_ip = int(kwargs["ip_range"][1])
            except:
                raise Exception("Invalid syntax: check if the values of the ip_range are integers")
            kwargs["ip_range"] = (start_ip, end_ip)

        elif range_num == 3:
            pass

        elif range_num == 4:
            return main()

        port_dict = ("portscan", portscan.portscan(**kwargs))
        file_list.append(port_dict)

    elif tool == 3:
        print("Tool: WAFW00F")

        domains = input("Enter the domain(s) you want to inspect (separated by space): ")
        print()

        domains = domains.strip().split(" ")

        waf_dict = ("wafw00f", wafwoof.wafwoof(domains))
        file_list.append(waf_dict)

    for f in file_list:
        with open(f"{f[0]}.json", "w") as file:
            json.dump(f[1], file, **OPTIONS)

    return 0

if __name__ == "__main__":
    main()
