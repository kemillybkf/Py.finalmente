def usuario(*val):
    val = []
    res = 'S'
    while res == 'S':
        val.append(int(input('Digite um número: ')))
        res = str(input('Continuar [S/N]: ')).upper()
        print(val)


usuario()