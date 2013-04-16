#!/usr/bin/python
#using crypt module to created an encrypted file
import hashlib
from Crypto.Cipher import AES


password = 'filepaswd'
key = hashlib.sha256(password).digest()

mode = AES.MODE_CBC
encryptor = AES.new(key,mode)

text = '1mysq1pa$$w0r123d'
ciphertext = encryptor.encrypt(text)

#print to file the encrypted data
f = open("/tmp/python-encrypted.txt","w")
f.write(ciphertext)
f.close

##decrypt the file
#f = open ("/tmp/python-encrypt.txt","r")
#ciphertextfromfile = f.read()
#decryptor = AES.new(key,mode)
##plain = decryptor.decrypt(ciphertextfromfile)
#plain = decryptor.decrypt(ciphertext)

#f = open("/tmp/decrypted.txt","w")
#f.write(plain)
#f.close

