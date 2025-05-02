import subprocess

def main() -> int:
    result = subprocess.run(["ls", "-l"], shell=True, capture_output=True, text=True)
    
    print(result.stdout)
    
    return 0

if __name__ == "__main__":
    main()
