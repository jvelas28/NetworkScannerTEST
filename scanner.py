import socket

def leer_archivo(filename):
    #Con el archivo abierto haz lo siguiente
    with open(filename,"r") as file:
        lineas= file.readlines()
        lineaslimpias=[]
        for linea in lineas:
            lineaslimpias.append(linea.rstrip())
        return lineaslimpias
            
hosts = leer_archivo("ips.txt")
ports = leer_archivo("puertos_comunes.txt")

#Para cada host que haya en hosts
for host in hosts:
#Nos dice los cantidad de puertos guardados en la array portspyt

    for port in ports:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(1)

        result= sock.connect_ex((host,int(port)))
        if result == 0:
            print(f"El puerto {port} está abierto en el host {host}")
        else:
            print(f"El puerto{port} está cerrado en el host {host} " )
        sock.close()
