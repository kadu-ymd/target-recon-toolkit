import subprocess
import re

class DNSLookup:
    def __init__(self):
        pass


    @staticmethod
    def dns_type(type: int):
        if type == 1:
            return "ns"
        elif type == 2:
            return "soa"
        elif type == 3:
            return "any"
        elif type == 4:
            return "ptr"
        elif type == 5:
            return 
        else:
            raise ValueError(f"{type} is not a valid type")

    @staticmethod
    def dns_query(): 
        return "-query=mx"

    @staticmethod
    def execute(cmd): pass

    def rollback(where): pass

def dnslookup(domain: str, 
              type: str | None = None, 
              query: str | None = None,
              server: str | None = None
              ) -> dict:

    dns_dict = {}

    cmd = ["nslookup"]

    if type is not None:
        cmd.append(f"-type={type}")

    if query is not None:
        cmd.append(f"-query={query}")
    
    cmd.append(domain)

    if server is not None:
        cmd.append(f"{server}")

    result = subprocess.run(" ".join(cmd), shell=True, capture_output=True, text=True)
    
    output = result.stdout

    result.check_returncode()

    print(output)

    lista = [re.sub(r"\t", "", item) for item in output.strip().split("\n")[4:]]
    lista_aux = [item[item.find(":")+1:].strip() for item in lista]
    output_list = list(zip(*[iter(lista_aux)]*2))
    
    # for item in output_list:
    #     _domain, ipaddr = item

    #     aux_ipaddr = {"IPv4": [], "IPv6": []}

    #     if _domain not in dns_dict:
    #         dns_dict[_domain] = aux_ipaddr

    #         if len(ipaddr.split(".")) > 1:
    #             dns_dict[_domain]["IPv4"].append(ipaddr)
    #         else:
    #             dns_dict[_domain]["IPv6"].append(ipaddr)
    #     else:
    #         if len(ipaddr.split(".")) > 1:
    #             dns_dict[_domain]["IPv4"].append(ipaddr)
    #         else:
    #             dns_dict[_domain]["IPv6"].append(ipaddr)

    # print(dns_dict)

    # lista = [re.sub(r"\t", "", i) for i in output.split("\n")]
    # print(lista)