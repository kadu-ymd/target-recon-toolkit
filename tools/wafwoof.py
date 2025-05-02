import subprocess
import re

def wafwoof(domain: str):
    waf_dict = {}

    result = subprocess.run(" ".join(["wafw00f", domain]), shell=True, capture_output=True, text=True)
    
    result.check_returncode()
    
    lista_result = result.stdout.strip().split("\n")
    lista_result = lista_result[len(lista_result)-3:]

    lista_final = [re.compile(r'\x1b\[[0-9;]*m').sub('', item) for item in lista_result]
    lista_final = [item[3:] for item in lista_final]

    print(lista_final)

    return 