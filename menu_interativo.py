from InquirerPy import inquirer

def menu_interativo():
    usuarios = []

    def adicionar_usuario():
        nome = inquirer.text(message='Digite o nome do usuário:').execute()
        usuarios.append(nome)
        print(f'Usuário {nome} adicionado com sucesso!\n')

    def ver_usuarios():
        if not usuarios:
            print('Nenhum usuário cadastrado.\n')
        else:
            print('Usuários cadastrados:')
            for i, usuario in enumerate(usuarios, 1):
                print(f'{i}. {usuario}\n')

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

    while True:
        opcao = inquirer.select(
            message='Selecione uma opção:',
            choices=[
                'Adicionar usuário',
                'Ver usuários cadastrados',
                'Calcule sua média',
                'Sair',
            ],
        ).execute()

        if opcao == 'Adicionar usuário':
            adicionar_usuario()
        elif opcao == 'Ver usuários cadastrados':
            ver_usuarios()
        elif opcao == 'Calcule sua média':
            calculadora_media()
        elif opcao == 'Sair':
            print('Saindo do programa...')
            break

menu_interativo()