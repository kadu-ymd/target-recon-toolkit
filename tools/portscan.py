import socket
import datetime


socket.setdefaulttimeout(.2)

def scanner(ip: str, 
            protocol: str, 
            ip_version: int,
            start_port: int = 1, 
            end_port: int = 1000
    ) -> dict:

    portscan_dict = {f"{ip}": {"open_ports": [], "closed_ports": [], "filtered_ports": []}}

    print("----------------------------------")

    socket_type = socket.SOCK_STREAM

    try:
        start_time = datetime.datetime.now()
        ports_open = 0
        service = ""

        for port in range(start_port, end_port):
            result = ""

            try:
                service = socket.getservbyport(port, protocol)
            except OSError:
                continue

            addrinfo = socket.getaddrinfo(ip, port)

            addr = addrinfo[0][4]
            socket_type = addrinfo[0][1]

            if protocol == "udp" and len(addrinfo) > 1:
                addr = addrinfo[1][4]
                socket_type = addrinfo[1][1]

            with socket.socket(family=ip_version, type=socket_type) as s:
                try:
                    errno_code = s.connect_ex(addr)
                    
                    if not errno_code:
                        result = f"{port}/{protocol} - {service} - open"

                        portscan_dict[f"{ip}"]["open_ports"].append(port)
                        ports_open += 1

                    elif errno_code in [111, 10061]:
                        result = f"{port}/{protocol} - {service} - closed"
                        portscan_dict[f"{ip}"]["closed_ports"].append(port)

                    else:
                        result = f"{port}/{protocol} - {service} - filtered"
                        portscan_dict[f"{ip}"]["filtered_ports"].append(port)
                        
                    print(result)

                except OSError:
                    service = "unknown port"

                except TimeoutError:
                    raise TimeoutError("Tempo limite atingido")

        runtime = datetime.datetime.now() - start_time
        
        print(f"\nTotal de portas abertas encontradas: {ports_open}\n"
              f"Tempo de execucao: {runtime.seconds}.{runtime.microseconds} segundos\n")

    except KeyboardInterrupt:
        runtime = datetime.datetime.now() - start_time
        
        print(f"\nTotal de portas abertas encontradas: {ports_open}\n"
              f"Tempo de execucao: {runtime.seconds}.{runtime.microseconds} segundos\n")

        raise KeyboardInterrupt("\nOperacao cancelada pelo usuario")

    return portscan_dict

def scanNetwork(
        network: str, 
        protocol: str, 
        ip_proto: int,
        start_port: int = 1, 
        end_port: int = 1000,
        start_ip: int = 1, 
        end_ip: int = 255, 
    ):

    portscan_dict = {}
    
    print(f"Rede a ser escaneada: {network}")
    
    for ip in range(start_ip, end_ip + 1):
        hostname = network + "." + str(ip)
        
        portscan_dict = scanner(hostname, protocol, ip_proto, start_port, end_port)

    print(f"Escaneamento da rede finalizada")

    return portscan_dict
    
def portscan(**kwargs) -> int:
    portscan_dict = {}

    if kwargs["protocol"] in ["-u", "-U"]:
        protocol = "udp"
    elif kwargs["protocol"] in ["-t", "-T"]:
        protocol = "tcp"
    else:
        raise Exception("Sintaxe incorreta: primeiro argumento (protocolo) deve ser -t para TCP ou -u para UDP")
    
    if kwargs["version"] in ["-v4", "-V4"]:
        version = socket.AF_INET
    elif kwargs["vers  ion"] in ["-v6", "-V6"]:
        version = socket.AF_INET6
    else:
        raise Exception("Sintaxe invalida: o argumento do protocolo IP deve ser -v4 ou -v6")
        
    if len(kwargs) - 1 == 4:
        if kwargs["type"] in ["-n", "-N"]:
            network = kwargs["network"]

            portscan_dict = scanNetwork(network, protocol, version)

        elif kwargs["type"] in ["-h", "-H"]:
            hostname = kwargs["hostname"]

            portscan_dict = scanner(hostname, protocol, version)

    elif len(kwargs) - 1 == 5:
        if kwargs["port_range"]:
            port_range = kwargs["port_range"]

            try:
                start_port = int(port_range[0])
                end_port = int(port_range[1])
            except:
                raise Exception("Sintaxe invalida: verifique se os valores do port_range sao inteiros")

            if kwargs["type"] in ["-n", "-N"]:
                network = kwargs["network"]

                portscan_dict = scanNetwork(network, protocol, version, start_port, end_port)

            elif kwargs["type"] in ["-h", "-H"]:
                hostname = kwargs["hostname"]

                portscan_dict = scanner(hostname, protocol, version, start_port, end_port)

        elif kwargs["ip_range"] and kwargs["type"] in ["-n", "-N"]:
            ip_range = kwargs["ip_range"]

            try:
                start_ip = int(ip_range[0])
                end_ip = int(ip_range[1])
            except:
                raise Exception("Sintaxe invalida: verifique se os valores do ip_range sao inteiros")

            network = kwargs["network"]

            portscan_dict = scanNetwork(network, protocol, start_ip=start_ip, end_ip=end_ip)
        else:
            raise Exception("Sintaxe invalida: o ip_range so pode ser utilizado para escaneamento de rede")
        
    elif len(kwargs) - 1 == 6 and kwargs["type"] in ["-n", "-N"]:
        if kwargs["port_range"]:
            port_range = kwargs["port_range"]

            try:
                start_port = int(port_range[0])
                end_port = int(port_range[1])
            except:
                raise Exception("Sintaxe invalida: verifique se os valores do port_range sao inteiros")
            
            if kwargs["ip_range"]:
                ip_range = kwargs["ip_range"]

                try:
                    start_ip = int(ip_range[0])
                    end_ip = int(ip_range[1])
                except:
                    raise Exception("Sintaxe invalida: verifique se os valores do ip_range sao inteiros")

                network = kwargs["network"]

                portscan_dict = scanNetwork(network, protocol, start_port, end_port, start_ip, end_ip)
            else:
                raise Exception("Sintaxe invalida: verifique se o ip_range foi utilizado corretamente")
        else:
            raise Exception("Sintaxe invalida: verifique se foi utilizada a flag -n")
   
    else:
        raise Exception("Quantidade incorreta de argumentos")
        
    return portscan_dict

if __name__ == "__main__":
    portscan()