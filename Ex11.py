
email_certo = input("crie  um email")
email_certo =str.lower(email_certo)

senha=input("crie uma senha")
if len(senha) < 8 :
    print("senha muito pequena")
else:
    senha_certa = senha
    email=input("insira o email")
    senha=input("insira a senha")
    if email == email_certo:
        if senha == senha_certa:
            print("bem vindo")
    else:
        print("Email ou senha incorretos")

 


