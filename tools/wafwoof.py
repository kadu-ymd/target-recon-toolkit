import subprocess
import re

def wafwoof(domain: str):
    waf_dict = {}

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
        return 1

    # match = re.search(r'is behind (.+?) WAF', lista_final[2])

    # if match:
    #     print(f"WAF: {match.group(1)}")
    # else:
    #     print("WAF nao encontrado")

    # if lista_final[0][8:] not in waf_dict:
    #     waf_dict[lista_final[0][8:]] = []

    # aux_idx = 0

    # for item in lista_final:
    #     if item.startswith("Checking"):
    #         aux_idx = lista_final.index(item)
    #         break
    #     elif item.startswith("Generic"):
    #         aux_idx = lista_final.index(item)
    #         break
    
    # print(result.stdout)

    # aux_list = lista_final[aux_idx:]

    # print(aux_list)

    # if len(aux_list) > 1:


    return 