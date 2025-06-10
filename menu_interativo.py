from InquirerPy import inquirer

def menu_interativo():
    """
    A função menu_interativo é responsável por executar um pequeno sistema de gerenciamento de usuários
    e o quanto vale cada pegada de carbono de cada um no terminal, utilizando a biblioteca InquirerPy 
    para criar um menu interativo. Essa função encapsula todas as operações do programa e oferece uma
    interface clara e amigável ao usuário.
    """
    usuarios = []

    def adicionar_usuario():
        nome = inquirer.text(message='Digite o nome do usuário:').execute()
        usuarios.append({'nome': nome,})
        print(f'Usuário {nome} adicionado com sucesso!\n')

    def ver_usuarios():
        if not usuarios:
            print('Nenhum usuário cadastrado.\n')
        else:
            print('Usuários cadastrados:')
            for i, usuario in enumerate(usuarios, 1):
                print(f'{i}. {usuario['nome']}')
            print()

    def calculadora_media():
        entrada = input('Digite suas notas separadas por espaço: ')
        try:
            notas = list(map(float, entrada.split()))
            if notas:
                media = sum(notas) / len(notas)
                print(f'A sua média de nota é: {media:.2f}\n')
            else:
                print('Nenhuma nota válida fornecida\n')
        except ValueError:
            print('Entrada inválida. Use apenas números separados por espaço.\n')

    def editar_usuario():
        if not usuarios:
            print('Nenhum usuário cadastrado. \n')
            return
        
        nome_antigo = inquirer.select(
            message='Escolha o usuário para editar:',
            choices=[usuario['nome'] for usuario in usuarios],
        ).execute()

        novo_nome = inquirer.text(message=f'Digite o novo nome para "{nome_antigo}":').execute()

        for usuario in usuarios:
            if usuario['nome'] == nome_antigo:
                usuario['nome'] = novo_nome
                print(f'Nome alterado para "{novo_nome}" com sucesso!\n')
                break

    def remover_usuario():
        if not usuarios:
            print('Nenhum usuário cadastrado. \n')
            return
        
        nome_escolhido = inquirer.select(
            message='Escolha o usuário para remover:',
            choices=[usuario['nome'] for usuario in usuarios],
        ).execute()

        for i, usuario in enumerate(usuarios):
            if usuario['nome'] == nome_escolhido:
                usuarios.pop(i)
                print(f'Usuário "{nome_escolhido}" removido com sucesso.\n')
                break

    while True:
        opcao = inquirer.select(
            message='Selecione uma opção:',
            choices=[
                'Adicionar usuário',
                'Ver usuários cadastrados',
                'Calcule sua média',
                'Editar nome de um usuário',
                'Remover usuário',
                'Sair',
            ],
        ).execute()

        if opcao == 'Adicionar usuário':
            adicionar_usuario()
        elif opcao == 'Ver usuários cadastrados':
            ver_usuarios()
        elif opcao == 'Calcule sua média':
            calculadora_media()
        elif opcao == 'Editar nome de um usuário':
            editar_usuario()
        elif opcao == 'Remover usuário':
            remover_usuario()
        elif opcao == 'Sair':
            print('Saindo do programa...')
            break

menu_interativo()