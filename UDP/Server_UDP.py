import socket
from datetime import datetime

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
address = (TCP_IP,TCP_PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#connect to socket IPV4 and UDP
s.bind((address)) #bind address to socket
msg= "What is the current date and time?"
msg_rcv=''
invalid = "Invalid Command!"

while True:
        while True:


                try: #try statement to catch exception and continue running after client exits
                        recv_data,addr = s.recvfrom(1024) #store received data in variable 1024 bits at a time
                        msg_rcv = recv_data.decode() # decode recieved data and store in msg_rcv
                        print ("Request Received: ",msg_rcv) 
                        if msg_rcv != msg: #check if valid request
                                s.sendto(invalid.encode(),(addr)) #send invalid info to client

                        else:
                                datetimeObject= datetime.now().strftime('%m/%d/%Y %H:%M:%S')#store current date and time in variable
                                sendmsg= "Current Date and Time - " +datetimeObject #send client the current date and time
                                s.sendto(sendmsg.encode(),(addr))
                                
                        msg_rcv = ""

                except Exception as e:
                        print(e)
                        break # break second loop and continue listenting if client exits
        
