import random

a1 = str(input('Digite o nome do primeiro aluno:'))
a2 = str(input('Digite o nome do segundo aluno:'))
a3 = str(input('Digite o nome do terceiro aluno:'))
a4 = str(input('Digite o nome do quarto aluno:'))
lista = [a1, a2, a3, a4]
print('A lista de nomes é: {}'.format(lista))
print('Sorteio :{}'.format(random.choice(lista)))
