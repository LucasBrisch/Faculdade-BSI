creditos_cartão = 0  # saldo inicial do cartão
preco_passagem = 6  # preço inicial da passagem
tentativas = 3  # tentativas de senha
senha = "admin123"  # senha do administrador
start = True

while start:
    volta = 0
    print()
    print("Bem-vindo ao sistema da Urbs!")
    print("Você é usuário ou administrador?\n")
    print("[1] Usuário")
    print("[2] Administrador")
    print("[3] Sair\n")
    escolha_menu = (input("Escolha uma opção: "))

    if escolha_menu == '1':
        while True:
            print("Você é um usuário\n")
            print(f"Você tem R${creditos_cartão}")
            print(f"O preço da passagem é de R${preco_passagem}\n")
            print("Você deseja carregar o cartão ou fazer uma viagem?\n")
            print("[1] Carregar cartão")
            print("[2] Fazer viagem")
            print("[3] voltar para página inicial\n")
            escolha_user = (input("Escolha uma opção: "))

            if escolha_user == '1':
                creditos_adicionados = int(input("Quantos créditos deseja colocar no cartão? (Se deseja voltar digite '0')\n"))
                if creditos_adicionados < 0:
                    print("Você não pode adicionar créditos negativos, tente novamente!\n")
                elif creditos_adicionados == 0:
                    print("Voltando para o menu de usuário\n")
                else:
                    creditos_cartão += creditos_adicionados
                    print(f"Você adicionou R${creditos_adicionados} ao seu cartão agora você tem R${creditos_cartão}\n")
            elif escolha_user == '2':
                if creditos_cartão >= preco_passagem:
                    creditos_cartão -= preco_passagem
                    print(f"Você fez uma viagem! O custo foi de R${preco_passagem}")
                    print(f"Agora você tem R${creditos_cartão}\n")
                else:
                    while True:
                        print("Você não tem créditos suficientes para fazer uma viagem, deseja carregar o cartão? \n")
                        print("[1] Sim")
                        print("[2] Não\n")
                        escolha = (input("Escolha uma opção: "))
                        if escolha == '1':
                            creditos_adicionados = int(input("Insira quantos créditos deseja colocar no cartão? (Se deseja voltar digite '0'): "))
                            if creditos_adicionados < 0:
                                print("Você não pode adicionar créditos negativos, tente novamente!\n")
                            elif creditos_adicionados == 0:
                                print("Voltando para o menu de usuário\n")
                                break
                            else:
                                creditos_cartão += int(creditos_adicionados)
                                print(f"Você adicionou R${creditos_adicionados} ao seu cartão agora você tem R${creditos_cartão}\n")
                                break
                        elif escolha == '2':
                            print("Você não pode fazer uma viagem sem créditos, volte quando quiser recarregar\n")
                            break
                        else:
                            print("Opção inválida, tente novamente!\n")
            elif escolha_user == '3':
                break
            else:
                print("Opção inválida, tente novamente!")

    elif escolha_menu == '2':
        while volta == 0:
            print("Você é um administrador, favor inserir a senha para continuar (caso não seja um administrador, digite 'sair')")
            senha_inserida = input("Digite a senha: ")
            if senha_inserida == 'sair':
                break
            elif senha_inserida == senha:
                while True:
                    print()
                    print("Bem-vindo administrador! O que você deseja fazer?\n")
                    print("[1] Alterar preço da passagem")
                    print("[2] Verificar saldo do usuário")
                    print("[3] Definir uma nova senha")
                    print("[4] Voltar para página inicial\n")
                    escolha_adm = (input("Escolha uma opção: "))

                    if escolha_adm == '1':
                        while True:
                            novo_preco_passagem = float(input("Qual será o novo preço da passagem? (Se deseja voltar digite '0'): "))
                            if novo_preco_passagem < 0:
                                print("O preço da passagem não pode ser negativo, tente novamente!\n")
                            elif novo_preco_passagem == 0:
                                print("Voltando para o menu de administrador\n")
                                break
                            else:
                                preco_passagem = novo_preco_passagem
                                print(f"O preço da passagem agora é de R${preco_passagem}\n")
                                break
                    elif escolha_adm == '2':
                        print()
                        print(f"O saldo do usuário é de R${creditos_cartão}\n")
                    elif escolha_adm == '3':
                        while True:
                            print('caso deseje voltar digite "voltar" (a senha não pode ser "voltar")')
                            nova_senha = input("Insira a nova senha: ")
                            if nova_senha == 'voltar':
                                break
                            elif nova_senha == senha:
                                print("A nova senha não pode ser igual à senha antiga, tente novamente")
                            elif len(nova_senha) < 4:
                                print("A senha deve ter no mínimo 4 caracteres, tente novamente")
                            else:
                                senha = nova_senha
                                print("Senha redefinida com sucesso!\n")
                                break
                    elif escolha_adm == '4':
                        volta += 1
                        break
                    else:
                        print("Opção inválida, tente novamente!\n")
            else:
                tentativas -= 1
                if tentativas == 0:
                    print()
                    print("Você excedeu o número de tentativas, desligando o sistema por motivos de segurança")
                    start = False
                    break
                else:
                    print()
                    print(f"Senha incorreta, você tem mais {tentativas} tentativas restantes")
    elif escolha_menu == "3":
        print("Desligando o sistema...")
        start = False
    else:
        print("Opção inválida, tente novamente!")
