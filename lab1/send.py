
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import base64
import sys,os,signal
import binascii
import socket

def getpubkey():
    with open('./pub.pem','rb') as f:
        pub = f.read()
        key = RSA.importKey(pub)
    return key

def readflag_enc():
    with open('./flag.enc', 'r') as f:
        flag_enc = f.read().strip()
    return flag_enc

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('moduler inverse does not exist')
    else:
        return x % m


if __name__ == '__main__':
    key = getpubkey()
    
    flag_enc = base64.b64decode(readflag_enc())

    flag_int = int(binascii.hexlify(flag_enc), 16)
    x = key.encrypt(2,'')[0]
    y = (flag_int * x) % key.n
    y_base64 = base64.b64encode(binascii.unhexlify(
        hex(y)[2:]))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('140.113.194.66',8888))
    data = s.recv(1024)
    #print(data.decode())
    
    s.send((str(y_base64)[2:-1]+'\n').encode())
    data = s.recv(1024)
    #print(data)
    data = s.recv(1024)
    #print(data.decode())
    
    a = modinv(2, key.n)
    
    dec_int = int(binascii.hexlify(base64.b64decode(data)), 16)
    
    flag = (a * dec_int) % key.n

    f = binascii.unhexlify(hex(flag)[2:])
    print(f)
