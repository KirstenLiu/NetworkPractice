import sys, socket
#msg based, don't need to take care of the size

#listen to server address + port
s_addr = ('localhost', 13000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(s_addr)

buf_size = 1024

#keep listen from client
while(True):
	data = b''
	#get msg from client
	data, c_address = s.recvfrom(buf_size)
	#DEBUG: print msg
	print("DEBUG:: received: ", data)
	#send msg back to client
	s.sendto(data, c_address)