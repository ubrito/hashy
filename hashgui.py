import hashlib

BLOCKSIZE = 65536

arquivo = "/home/ubrito/gui.py"

hash = hashlib.sha256()
with open(arquivo, 'rb') as arq:
    buf = arq.read(BLOCKSIZE)
    while len(buf) > 0:
        hash.update(buf)
        buf = arq.read(BLOCKSIZE)

print(len(hash.hexdigest()))
print(hash.hexdigest())