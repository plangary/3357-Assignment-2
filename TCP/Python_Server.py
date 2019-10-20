import socket
from datetime import datetime

TCP_IP = '127.0.0.1'
TCP_PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
invalid = "Invalid!"
#msg= "What is the current date and time?"
msg="t"
msg_rcv=''

while True:
        clientsocket, address = s.accept()
        print("Connection has been established!")
        while True:


                try:


                        data = clientsocket.recv(100)
                        msg_rcv = data.decode()
                        print (msg_rcv)
                        if msg_rcv != msg:
                                clientsocket.sendall(invalid.encode())

                        else:
                                datetimeObject= datetime.now().strftime('%m/%d/%Y %H:%M:%S')
                                sendmsg= "Current Date and Time - " +datetimeObject
                                clientsocket.sendall(sendmsg.encode())
                                
                        msg_rcv = ""

                except Exception as e:
                        print(e)
                        break
        

        



    





#print('Client Address:', addr)
#data = conn.recv(16)
#s.close()
