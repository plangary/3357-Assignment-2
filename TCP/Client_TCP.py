import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005

print ("Attempting to contact server at ",TCP_IP,":",TCP_PORT) 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Communicate with socket using IPV4 address using TCP
s.connect((TCP_IP, TCP_PORT)) #connect to specified IP and Port

print ("Connection to Server Established, Sending Message....")
message= '' #empty message string to store message

while message.upper() !='Q': #run loop until user enters "q"
    message = input("Enter Command\n")
    s.sendall(message.encode()) #encode then send the message
    data = s.recv(100) #receive message and store it in "data" 
    print(data.decode())#print received data
        




    

s.close()
