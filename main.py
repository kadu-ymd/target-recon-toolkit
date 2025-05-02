from tools import dnslookup

def main() -> int:
    dnslookup.dnslookup("insper.edu.br")
    
    return 0

if __name__ == "__main__":
    main()
