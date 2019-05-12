import socket
import select
import sys

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 12345
client_socket.connect(('',port))
print("Connected")
while True:
	r,w,e = select.select([sys.stdin,client_socket],[],[])
	for soc in r :
		if soc == sys.stdin:
			msg = raw_input()
			client_socket.send(msg.encode("utf-8"))
		elif soc == client_socket:
			msg = client_socket.recv(1024).decode("utf-8")
			print(msg)
		if msg == "bye":
			client_socket.close()
			break
	if msg == "bye":
		client_socket.close()
		break

