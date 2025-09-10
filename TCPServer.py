from socket import *
import threading

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(2)
print('Server is ready')

def handleClient(connectionSocket):
    openConnection = True    
    while openConnection:
        sentence = connectionSocket.recv(1024).decode()
        sentence = sentence.strip()
        print(sentence)
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode())
        if capitalizedSentence == 'EXIT':
            openConnection = False
            connectionSocket.close()

while True:
    connectionSocket, addr = serverSocket.accept()
    print(addr)
    clientThread = threading.Thread(target=handleClient, args=(connectionSocket,))
    clientThread.start()
    #handleClient(connectionSocket)

sdhfjknk