from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import sys

args = sys.argv[1:]

msg = raw_input('Digite uma mensagem: ')

print "encriptando ..."
key = RSA.importKey(open('%s'%(str(args[0]))).read())
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(msg)
print ciphertext

fd = open("msg_cript.txt", "wb")
fd.write(ciphertext)
fd.close()

