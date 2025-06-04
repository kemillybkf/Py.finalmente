te = int(input('Digite o tempo de deposito: '))
v = float(input('Digite o valor que você deseja depositar: '))
taxa = float()
total = float()


total = (v*taxa)/100
if te >= 5:
    print('O valor da taxa de juros será de R$0,95')
    print('Você terá o total de: R$', total + v)
    taxa = 95
elif te < 5 or te >= 4:
    print('O valor da taxa de juros será de R$0,9')
    print('Você terá o total de: R$', total + v)
    taxa = 90
elif te < 4 or te >= 3:
    print('O valor da taxa de juros será de R$0,85')
    print('Você terá o total de: R$', total + v)
    taxa = 85
elif te < 3 or te >= 2:
    print('O valor da taxa de juros será de R$0,75')
    print('Você terá o total de: R$', total + v)
    taxa = 75
elif te < 2 or te >= 1:
    print('O valor da taxa de juros será de R$0,65')
    print('Você terá o total de: R$', total + v)
    taxa = 65
elif te < 1:
    print('O valor da taxa de juros será de R$0,55')
    print('Você terá o total de: R$', total + v)
    taxa = 55
else:
    print('Erro nos dados apresentados!')
   