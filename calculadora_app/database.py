# O arquivo "database.py" serve para comunicar o python com o banco de dados JSON.
# Nele, estão contidas as funções que servem para ler, modificar(criar, alterar, excluir...) e salvar o arquivo JSON e os dados contidos nele. 
# O arquivo "menu_interativo.py" que estará encarregado
# de importar essas funções e utilizá-las.

import json # Módulo que permite interagir com o arquivo JSON.

NOME_ARQUIVO = 'usuarios_pegada.json' # Nome que será atribuído ao arquivo JSON.

def carregar_dados():
    """Lê o banco de dados JSON e o retorna como um dicionário, caso ele ainda não exista."""
    try:
        with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo: # o r indica "modo de leitura".
            return json.load(arquivo) # o load lê o arquivo json e o traduz para listas e dicionários em python.
    except (FileNotFoundError, json.JSONDecodeError): # Caso os erros relacionados a falta ou a corrupção do arquivo aconteçam, o programa retorna um dicionário vazio.
        return {}

def salvar_dados(dados):
    """Salva o dicionário de dados no arquivo JSON."""
    with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo: # o w indica "modo de escrita", se o arquivo não existir, ele cria ele.
        json.dump(dados, arquivo, indent=4, ensure_ascii=False) # O dump converte o dicionário python em texto JSON formatado para que seja possível salvá-lo.

def obter_nomes_usuarios():
    """Retorna uma lista com os nomes de todos os usuários cadastrados."""
    dados = carregar_dados()
    return list(dados.keys()) # Retorna apenas as chaves do dicionário, ou seja, os nomes.

def criar_novo_usuario(nome_usuario):
    """Cria um novo usuário com pegada inicial 0. Retorna True se bem-sucedido, False caso contrário."""
    # Ler:
    dados = carregar_dados()

    # Modificar:
    if nome_usuario in dados:
        return False  # Usuário já existe
    else:
        dados[nome_usuario] = 0
        # Salvar:
        salvar_dados(dados)
        return True

def editar_nome_usuario(nome_antigo, novo_nome):
    """Edita o nome de um usuário. Retorna uma string indicando o resultado."""
    dados = carregar_dados()
    if nome_antigo not in dados:
        return "nao_encontrado"
    if novo_nome in dados:
        return "ja_existe"
    
    # Copia a pegada do usuário antigo, remove-o e cria o novo com a pegada copiada
    pegada_salva = dados[nome_antigo]
    del dados[nome_antigo]
    dados[novo_nome] = pegada_salva
    salvar_dados(dados)
    return "sucesso"

def remover_usuario(nome_usuario):
    """Remove um usuário. Retorna True se bem-sucedido, False caso contrário."""
    dados = carregar_dados()
    if nome_usuario in dados:
        del dados[nome_usuario]
        salvar_dados(dados)
        return True
    else:
        return False

def atualizar_pegada(nome_usuario, valor_pegada):
    """Atualiza a pegada de carbono de um usuário."""
    dados = carregar_dados()
    dados[nome_usuario] = round(valor_pegada, 2)
    salvar_dados(dados)