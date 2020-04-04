import hashlib
import os

BLOCKSIZE = 65536


def calcula_hash(arquivo, funcao):
    hash = hashlib.new(funcao)

    try:
        with open(arquivo, 'rb') as arq:
            buf = arq.read(BLOCKSIZE)
            while len(buf) > 0:
                hash.update(buf)
                buf = arq.read(BLOCKSIZE)

    except:
        print("Houve algum problema!")

    return hash.hexdigest(), hash.digest_size, hash.block_size


def main():
    funcoes = [x for x in hashlib.algorithms_guaranteed]
    arquivo = input("Informe o caminho do arquivo que deseja obter o hash:\n  >>> ")
    while not os.path.isfile(arquivo):
        arquivo = input(
            "\nArquivo não encontrado no caminho digitado!!\n"
            "Informe o caminho do arquivo que deseja obter o hash:\n  >>> ")

    print("\nEscolha a função de hash:\n")

    for i in range(len(funcoes)):
        print("{}\t-\t{}".format(i + 1, funcoes[i]))

    funcao = int(input("\n  >>> "))

    hash_final, ds, bs = calcula_hash(arquivo, funcoes[funcao - 1])

    if len(hash_final) > len(arquivo):
        tamanho = len(hash_final) + 4
    else:
        tamanho = len(arquivo) + 4

    print("")
    print("".center(tamanho, "="))
    print("ARQUIVO".center(tamanho))
    print("")
    print(arquivo.center(tamanho))
    print("".center(tamanho, "="))
    print("FUNÇÃO".center(int(tamanho / 3)), end="")
    print("DIGEST SIZE".center(int(tamanho / 3)), end="")
    print("BLOCK SIZE".center(int(tamanho / 3)))
    print("")
    print(funcoes[funcao - 1].center(int(tamanho / 3)), end="")
    print(str(ds).center(int(tamanho / 3)), end="")
    print(str(bs).center(int(tamanho / 3)))
    print("".center(tamanho, "="))
    print("HASH".center(tamanho))
    print("")
    print(hash_final.center(tamanho))
    print("".center(tamanho, "="))
    print("")


if __name__ == '__main__':
    main()
