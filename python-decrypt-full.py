#!/usr/bin/python
#
import os, random, struct, hashlib, StringIO
from Crypto.Cipher import AES

def decrypt_file(password, in_filename, out_filename=None, chunksize=24*1024):
    """ Decrypts a file using AES (CBC mode) with the
        given key. Parameters are similar to encrypt_file,
        with one difference: out_filename, if not supplied
        will be in_filename without its last extension
        (i.e. if in_filename is 'aaa.zip.enc' then
        out_filename will be 'aaa.zip')
    """
    key = hashlib.sha256(password).digest()
    if not out_filename:
        #out_filename = os.path.splitext(in_filename)[0]
        out_filename = StringIO.StringIO()

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        #with open(out_filename, 'wb') as outfile:
	outfile = StringIO.StringIO()
        while True:
          chunk = infile.read(chunksize)
          if len(chunk) == 0:
            break
          outfile.write(decryptor.decrypt(chunk))

        outfile.truncate(origsize)
	decrypted_content = outfile.getvalue()
	print decrypted_content

decrypt_file('foobar','./passwords.yml.enc')
