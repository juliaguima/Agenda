

# lista

agenda = [

]

# fim lista


while True:

    # Pede para o usuário digitar o que ele deseja fazer
    op = input("\n Qual operação você deseja realizar?\n \n * (1) - Cadastrar\n * (2) - Listar contatos\n * (3) - Alterar\n * (4) - Apagar\n * (0) - Sair\n--> ")

# Se o número digitado for igual a 1, o programa realizará o cadastro do contato
    if op == '1':

        # inputs de nome, data de nascimento, telefone, email

        print("\n----- Realizando seu cadastro ------\n ")
        nome = input("\nDigite seu nome:  ")
        data_nasc = input("\nDigite sua data de nascimento:  ")
        telefone = input("\nDigite seu telefone:  ")
        email = input("\nDigite seu email:  ")

    

        # calcula a idade usando o ano digitado e o ano atual
    
        ano = data_nasc[6:10]
        idade = 2023 - int(ano)

        # dicionario com os dados
        dados_cadastro = {'Nome': nome,
                          'Data de nascimento': data_nasc,
                          'Idade': idade,
                          'Telefone': telefone,
                          'Email': email}

    # adiciona o dicionário dados_cadastro para a lista agenda

        agenda.append(dados_cadastro)
        

# Lista os contatos
    elif op == '2':

    # verifica se a lista agenda está vazia
        if agenda == []:
            print(' -----  A agenda está vazia, realize o cadastro para continuar ------')
    # Lista os cadastros existentes
        elif agenda != []:
            for cadastro in agenda:
                print("\n ......................... \n/ Próximo cadastro: \n", )
                for chave, valor in cadastro.items():
                    print(' * ', chave, '--- > ', valor, '\n')
    # Alterar o contato
    elif op == '3':

        print('---------- Alterando o contato ---------\n')

    # Pede o nome da pessoa cadastrada
        nom = input("Qual o nome do cadastrado?\n -->  ")

    # Verifica se agenda está vazia
        if agenda == []:
            print(' -----  A agenda está vazia ------ \n')

        elif agenda != []:
            for dados_cadastro in agenda:
            # busca pelo nome digitado
                if dados_cadastro['Nome'] == nom:
            #  mostra as informações mais recentes desse usuário
                    print("\n------- Contato encontrado! --------\n\n         - Último registo -\n")
                    for key, value in dados_cadastro.items():
                            print(' * ', key, '--- > ', value, '\n')
           
            print("------- Atualização do cadastro ------\n")

            # Pede as novas informações    
                       
            novo_nome= input("\nDigite novo nome:  ")
            novo_data_nasc = input("\nDigite nova data de nascimento:  ")
            novo_telefone= input("\nDigite novo telefone:  ")
            novo_email = input("\nDigite novo email:  ")

            ano = novo_data_nasc[6:10]
            novo_idade = 2023 - int(ano)

        # substitui as informações velhas pelas novas 
                   
        for cadastro in agenda:
            if cadastro['Nome'] == nom:
                cadastro.update({ 'Nome': novo_nome,
                                   'Data de nascimento': novo_data_nasc,
                                    'Idade': novo_idade,
                                    'Telefone': novo_telefone,
                                    'Email': novo_email})  
        
        # informa o usuário sobre a atualização   

                print("Cadastro atualizado com sucesso!") 

        # se o cadastro não for encontrado, volta ao menu  
        else:
            print("\n------- Contato não encontrado! --------\n ---------------------")
        
        # excluir usuário
    
    elif op == '4':
        
        print('---------- Excluindo o contato ---------\n')
    
    # Pede o nome do cadastro
    
        inp_nom = input("Qual o nome do cadastro a ser excluído?\n -->  ")
    
    # verifica se a agenda está vazia
        if agenda == []:
            print(' -----  A agenda está vazia ------ \n')
    # Remove os dados através da chave nome
        elif agenda != []:
            for cadastro in agenda:
                if cadastro['Nome'] == inp_nom:
                    agenda.remove(cadastro)    
    #  informa o usuário sobre a exclusão
            print("\nCadastro de ",inp_nom," removido com sucesso!")
    
    # Volta ao menu se o nome não for encontrado 
        else:
            print("\n------- Contato não encontrado! --------\n ---------------------")
    #  Sair do programa
    elif op=='0':
        print("Sessão finalizada")
        break

