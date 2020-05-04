import sys, socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_addr = ('localhost', 10005)
s.bind(s_addr)

s.listen(5)

buf_size = 1024    
while(True):   
    #print("server socket: ", s)
    (conn, address) = s.accept()
    print("open new socket", conn)
    #print("server connection: ", conn)
    #print("server address: ", address)

    data = None
    #TODO: if recv empty, establish new conn 
    while(True):
        data = conn.recv(buf_size)
        if(data == b''):
        	#print("close socket", conn)
            break
        else:
        	#send back to the client
        	conn.send(data)


