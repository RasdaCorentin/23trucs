#!/usr/bin/env python3
import sys
from socket import *
#================================================================
# Constantes
#================================================================
HOST = '::FFFF:127.0.0.1' ;
PORT = 18887 # Arbitrary non−privileged port


def client(STr) : 
    STr.connect(serveraddr)
    print("Connection on {}".format(PORT))
    print("Input lowercase sentence : ?"); sentence = sys.stdin.readline()
    STr.send(sentence.encode())
    modifiedsentence = STr.recv(1024)
    print("From Server :", modifiedsentence.decode())
    print("Close")
    STr.close()

def server (SEc):
    capitalizedSentence = "."
    SEc = socket(AF_INET, SOCK_STREAM)
    SEc.bind(('',PORT))
    SEc.listen(1)
    print('The server is ready to receive')
    while capitalizedSentence != "": 
        print("The server is ready to receive")
        connectionSocket, addr = SEc.accept()
        print("{} connected".format(addr))
        sentence = connectionSocket.recv(1024).decode()
        capitalizedSentence = sentence.upper()
        print(capitalizedSentence)
        connectionSocket.send(capitalizedSentence.encode())
        print("Close STR")
        connectionSocket.close()
    print("Server is stopped")
    SEc.close()

def usage (msg) :
    sys.stderr.write("Usage: %s server | client [host]\n %s \n" % (sys.argv[0],msg))
    sys.exit(1)

#================================================================
hostaddr = sys.argv.pop() if len(sys.argv) == 3 else HOST
print(hostaddr)
serveraddr = (hostaddr ,PORT)
try :
    mainsock = socket(AF_INET6,SOCK_STREAM)
except OSError as error :
    print ( " ERROR : creating socket % s " % error.strerror); sys.exit(1)
#−−−−−−−−−−−−−
if sys.argv[1:] == ['client']:
    client(mainsock)
#−−−−−−−−−−−−−
elif sys.argv[1:] == ['server']:
    server(mainsock)
#−−−−−−−−−−−−−
else :
    usage(' ERROR : Parameter client or server is requested ')
sys.exit(0)

