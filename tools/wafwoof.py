import subprocess
import re
from typing import List

def wafwoof(domains: List[str]):
    print("Starting WAFW00F...")

    waf_dict = {}

    for domain in domains:
        result = subprocess.run(" ".join(["wafw00f", domain]), shell=True, capture_output=True, text=True)
        
        result.check_returncode()
        
        lista_result = result.stdout.strip().split("\n")

        aux_idx = 0

        for i in lista_result:
            if i == "":
                aux_idx = lista_result.index(i) + 4
                break

        aux_lista = lista_result[aux_idx:]

        lista_final = [re.compile(r'\x1b\[[0-9;]*m').sub('', item) for item in aux_lista]
        lista_final = [item[3:].strip() for item in lista_final]

        if len(lista_final) <= 1:
            print(f"-> Nenhum WAF encontrado para o dominio {domain}")
        else:
            for i in lista_final:
                match1 = re.search(r'is behind (.+?) WAF', i)

                if match1 is not None:
                    match = match1
                    break
            
            if match1 is None:
                for i in lista_final:
                    match2 = re.search(r'seems to be behind a WAF', i)

                    if match2 is not None:
                        match = match2

                        break

            if match:
                if not match.group(0).startswith("seems to be behind a WAF"):
                    print(f"-> WAF encontrado para o dominio \x1b[33m{domain}\x1b[0m: \x1b[94m{match.group(1)}\x1b[0m")

                    if domain not in waf_dict:
                        waf_dict[domain] = {"WAF": [match.group(1)]}
                    else:
                        waf_dict[domain]["WAF"].append(match.group(1))
                else:
                    print(f"-> WAF nao encontrado para o dominio {domain}")
            else:
                print(f"-> WAF nao encontrado para o dominio {domain}")

    return waf_dict
