#!/usr/bin/python
from Crypto.Cipher import AES
import base64
import os
import binascii


def encrypt(plain_text, secret_key, nonce):
    """encrypts a plain text string using the given secret_key and nonce - usually a session id"""
    
    #nonce = 'j8h6g88uu9ot6r44'
    encobj = AES.new(secret_key, AES.MODE_CBC, nonce)
    
    str_length = len(plain_text) + (16 - (len(plain_text) % 16))
    padded = plain_text.rjust(str_length, '~')
    
    encrypted_text = encobj.encrypt(padded)
    return encrypted_text.encode('hex')

ciphertext = encrypt('foobar12', '1234567812345678', 'some_password')
print ciphertext
