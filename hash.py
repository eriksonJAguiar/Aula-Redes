import hashlib

print('Digite a mensagem:')
msg = raw_input()


sha = hashlib.sha256(msg.encode()).hexdigest()
print('\n')
print('-----------------------------------')
print('mensagem: %s'%(msg))
print('Hash: %s'%(sha))
print('------------------------------------\n')

