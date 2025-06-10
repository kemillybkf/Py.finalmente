def mostrar(*args):
    return args

nome = str(input('Digite o nome: '))
idade = int(input('Digite a idade: '))
filho = int(input('Digite o n de filhos: '))
renda = float(input('Digite a sua renda: '))

dados = mostrar(nome, idade, filho, renda)
print(dados)