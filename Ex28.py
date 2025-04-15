numeros=[]
for i in range(8):
    numero=int(input("digite um numero"))
    numeros.append(numero)pares=[]
ímpares=[]
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        ímpares.append(numero)
    print("numeros pares:",pares)
    print("numeros impares:",ímpares)