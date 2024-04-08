import math
oposto = float(input(' digite o valor do cateto oposto:'))
adj = float(input('digite o cateto adjacente: '))
h = math.hypot(oposto, adj)
#h = (oposto**2)+(adj**2)
#print('A hipotenusa é {:.2f}'.format(math.sqrt(h)))
print('A hipotenusa é {:.2f}'.format(h))
