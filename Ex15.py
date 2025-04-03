nome= input("insira o nome do produto")
qnt= int(input("adicione quantidade de produtos comprados"))
preco = float(input("adicione o preço unitário de cada produto"))

total=qnt*preco
desconto5 = total * 0.05
if total >=100:
    print(total-desconto5)
else:
    print("sem desconto")