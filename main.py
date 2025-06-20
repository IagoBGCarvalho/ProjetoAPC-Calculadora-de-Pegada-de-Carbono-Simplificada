# Arquivo que deve ser executado
from menu_interativo import menu_interativo

if __name__ == "__main__":
    """
    Ponto de entrada principal do programa.
    Chama a função que inicia o menu interativo.
    Também serve como uma camada de segurança 
    para garantir que o programa funcione
    apenas quando o arquivo main for executado.
    """
    menu_interativo()
    