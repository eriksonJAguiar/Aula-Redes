from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import sys

args = sys.argv[1:]


print "decriptando ..."
key = RSA.importKey(open('%s'%(str(args[0]))).read())
cipher = PKCS1_OAEP.new(key)

cipher_msg = open('%s'%(str(args[1])), 'rb').read()

print cipher_msg

msg = cipher.decrypt(str(cipher_msg))

print msg

