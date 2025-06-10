inicio = int(input('Digite um número inicial:'))
final = int(input('Digite o número final: '))
passo = int(input('Digite o intervalo: '))

for conta in range(inicio, final+1, passo):
    print('Número {}' .format(conta))
print('Fim Contagem')