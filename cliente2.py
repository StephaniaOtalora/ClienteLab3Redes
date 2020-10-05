import socket

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
    received = tcp_client.recv(estandar)

    f = open("arc.mp4", 'wb')
    while received:
        f.write(received)
        received = tcp_client.recv(estandar)
    f.close()
finally:
    tcp_client.close()