#set é um conjuto desordenato e imutável em python, ele não ceitas duplicatas.
#criando um set
cities = {'Betim', 'Belo Horizonte', 'Contagem', 'Esmeraldas'}
print(cities)
print(type(cities))
#inserindo novos itens
cities.add('Ouro Preto')
print(cities)
#removendo
cities.remove('Ouro Preto')
print(cities)
#itens duplicados de uma lista em um set
duplicate_numbers = [1,1,2,2,3,3,4,4]
no_duplicate_numbers = set(duplicate_numbers)
print(f'Lista : {duplicate_numbers}\nSet : {no_duplicate_numbers}')
