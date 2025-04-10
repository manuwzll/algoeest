idade = int(input("Insira sua idade"))
membro=input("Você é um membro? (sim ou não)")
acompanhante = input("Você está acompanhado por um membro? (estou ou não estou)")
if idade >=18:
    print("pode entrar ")
else:
    print("não pode entrar")
if membro == "sim" and acompanhante == "estou":
    print("pode entrar,porém paga meia entrada")
else: 
    print("paga um inteiro")