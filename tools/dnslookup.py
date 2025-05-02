import subprocess
import re

def dnslookup(domain: str, type: str | None = None):
    """
    options:
    1. type: ns (name servers), soa (start of authority), any, ptr (ptr records)
    2. query: mx (mail exchanger)
    3. specific dns server: pass the dns server 
    4. reverse dns: pass the ip
    """
    dns_dict = {}

    

    result = subprocess.run(["nslookup", f"{domain}"], shell=True, capture_output=True, text=True)
    
    output = result.stdout

    if result.returncode == 0:
        lista = [re.sub(r"\t", "", item) for item in output.strip().split("\n")[4:]]
        lista_aux = [item[item.find(":")+1:].strip() for item in lista]
        output_list = list(zip(*[iter(lista_aux)]*2))
        
        for item in output_list:
            _domain, ipaddr = item

            aux_ipaddr = {"IPv4": [], "IPv6": []}

            if _domain not in dns_dict:
                dns_dict[_domain] = aux_ipaddr

                if len(ipaddr.split(".")) > 1:
                    dns_dict[_domain]["IPv4"].append(ipaddr)
                else:
                    dns_dict[_domain]["IPv6"].append(ipaddr)
            else:
                if len(ipaddr.split(".")) > 1:
                    dns_dict[_domain]["IPv4"].append(ipaddr)
                else:
                    dns_dict[_domain]["IPv6"].append(ipaddr)

        print(dns_dict)
    else:
        lista = [re.sub(r"\t", "", i) for i in output.split("\n")]
        print(lista)
