email = input("Digite seu email: ")
senha = input("Digite sua senha: ")

print(f"\nSeu email {email} foi cadastrado com sucesso")

email2 = input("\nDigite seu email novamente: ")
senha2 = input("Digite sua senha novamente: ")


if email == email2 and  senha == senha2:

    print("\nDados confirmados")
else:
    print("\nDados incorretos")
