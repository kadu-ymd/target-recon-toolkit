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
        return "mx"

    @staticmethod
    def execute(cmd): pass

    def rollback(where): pass

def dnslookup(domain: str, 
              type: str | None = None, 
              query: str | None = None,
              server: str | None = None
              ):

    cmd = ["nslookup"]

    if type is not None:
        cmd.append(f"-type={type}")

    if query is not None:
        cmd.append(f"-query={query}")
    
    cmd.append(domain)

    if server is not None:
        cmd.append(f"{server}")

    result = subprocess.run(" ".join(cmd), shell=True, capture_output=True, text=True)

    result.check_returncode()

    dns_dict = {"result": result.stdout}

    return dns_dict

    
