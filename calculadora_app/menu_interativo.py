from InquirerPy import inquirer
import webbrowser
import calculadora_app.database as database
import calculadora_app.calculadora as calculadora

def menu_interativo():
    """
    Executa o sistema de gerenciamento de usuários e calculadora de pegada de carbono.
    Esta função coordena as chamadas para os módulos de database e calculadora.
    """

    def adicionar_usuario():
        nome = inquirer.text(message='Digite o nome do novo usuário:').execute()
        if database.criar_novo_usuario(nome):
            print(f'\n✅ Usuário "{nome}" adicionado com sucesso!\n')
        else:
            print(f'\n❌ Erro: Usuário "{nome}" já existe.\n')

    def ver_usuarios():
        usuarios = database.carregar_dados()
        if not usuarios:
            print('\nNenhum usuário cadastrado.\n')
        else:
            print('\n--- Usuários Cadastrados ---')
            for nome, pegada in usuarios.items():
                print(f'- {nome}: {pegada:.2f} kg de CO₂')
            print('--------------------------\n')

    def iniciar_calculadora_para_usuario():
        nomes_usuarios = database.obter_nomes_usuarios()
        if not nomes_usuarios:
            print('\n❌ Nenhum usuário cadastrado. Crie um usuário antes de calcular.\n')
            return

        usuario_selecionado = inquirer.select(
            message='Para qual usuário deseja calcular a pegada?',
            choices=nomes_usuarios,
        ).execute()

        # Chama a função do arquivo da calculadora
        nova_pegada = calculadora.iniciar_calculo_pegada()
        
        # Atualiza o valor no banco de dados
        database.atualizar_pegada(usuario_selecionado, nova_pegada)
        print(f'✅ Pegada de carbono do usuário "{usuario_selecionado}" atualizada com sucesso!\n')


    def editar_usuario():
        nomes_usuarios = database.obter_nomes_usuarios()
        if not nomes_usuarios:
            print('\n❌ Nenhum usuário cadastrado.\n')
            return
        
        nome_antigo = inquirer.select(
            message='Escolha o usuário para editar:',
            choices=nomes_usuarios,
        ).execute()

        novo_nome = inquirer.text(message=f'Digite o novo nome para "{nome_antigo}":').execute()
        
        resultado = database.editar_nome_usuario(nome_antigo, novo_nome)

        if resultado == "sucesso":
            print(f'\n✅ Nome alterado de "{nome_antigo}" para "{novo_nome}" com sucesso!\n')
        elif resultado == "ja_existe":
            print(f'\n❌ Erro: O nome "{novo_nome}" já está em uso.\n')
        else: # "nao_encontrado"
             print(f'\n❌ Erro: Usuário "{nome_antigo}" não encontrado.\n')


    def remover_usuario():
        nomes_usuarios = database.obter_nomes_usuarios()
        if not nomes_usuarios:
            print('\n❌ Nenhum usuário cadastrado.\n')
            return
        
        nome_escolhido = inquirer.select(
            message='Escolha o usuário para remover:',
            choices=nomes_usuarios,
        ).execute()

        if database.remover_usuario(nome_escolhido):
            print(f'\n✅ Usuário "{nome_escolhido}" removido com sucesso.\n')
        else:
            print(f'\n❌ Erro: Usuário "{nome_escolhido}" não encontrado.\n')

    def saiba_mais():
        """
        Função que funciona como um hyperlink que leva o usuário até a documentação do projeto.
        """
        url = "https://github.com/IagoBGCarvalho/ProjetoAPC-Calculadora-de-Pegada-de-Carbono-Simplificada/tree/main/documentacao"
        print('Abrindo a documentação do projeto no navegador...')
        webbrowser.open(url)


    while True:
        # Opções que serão mostradas para o usuário ao iniciar o programa
        opcao = inquirer.select(
            message='Selecione uma opção:',
            choices=[
                'Adicionar novo usuário',
                'Calcular Pegada de Carbono',
                'Ver usuários',
                'Editar nome de um usuário',
                'Remover usuário',
                'Saiba mais',
                'Sair',
            ],
        ).execute()

        # Condicionais que acionarão cada função de acordo com a escolha do usuário
        if opcao == 'Ver usuários':
            ver_usuarios()
        elif opcao == 'Adicionar novo usuário':
            adicionar_usuario()
        elif opcao == 'Editar nome de um usuário':
            editar_usuario()
        elif opcao == 'Remover usuário':
            remover_usuario()
        elif opcao == 'Calcular Pegada de Carbono':
            iniciar_calculadora_para_usuario()
        elif opcao == 'Saiba mais':
            saiba_mais()
        elif opcao == 'Sair':
            print('Saindo do programa...')
            break

# Esta linha permite que o programa execute diretamente pelo arquivo menu_interativo.py
if __name__ == "__main__":
    menu_interativo()