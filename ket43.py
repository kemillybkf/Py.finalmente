def dobrar(lista):
    conta = 0
    while conta < len(lista):
        lista[conta] *= 2
        conta = conta + 1

num = [1, 2, 3, 4, 5]
print(num)
dobrar(num)
print(num)