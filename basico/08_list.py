#criando listas em python
cars = ['Uno', 'Palio', 'Gol', 'Celta']
#acessando dados
print(cars)
print(cars[1])
#verificando tipo
print(type(cars))
#adiconar itens ao fim da lista
cars.append('Marea')
print(cars)
#adicionar item ao inicio da lista
cars.insert(0, 'Parati')#o indice pode ser escolhido
print(cars)
#deletando itens
del cars[5]
print(cars)

cars.remove('Parati')
print(cars)

car = cars.pop()
print(car)