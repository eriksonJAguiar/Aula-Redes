from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random
import sys

args = sys.argv[1:]

random_generator = Random.new().read
new_key = RSA.generate(1024, random_generator)
private_key = new_key.exportKey("PEM")
public_key = new_key.publickey().exportKey("PEM")

print private_key
fd = open("%s.pem"%(str(args[0])), "wb")
fd.write(private_key)
fd.close()
print "gerado"

print public_key
fd = open("%s.pem"%(str(args[1])), "wb")
fd.write(public_key)
fd.close()
print "gerado"

	
