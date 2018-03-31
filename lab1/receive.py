
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import base64
import sys,os,signal
import binascii

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

def getpubkey():
    with open('./pub.pem','rb') as f:
        pub = f.read()
        key = RSA.importKey(pub)
    return key

if __name__ == '__main__':
    key = getpubkey()
    
    a = modinv(2, key.n)
    
    input()
    dec = input()
    dec_int = int(binascii.hexlify(base64.b64decode(dec)), 16)
    
    flag = (a * dec_int) % key.n

    f = binascii.unhexlify(hex(flag)[2:])
    print(f)
    
