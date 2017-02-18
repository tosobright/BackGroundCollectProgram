__author__ = 'Toso'
import socket
import time
import threading
import Queue

TcpQueue=Queue.Queue(maxsize=100)

def tcplink(sock,addr):
    data,savedata='',''
    flag=True
    print('Accept new connection from %s:%s' %addr)
    sock.send('Welcome!\n')
    while flag:
        data=sock.recv(1024)
        time.sleep(1)
        if data=='Exit' or not data:
            flag=False
        if data=='Save':
            TcpQueue.put(savedata)
        sock.send('%s\n'%data)
        savedata=data
    sock.close()
    print('Connection from %s:%s closed' %addr)

def tcplisten():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('0.0.0.0',8899))
    s.listen(5)
    print('Server is running...')
    while True:
        print('TCP Listening.............')
        sock,addr=s.accept()
        t=threading.Thread(target=tcplink,args=(sock,addr))
        t.start()


