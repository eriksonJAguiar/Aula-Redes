from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import sys
import base64

args = sys.argv[1:]


print "encriptando ..."
key = RSA.importKey(open('%s'%(str(args[0]))).read())
cipher = PKCS1_OAEP.new(key)

fd = open("%s"%(args[1]), "rb")
msg = fd.read()
fd.close()

ciphertext = cipher.encrypt(msg)
ciphertext = base64.b64encode(ciphertext)
print ciphertext


fd = open('msg.crypt','wb')
fd.write(ciphertext)
fd.close()
