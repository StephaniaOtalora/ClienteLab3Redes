import socket
ip_servidor_de_verdad = "54.145.37.10"
host_ip, server_port = "localhost", 9999

estandar = 1024

# Initialize a TCP client socket using SOCK_STREAM
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (host_ip, server_port)

try:
    print('connecting to {} port {}'.format(*server_address))
    # Establish connection to TCP server and exchange data
    tcp_client.connect(server_address)
    #tcp_client.sendall(data.encode())
    print('Connection status: ready')
    tcp_client.send('Established connection. Waiting for the message.'.encode())
    # Read data from the TCP server and close the connection
    received = tcp_client.recv(estandar)

    f = open("archivorecibido.mp4", 'wb')
    while received:
        f.write(received)
        received = tcp_client.recv(estandar)
    f.close()

#except:
#    print('Connection status: refused')

finally:
    tcp_client.close()
