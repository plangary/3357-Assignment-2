import socket

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
        print(f"Connection has been established!")

        data = clientsocket.recv(100)
        if not data:
                break
        elif data == 'killsrv':
                clientsocket.close()
                sys.exit()
        else:
                print(data)
                clientsocket.sendall("sending".encode())
                #msg_rcv += data.decode()
                #if msg_rcv != msg:
                 #   clientsocket.sendall(invalid.encode())
                  #  msg_rcv = ''
                #else:
                 #   clientsocket.sendall("good".encode())
                  #  msg_rcv = ''
         

        



    





#print('Client Address:', addr)
#data = conn.recv(16)
#s.close()
