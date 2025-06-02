   
print('-' *40)
print('         CONTRIBUIÇÃO DO INSS      ')
print('-'*40)
s = float(input('Digite o salário: '))
m1 = float
m2 = float
if s >= 1.000 and s <= 1.693:
    m1 = (s * 8)/100
    m2 = s - m1
    print('Você deve contribuir 8% do seu salário ')
    print('Sendo no valor de: ', m1)
    print('Obtendo o valor restande de ', m2,' do seu salário')
elif s > 1.693 and s <= 2.822:
    m1 = (s * 9)/100
    m2 = s - m1
    print('Você deve contribuir 9% do seu salário ')
    print('Sendo no valor de: ', m1)
    print('Obtendo o valor restande de ', m2,' do seu salário')
elif s > 2.822 and s <= 5.645:
    m1 = (s * 11)/100
    m2 = s - m1
    print('Você deve contribuir 11% do seu salário ')
    print('Sendo no valor de: ', m1)
    print('Obtendo o valor restande de ', m2,' do seu salário')
else:
    print('Erro de entrada de dados')