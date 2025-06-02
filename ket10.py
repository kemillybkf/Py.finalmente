ano = int(input('Digite o ano do seu automóvel: '))
p = float(input('Digite o peso do seu automóvel: '))

if ano <= 1970 and p <= 1200:
 print('Classe 1')
 print('Taxa de registro: 16,50')
elif ano <= 1970 and p <= 1700:
 print('Classe 2')
 print('Taxa de registro: 25,50')
elif ano <= 1970 and p > 1700:
 print('Classe 3')
 print('Taxa de registro: 46,50')

elif ano <= 1979 and p <= 1200:
 print('Classe 4')
 print('Taxa de registro: 27,00')
elif ano <= 1979 and p <= 1700:
 print('Classe 5')
 print('Taxa de registro: 30,50')
elif ano <= 1979 and p > 1700:
 print('Classe 6')
 print('Taxa de registro: 52,50')

elif ano >= 1980 and p <= 3600:
 print('Classe 7')
 print('Taxa de registro: 19,50')
elif ano >= 1980 and p > 3600:
 print('Classe 8')
 print('Taxa de registro: 52,50')
else: 
 print('Erro nos dados informados!!')