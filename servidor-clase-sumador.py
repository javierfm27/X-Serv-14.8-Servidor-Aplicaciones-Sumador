#!/usr/bin/python3

from webapp import webApp
import socket

class servSum(webApp):
    state = 0
    operando = 0

    def parse(self, request):
        peticion = request.decode('utf-8', 'strict')
        print(peticion)
        peticionParsed = peticion.split()[1][1:]
        return peticionParsed

    def process(self, parsedRequest):
        codeHTTP = "200 Ok"
        if self.state == 0:
            self.operando = int(parsedRequest)
            htmlAnswer = "<!DOCTYPE html> <html>" + "Ha introducido " + str(parsedRequest) + ", Introduce el segundo operando " + " </body></html>"
            self.state = 1
        else:
            print("Debe entrar aqui")
            resultado = self.operando + int(parsedRequest) #Este seria el opeando 2
            htmlAnswer = "<!DOCTYPE html><html><body> El resultado de sumar " + str(self.operando) + " y " + parsedRequest + " es " + str(resultado) + " </body></html>"
            self.state = 0
        return (codeHTTP, htmlAnswer)

    def __init__(self, hostname, port, state):
        webApp.__init__(self, hostname, port)
        self.state = 0

if __name__ == "__main__":
    testServSum = servSum(socket.gethostname(), 1231, 0)
