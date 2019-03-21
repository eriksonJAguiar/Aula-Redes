import socket
import sys

args = sys.argv[1:]

HOST = '10.62.9.23'     
PORT = 5000            
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
tcp.send('Hi Server')
with open('%s'%(str(args[0])), 'wb') as f:
    print 'file opened'
    while True:
        print('receiving data...')
        data = tcp.recv(1024)
        if not data:
            break
        f.write(data)

f.close()
tcp.close()
