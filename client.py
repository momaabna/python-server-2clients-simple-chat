#usage : python client.py [IP]
import socket
import sys
import thread
args = sys.argv
ip = args[1]
port = 5555
tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
print 'Connected..'
#Connect to server
tcp.connect((ip,port))
#recieve greeting and display it
g = tcp.recv(1024)
print 'Greeting from Server :' + g
#function to lesten to keyboard and send
def inp(id):
    while (True):

        mess = raw_input('')
        tcp.send(mess)
        print 'Me :' +mess
#function to ricieve and display
def rec(id):
    while(1):
        print 'Another side:' + tcp.recv(1024)
#start inp function as thread
thread.start_new_thread(inp,(1,))
#start rec function as thread
thread.start_new_thread(rec,(1,))

while(1):
    pass
