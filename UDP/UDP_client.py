import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_socket.sendto("this is client Message ".encode(),('',12345))
data,(IP,port) = client_socket.recvfrom(2048)
print(data.decode())
client_socket.close()
