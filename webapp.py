#!/usr/bin/python3

import socket


class webApp:

    def parse(self, request):

        return None

    def process(self, parsedRequest):

        return ("200 OK", "<html><body><h1>It works!</h1></body></html>")

    def __init__(self, hostname, port):

        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))

        mySocket.listen(5)
        
        try:
            while True:
                print('Waiting for connections')
                (recvSocket, address) = mySocket.accept()
                request = recvSocket.recv(2048)
                parsedRequest = self.parse(request)
                (returnCode, htmlAnswer) = self.process(parsedRequest)
                print('Answering back...')
                recvSocket.send(bytes("HTTP/1.1 " + returnCode + " \r\n\r\n"
                                + htmlAnswer + "\r\n", 'utf-8'))
                recvSocket.close()
        except KeyboardInterrupt:
            print("Cerrando socket")
            mySocket.close()
