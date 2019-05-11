import socket
import select
import sys

def binary(string_data):
	binary =  ' '.join(format(ord(x), 'b') for x in string_data)
	return binary

def xor(a,b):
	result = list(b)
	for i in range(0,len(b)):
		if a[i] == b[i]:
			result[i] ='0'
		else:	
			result[i] ='1'
	return "".join(result)


def mod2div(divident,divisor):
	pick = len(divisor)
	temp = divident[0:pick]	
	while pick < len(divident):
		if temp[0] == '1':
			temp = xor(temp,divisor) + divident[pick]
			temp = temp[1:]
		else:
			temp = xor('0'*pick,temp) + divident[pick]
			temp =temp[1:]
		pick = pick + 1
	if temp[0] == '1': 
        	temp = xor(divisor, temp) 
    	else: 
       		temp = xor('0'*pick, temp) 
	return temp

def encodeData(data,key):
	lengthOfKey = len(key)
	addZerotoData = data + '0'*(lengthOfKey-1)
	remainder = mod2div(addZerotoData,key)
	return data+remainder[(-1)*(lengthOfKey-1):],remainder[(-1)*(lengthOfKey-1):]

s = socket.socket()
s.connect(('',12345))
print("Connected")
key = "1001"
while True:
	input_s = [sys.stdin,s]
	r,w,e = select.select(input_s,[],[])
	for soc in r:
		if soc == s :
			msg = s.recv(1024).decode('utf-8')
			print("Message From Server :",msg)
			print("Check CRC :",mod2div(msg,key))
		if soc == sys.stdin:
			msg = raw_input()
			print("Message : ",msg)
			binary_msg = binary(msg)
			print("Message in Binary : ",binary_msg)
			encode_msg,crc = encodeData(binary_msg,key)
			print("Message after apply CRC : ",encode_msg)
			print("CRC :" , crc)
			s.send(encode_msg.encode("utf-8"))
		if msg == "bye":
			input_s.remove(s)
	if s not in input_s:
		break
s.close()

	

