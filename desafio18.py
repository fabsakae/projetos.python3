import math
ang = float(input('Digite um ângulo: '))
rad = math.radians(ang)
seno = math.sin(rad)
cos = math.cos(rad)
tangente = math.tan(rad)
print('o valor do seno é {:.2f}\ndo cosseno é {:.2f}\ne da tangente é {:.2f}'.format(seno,cos,tangente))
# ou vc faz assim
#seno = math.sin(math.radians(ang))
#cos = math.cos(math.radians(ang))
#tangente = math.tan(math.radians(ang))
