import socket
from datetime import datetime

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
print("Waiting for connection")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
invalid = "Invalid Command!"
msg= "What is the current date and time?"
msg_rcv=''

while True:
        clientsocket, address = s.accept()
        print("Connection has been established!")
        while True:


                try:


                        data = clientsocket.recv(100)
                        msg_rcv = data.decode()
                        print ("Received Message: ",msg_rcv)
                        if msg_rcv != msg:
                                clientsocket.sendall(invalid.encode())

                        else:
                                datetimeObject= datetime.now().strftime('%m/%d/%Y %H:%M:%S')
                                sendmsg= "Current Date and Time - " +datetimeObject
                                clientsocket.sendall(sendmsg.encode())
                                
                        msg_rcv = ""

                except Exception as e:
                        print(e)
                        print("Waiting for next connection")
                        break
        

        



s.close()
