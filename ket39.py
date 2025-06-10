def saudacao(msg, nome):
    print(msg, nome)
def linha():
    print('='*30)

msg = ('olá, tudo bem?')
nome = str(input('Digite o seu nome: '))
saudacao(msg, nome)