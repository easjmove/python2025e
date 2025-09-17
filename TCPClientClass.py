from socket import *
import json

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
serverSentence = clientSocket.recv(1024).decode()
name = input(serverSentence)
clientSocket.send(name.encode())
serverSentence = clientSocket.recv(1024).decode()
print(serverSentence)

while True:
    print('Vælg funktion: alle funktioner')
    funktion = input("Funktion nummer: ")
    data = ""
    match funktion:
        case "1":
            tal1 = input("Tal1: ")
            tal2 = input("Tal2: ")
            data = {"funktion":"plus", "values":[int(tal1), int(tal2)]}
    clientSocket.send(json.dumps(data).encode())
    print(clientSocket.recv(1024).decode())

