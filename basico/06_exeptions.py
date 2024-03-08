#execoes com python
try:
    user_number = float(input('Digite um número: '))
    print(f'Você digitou {user_number}')
except:
    print(f'Erro.\nvocê não digitou um número.')