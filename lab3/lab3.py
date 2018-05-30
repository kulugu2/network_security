import socket
import re

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('140.113.194.66',8787))
    data = s.recv(1024)
    print(data.decode())
    #a = re.split('\n', data.decode().strip())
    #print(a)
    #s.settimeout(1.0)
    data = s.recv(1024)
    print(data.decode())
    s.send('1\n'.encode())
    data = s.recv(1024)
    print(data.decode())

    s.send('-1\n'.encode())
    data = s.recv(1024)
    print(data.decode())
    data = data.decode().replace('\n', ' ')
    data = data.replace('\t', ' ')
    a = data.strip().split(' ')
    i = a.index('Age:')
    secret = int(a[i+1])
    print(secret)

    
    s.send('2\n'.encode())
    data = s.recv(1024)
    print(data.decode())
    s.send((str(secret)+'\n').encode())

    data = s.recv(1024)
    print(data.decode())

    s.send('-3\n'.encode())
    #s.send('12\n'.encode())
    data = s.recv(1024)
    print(data.decode())
    s.send('13\n'.encode())
    l = [8, 4, 137, 224]
    l1 = [224, 137, 4, 8]
    s.send('aaaaaaaa'.encode()+bytes(l1))
    #s.send(bytes(l))
    #s.send('\n'.encode())
    #s.send('aaaaaaaa\xe0\x89\x04\x08\n'.encode())
    data = s.recv(1024)
    print(data.decode())
    data = s.recv(1024)
    print(data.decode())
    data = s.recv(1024)
    print(data.decode())
