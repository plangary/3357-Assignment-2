import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005

print ("Attempting to contact server at ",TCP_IP,":",TCP_PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # connect to socket using IPV4 using UDP
message=''
while message.upper() !='Q': #loop until exit command q is pressed
    message = input("Enter Command\n") #ask user for input
    s.sendto(message.encode(),(TCP_IP,TCP_PORT)) # send data to socket 
    recv_data, addr = s.recvfrom(1024) #store received info in recv_data 1024 bits at a time
    print (recv_data.decode()) # decode received message
        




    

