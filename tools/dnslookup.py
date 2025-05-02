import subprocess

def dnslookup(domain: str):
    result = subprocess.run(["nslookup", domain], shell=True, capture_output=True, text=True)
    
    print(result.stdout)