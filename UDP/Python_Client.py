import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005

print ("Attempting to contact server at ",TCP_IP,":",TCP_PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message=''
while message.upper() !='Q':
    message = input("Enter Command\n")
    s.sendto(message.encode(),(TCP_IP,TCP_PORT))
    recv_data, addr = s.recvfrom(1024)
    print (recv_data.decode())
        




    

