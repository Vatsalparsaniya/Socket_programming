import socket
import select
import sys

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 12345
server_socket.bind(('',port))
server_socket.listen(1)
while True:	
	client_socket , C_address = server_socket.accept()
	print("connect to : " + str(C_address))
	while True:
		r,w,e = select.select([sys.stdin,client_socket],[],[])
		for soc in r:
			if soc == sys.stdin:
				msg = raw_input()
				client_socket.send(msg.encode("utf-8"))
			else:
				msg = client_socket.recv(1024).decode("utf-8")
				print(msg)
			if msg == "bye":
				break
		if msg == "bye":
			client_socket.close()
			break

	
