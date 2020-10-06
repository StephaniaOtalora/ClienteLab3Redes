import socket
from datetime import datetime

ip_mudial = "54.145.37.10"
host_ip, server_port = "localhost", 9999

estandar = 1024

# Initialize a TCP client socket using SOCK_STREAM
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('connecting to {} port {}'+host_ip+" "+str(server_port))
try:
    # Establish connection to TCP server and exchange data
    tcp_client.connect((host_ip, server_port))
    print('Connection status: ready')
    tcp_client.send('Established connection. Waiting for the message.'.encode())

    # Read data from the TCP server and close the connection
    hora_inicial = tcp_client.recv(19).decode(encoding='UTF-8')
    fecha1 = datetime.strptime(hora_inicial, '%m-%d-%Y %H:%M:%S')

    received = tcp_client.recv(estandar)
    print("Comenzó a leer")
    f = open("arc.mp4", 'wb')
    while received:
        f.write(received)
        received = tcp_client.recv(estandar)
    f.close()
    hora_final = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    fecha2 = datetime.strptime(hora_final, '%m-%d-%Y %H:%M:%S')
    segundos = (fecha2-fecha1).seconds
    print("tiempo :D : "+ str(segundos))
    
    print("terminó de leer")

    tcp_client.send("File received".encode())
    print("ya envió el mensaje")

finally:
    tcp_client.close()