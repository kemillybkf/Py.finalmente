
import random
numero = [ random.randint(1,100) for num in range (1,21) ]
import time
time.sleep(1) 
maior = max(numero)
menor = min(numero)
print(numero)
print('O maior número é:{} '.format(maior) )
print('O menor número é:{} '.format(menor))
