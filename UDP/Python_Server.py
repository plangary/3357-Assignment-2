import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((TCP_IP, TCP_PORT))
invalid = "Invalid!"
#msg= "What is the current date and time?"
msg="t"
msg_rcv=''


while True:
        data, address = s.recvfrom(1024)
        print (data)

        

        


#print('Client Address:', addr)
#data = conn.recv(16)
#s.close()
