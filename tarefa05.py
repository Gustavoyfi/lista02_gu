sexo = input("Informe seu sexo masculino/femenino: ")
altura = float(input("Informe sua altura: "))
if sexo == "masculino":
    peso = (72.7*altura) - 58
    print(f"Seu peo ideal é {peso}")
elif sexo == "fmenino":
    peso1 = (62.1*altura)-44.7
    print(f"Seu peo ideal é {peso1}")
else: 
    print("Erro!")
