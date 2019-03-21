import socket
HOST = '127.0.0.1'     
PORT = 5000            
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
tcp.send('Hi Server')
with open('received_file', 'wb') as f:
    print 'file opened'
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        f.write(data)

f.close()
print('Successfully get the file')
#print 'Para sair use CTRL+X\n'
#msg = raw_input()
#while msg <> '\x18':
#    tcp.send (msg)
#    msg = raw_input()
tcp.close()
