#!/usr/bin/python
#
import os, random, struct, hashlib, StringIO, yaml
from Crypto.Cipher import AES

def decrypt_file(password, in_filename, chunksize=24*1024):
    """ Decrypts a file which orginal format before encrytpion is YAML
    	using AES (CBC mode) with the
        given password hashed and used as the key.
	Decrypted file will remain in memory
    """
    key = hashlib.sha256(password).digest()
    out_filename = StringIO.StringIO()

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

	outfile = StringIO.StringIO()
        while True:
          chunk = infile.read(chunksize)
          if len(chunk) == 0:
            break
          outfile.write(decryptor.decrypt(chunk))

        outfile.truncate(origsize)
	#decrypted_content = outfile.getvalue()
	decrypted_content = yaml.load(outfile.getvalue())
	
    return decrypted_content

decrypted_data = decrypt_file('foobar','./passwords.yml.enc')
print decrypted_data
