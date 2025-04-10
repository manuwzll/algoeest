idade=int(input("Insira sua idade"))
genero=input("Insira seu genêro (f ou m)")
atleta=input("Você é atleta? (sim ou não)")
if idade < 15:
    print("Artigos infantis")
elif idade >= 15 and idade < 21 and genero == "f" and atleta == "não":
    print("Maquiagem e moda")
elif idade >=15 and idade < 32 and genero == "m" and atleta == "sim":
    print("Artigo esportivos")
elif idade >= 15 and idade <21 and genero == "m" and atleta == "não":
    print("Videogames") 
elif idade >= 21 and idade <32 and genero == "m" and atleta == "não":
    print(" livros, jardinagem e eletrodomesticos")
else: 
    idade >= 32 and genero == "f" and atleta == "não":
    print("IEDUEIDUEI")