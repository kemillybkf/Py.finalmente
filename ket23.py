import random

conta = 0
menor = 101
maior = 1
while conta < 21:
    num = random.randint(1,100)
    print(num)
    conta = conta + 1 
    if num < menor:
     menor = num
    if num > maior:
     maior = num 

print(num)
print('O menor número é igual a: {}' .format(menor))
print('O maior número é igual a: {}' .format(maior))
 