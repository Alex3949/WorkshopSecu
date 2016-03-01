from socket import *
import thread
from time import sleep

BUFF = 1024
HOST = '127.0.0.1'# must be input parameter @TODO
PORT = 9999 # must be input parameter @TODO

passwd = "SucH_p4sSw0rD!"

def checkPasswd(string):
    if len(string) > len(passwd):
        return False
    if string == passwd:
        return True
    if string == passwd[:len(string)]:
        sleep(1)
    return False

def handler(clientsock,addr):
    clientsock.send("Veillez entrer le mot de passe.\n>>> ")
    data = clientsock.recv(BUFF)
    print(repr(addr) + ' recv:' + repr(data))
    string = data.strip()
    if checkPasswd(string):
        clientsock.send("Felicitation, vous pouvez utiliser ce password comme flag.\n")
    else:
        clientsock.send("Oh non, ce n'est pas le bon password.\n")

    clientsock.close()
    print(addr, "- closed connection") #log on console

if __name__=='__main__':
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(5)
    while 1:
        print('waiting for connection... listening on port', PORT)
        clientsock, addr = serversock.accept()
        print('...connected from:', addr)
        thread.start_new_thread(handler, (clientsock, addr))
