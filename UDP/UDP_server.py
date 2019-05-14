import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(('',12345))
ClientData,(IP,port) = server_socket.recvfrom(2048)
print("ClientData :"+str(ClientData))
print("from : " +str(IP))
server_socket.sendto("this is server message :".encode(),(IP,port))
server_socket.close()


