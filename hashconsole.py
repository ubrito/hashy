import hashlib
import os

BLOCKSIZE = 65536
funcoes = [ x for x in hashlib.algorithms_available ]

arquivo = "/home/ubrito/gui.py" #input("Informe o caminho do arquivo que deseja obter o hash:\n  >>> ")

while not os.path.isfile(arquivo):
    arquivo = input("\nArquivo não encontrado no caminho digitado!!\nInforme o caminho do arquivo que deseja obter o hash:\n  >>> ")

print("\nEscolha a função de hash:\n")

for i in range(len(funcoes)):
    print("{}\t-\t{}".format(i+1, funcoes[i]))

funcao = int(input("\n  >>> "))

hash = hashlib.new(funcoes[funcao-1])


try:
    with open(arquivo, 'rb') as arq:
        buf = arq.read(BLOCKSIZE)
        while len(buf) > 0:
            hash.update(buf)
            buf = arq.read(BLOCKSIZE)

except:
    print("Houve algum problema!")

print("Função - {}".format(funcoes[funcao-1]))
print(hash.digest_size)
print(hash.block_size)
print(hash.hexdigest())