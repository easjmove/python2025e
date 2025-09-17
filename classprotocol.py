from socket import *
import threading
import json
import morsecode

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(2)
print('Server is ready')

def handleClient(connectionSocket):
    connectionSocket.send("skriv dit navn".encode())
    name = connectionSocket.recv(1024).decode()
    connectionSocket.send(("Velkommen " + name).encode())

    while True:
        jsonstring = connectionSocket.recv(1024).decode()
        dictionary = json.loads(jsonstring)
        clientFunction = dictionary["funktion"]
        values = dictionary["values"]
        result = "not implemented funktion"

        if clientFunction == "plus":
            result = sum(values)
        
        elif clientFunction == "encode":
            result = morsecode.encrypt(values[0].upper())

        connectionSocket.send(str(result).encode())



while True:
    connectionSocket, addr = serverSocket.accept()
    print(addr)
    clientThread = threading.Thread(target=handleClient, args=(connectionSocket,))
    clientThread.start()
    #handleClient(connectionSocket)