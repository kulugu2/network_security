
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import base64
import sys,os,signal
import binascii

def getpubkey():
    with open('./pub.pem','rb') as f:
        pub = f.read()
        key = RSA.importKey(pub)
    return key

def readflag_enc():
    with open('./flag.enc', 'r') as f:
        flag_enc = f.read().strip()
    return flag_enc

if __name__ == '__main__':
    key = getpubkey()
    #print(key.n)
    #print(type(key.e))
    
    flag_enc = base64.b64decode(readflag_enc())
    #print(flag_enc)

    flag_int = int(binascii.hexlify(flag_enc), 16)
    #print(flag_int)
    x = key.encrypt(2,'')[0]
    #print(x, type(x))
    y = (flag_int * x) % key.n
    #print(y)
    #print(hex(y))
    #print(len(hex(y)[2:]))
    y_base64 = base64.b64encode(binascii.unhexlify(
        hex(y)[2:]))
    #print(type(binascii.unhexlify(hex(y)[2:])))
    #print(str(y_base64))
    print(str(y_base64)[2:-1])
    
