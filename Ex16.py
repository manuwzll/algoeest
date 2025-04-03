nota1 = int(input("insira a primeira nota"))
nota2 = int(input("insira a segunda nota"))
nota3 = int(input("inisira a terceira nota"))
media=(nota1+nota2+nota3) /3
if media >= 7:
    print("aprovado")
elif media < 7 and media >5:
    print("recuperação")
else:
    print("reprovado")