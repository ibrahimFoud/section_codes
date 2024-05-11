from socket import *
from _thread import *
import threading

def recieve_thread(c):
    while True:
        x=c.recv(1024)
        print("\nClient: ",x.decode('utf-8'))

s=socket(AF_INET,SOCK_STREAM)
host = "127.0.0.1"
port = 7000
s.connect((host,port))

recieve=threading.Thread(target=recieve_thread,args=(s,))
recieve.start()

while True:
        s.send(input("\nServer :").encode( 'utf-8' ))