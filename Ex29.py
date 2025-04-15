valores[]
for i in range(4):
    valor=int(input("digite um número:"))
    valores.append(valor)
numero=int(input("digite um numero adicional:"))
for i in range(len(valores)):
    valores[1]*=numero
print("novos valores da lista",valores)