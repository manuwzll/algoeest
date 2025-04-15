import random
numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
palpites=[]
while True:
    palpite=ramdom.choice(numeros)
    palpites.append(palpite)
    print(f"palpite:{palpite}")
    if palpite ==10:
        break
