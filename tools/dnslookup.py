import subprocess
import re

class DNSLookup:
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

    aux_lista = [item for item in output.strip().split("\n")]
    
    if "ns" in type:
        dns_dict = {"Non-authoritative": {}, "Authoritative": {}}
        flag_non_authoritative = False
        flag_authoritative = False

        for item in aux_lista[3:]:
            if flag_non_authoritative:
                _domain = item.split("\t")[0].strip()

                if item == "":
                    flag_non_authoritative = False
                
                if flag_non_authoritative:
                    if _domain not in dns_dict["Non-authoritative"]:
                        dns_dict["Non-authoritative"][_domain] = [item.split("\t")[1].strip().split()[2]]
                    else:
                        dns_dict["Non-authoritative"][_domain].append(item.split("\t")[1].strip().split()[2])

            if flag_authoritative:
                nameserver = item.split("\t")[0].strip()

                if item == "":
                    flag_authoritative = False
                
                if flag_authoritative:
                    if nameserver not in dns_dict["Authoritative"]:
                        dns_dict["Authoritative"][nameserver] = [item.split("\t")[1].strip().split()[3]]
                    else:
                        dns_dict["Authoritative"][nameserver].append(item.split("\t")[1].strip().split()[3])

            if "Non-authoritative" in item:
                flag_non_authoritative = True
            
            if "Authoritative" in item:
                flag_authoritative = True

    # elif "soa" in type:

    print(aux_lista)

    print(dns_dict)