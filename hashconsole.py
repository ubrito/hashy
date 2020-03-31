import hashlib
import os

BLOCKSIZE = 65536
funcoes = [ x for x in hashlib.algorithms_guaranteed]

arquivo = input("Informe o caminho do arquivo que deseja obter o hash:\n  >>> ")

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


hash_final = hash.hexdigest()

if len(hash_final) > len(arquivo):
    tamanho = len(hash_final) + 4
else:
    tamanho = len(arquivo) + 4

print("")
print("".center(tamanho,"="))
print("ARQUIVO".center(tamanho))
print("".center(tamanho,"-"))
print(arquivo.center(tamanho))
print("".center(tamanho,"="))
print("FUNÇÃO".center(int(tamanho/3)), end="")
print("DIGEST SIZE".center(int(tamanho/3)), end="")
print("BLOCK SIZE".center(int(tamanho/3)))
print("".center(tamanho,"-"))
print(funcoes[funcao-1].center(int(tamanho/3)), end="")
print(str(hash.digest_size).center(int(tamanho/3)), end="")
print(str(hash.block_size).center(int(tamanho/3)))
print("".center(tamanho,"="))
print("HASH".center(tamanho))
print("".center(tamanho,"-"))
print(hash_final.center(tamanho))
print("".center(tamanho,"="))
print("")