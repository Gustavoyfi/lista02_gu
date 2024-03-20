codigo = input("Informe o código [1] para a PUC e [2] para a UNICAMP: ")
nota = int(input("Informe sua média: "))
if codigo == 1:
    if nota >= 7:
        print("aprovado")
    elif nota <7 and nota>=4: 
        print("Em exame")
    else: 
        print("Reprovado")
elif codigo == 2:
    if nota >= 5:
        print("Aprovado")
    else:
        print("Em exame")
else:
    print("Erro")
    
