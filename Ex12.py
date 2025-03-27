status_da_conta = True
saldo = float(input("insira o saldo da sua conta"))
if saldo == 0:
    status_da_conta = False
    print("Sua conta está inativa")
elif saldo<0:
    print("Renegocie sua divida")
else:
    print ("Sua conta está ativa")
