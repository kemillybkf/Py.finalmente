nota = float(input('Digite a nota do aluno: '))
faltas = int(input('Digite a quantidade de faltas do aluno: '))
if nota < 5 or faltas > 4:
    print('O aluno está REPROVADO!!!!')
else:
    print('O aluno está APROVADO!!!')