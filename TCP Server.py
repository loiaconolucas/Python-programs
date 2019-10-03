#!/usr/bin/python3
from socket import *


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(("", serverPort))
serverSocket.listen(1)

print('The server is ready to receive')

while True:

    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    if not sentence:
        break
    print('connected to user : '+str(sentence))

   ##capSentence = sentence.upper()"""

    sentence = input('->')
    connectionSocket.send(sentence.encode())


    #connectionSocket.send(capSentence.encode())
    connectionSocket.close()