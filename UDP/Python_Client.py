import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005

print ("Attempting to contact server at ",TCP_IP,":",TCP_PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto("SUP".encode(),(TCP_IP,TCP_PORT))
message= ''

####while message.upper() !='Q':
##    message = input("Enter Command\n")
##    s.sendall(message.encode())
##    data = s.recv(100)
##    print(data)
##        




    

