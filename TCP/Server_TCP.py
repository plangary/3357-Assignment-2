import socket
from datetime import datetime

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
print("Waiting for connection")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #connect to socket using IPV4 address using TCP
s.bind((TCP_IP, TCP_PORT)) #bind to socket
s.listen(1) #listen for connection, queue size of 1
invalid = "Invalid Command!"
msg= "What is the current date and time?"
msg_rcv='' #store message received 

while True:
        clientsocket, address = s.accept() #accept connection
        print("Connection has been established!")
        while True:


                try: #try statement to continue running while loop and listen for next connection


                        data = clientsocket.recv(100) # store received info in data
                        msg_rcv = data.decode()
                        print ("Received Message: ",msg_rcv)
                        if msg_rcv != msg: # check if msg received is a valid msg
                                clientsocket.sendall(invalid.encode()) #send msg to client about incorrect command

                        else:
                                datetimeObject= datetime.now().strftime('%m/%d/%Y %H:%M:%S') # store current date and time in object
                                sendmsg= "Current Date and Time - " +datetimeObject
                                clientsocket.sendall(sendmsg.encode()) # encode and send message
                                
                        msg_rcv = ""

                except Exception as e: #Throw expection and exit second while loop
                        print(e)
                        print("Waiting for next connection")
                        break
        

        



s.close()
