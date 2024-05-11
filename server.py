from socket import *
from _thread import *
import threading

def recieve_thread(c):
    while True:
        x=c.recv(1024)
        print("\nClient: ",x.decode('utf-8'))

def client_thread(c):
    recieve=threading.Thread(target=recieve_thread,args=(c,))
    recieve.start()
    while True:
        c.send(input("\nServer: ").encode('utf-8'))
        
s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
host = "127.0.0.1"
port = 7000
s.bind((host,port))
s.listen(5)
print("waiting ")
try:
    while True:
        c,ad=s.accept()
        print(" successfull ",ad[0])
        
        start_new_thread(client_thread,(c,))
except KeyboardInterrupt:
    print("chat is ended")
    s.close()
        