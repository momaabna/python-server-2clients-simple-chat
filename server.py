#Usage :python server.py
#import socket library to make socket
import socket
#import sys library to get system arguments
import sys
#import thread to make threads(multy process)
import thread
#getting system arguments
args = sys.argv
#setting port number
port = 5555#args[1]
#creat socket handler
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#setting re-use adress option to 1
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#binding port
tcp.bind(("0.0.0.0", 5555))
#start lestining to port
tcp.listen(5)
#Accept connetion from first client and display that and send greeting
(client1,(ip,port))=tcp.accept();
print 'connected 1'
client1.send('Welcome client 1')
#Accept connetion from second client and display that and send greeting
(client2,(ip,port))=tcp.accept();
print 'connected 2'
client2.send('Welcome client 2')
#function to recieve data from client2 and send to client1
def c1(id):
    print 'c1'
    while(1):
        client1.send(client2.recv(1024))
#function to recieve data from client1 and send to client2
def c2(id):
    print 'c2'
    while(1):
        client2.send(client1.recv(1024))
#start function 1 as thread
thread.start_new_thread(c1,(1,))
#start function 2 as thread
thread.start_new_thread(c2,(1,))
print 'Starting chat ....'
#keep program working
while(1):
    pass
