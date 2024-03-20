import math
a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

delta = (b ** 2) - 4 * a * c

if delta <0:
    print("Não tem raízes reais")
elif delta == 0:
    x = -b/(2*a)
    print(f"temos como soulução duas raizes reais e iguais np valor de {x}")
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("Temos como soulução duas raízes reais e diferentes")
    print(f"X1 é = {x1}")
    print(f"X2 é = {x2}")