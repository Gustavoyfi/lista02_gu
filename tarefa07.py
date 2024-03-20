idade = int(input("Informe sua idade: "))
peso = float(input("Informe seu peso: "))
if idade > 15 and peso <120:
	print("Você está liberado")
else:
	print("Você não está liberado por ser menos de 16 anos ou por ter mais que 120kg")