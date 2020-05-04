import sys, socket
##size approach

#have ip and port of server
s_addr = ('localhost', 13000)

#handshake: let server know my ip and port
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

buf_size = 1024
#read msg to send from keyboard until read ending char, with size info
canary = '#'
input_info = "what do you want to say (hit '" + canary + "' to end):"
while(True):
	while(True):
		data = b''
		k_input = b''

		k_input = input(input_info)
		#put msg into buffer
		data = k_input.encode('ASCII')

		if(k_input[-1] == canary):
			break

	#send msg to server
	s.sendto(data, s_addr)

	#keep listen to server to heard back the msg
	returned =b''
	while(len(returned)!=len(data)):
		returned += s.recv(buf_size)

	print(returned[:-1])







