#python tem tipagem dinamica, mas ainda assim podemos converter tipos e até 'tipar'
input('Digite seu nome: ')#recebendo dados do usuario
input('Digite sua idade em anos: ')

#ambos são recebidos como strings
name = input('Digite seu nome: ')
age = int(input('Digite sua idade: '))

print(f'Você se chama {name} e tem {age} anos.\n Seu nome é uma {type(name)} e sua idade uma {type(age)}')
#podemos usar int(), float(), str()