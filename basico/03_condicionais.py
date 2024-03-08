#operadores condicionais

number_one = 1
number_two = 2
print(number_one == number_two)#iqualdade
print(number_one != number_two)#diferente
print(number_one > number_two)#maior que
print(number_one < number_two)#menor que
print(number_one >= number_two)#maior ou igual
print(number_one <= number_two)#menor ou igual

#declarações condicionais
if number_one < number_two:
    print('1 é maior que dois')
else:
    print('Algo errado')

if type(1) == type('1'):
    print('iguais')
elif type(1) != type('1'):
    print('diferentes')
else:
    print('erro')