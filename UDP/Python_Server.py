import socket
from datetime import datetime

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
address = ('127.0.0.1',5005)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((address))
##msg= "What is the current date and time?"
msg = 't'
msg_rcv=''


while True:
        recv_data, addr = s.recvfrom(1024)
        msg_rcv += recv_data.decode()
        if msg_rcv != msg:
                s.sendto("wrong".encode(),(address))
                msg_rcv =''

        else:
                datetime= datetime.now().strftime('%m/%d/%Y %H:%M:%S')
                sendmsg= "Current Date and Time - " +datetime
                s.sendto(sendmsg.encode(),(address))
                msg_rcv = ''
                
        
