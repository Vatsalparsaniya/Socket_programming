from textwrap import wrap

data = raw_input("Enter Your Data into binary :")
checksum = 8
data = str(data)
padding = len(data)%checksum
print(padding)
data = data + "0"*(checksum - padding)
c_data = wrap(data,checksum)
sum = "0"*checksum
print(c_data)
sum = 0
for i in range(0,len(c_data)):
 	sum += int(c_data[i],2)
sum = bin(sum)
sum = sum[2:]
print(sum)
print(len(sum))
sum = str(sum)
a = sum[-8:]
print(a)
b = sum[0:len(sum)-checksum]
print(b)
ck = int(a,2) + int(b,2)
print(ck)

	 



