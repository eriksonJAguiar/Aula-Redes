import socket
import sys

args = sys.argv[1:]

HOST = '10.62.9.23'              
PORT = 5000         
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(5)
print('sevidor iniciado ...')
while True:
    con, cliente = tcp.accept()
    print 'Concetado por', cliente
    filename = args[0]
    fd = open(filename,'rb')
    f = fd.read(1024)
    while(f):
        con.send(f)
        f = fd.read(1024)

    fd.close()


    print('Arquivo enviado!')
    con.close()
    break

