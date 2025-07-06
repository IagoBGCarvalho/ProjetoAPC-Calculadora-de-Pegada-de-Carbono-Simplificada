# main.py
from menu_interativo import menu_interativo
from ui_components import exibir_banner

def iniciar_programa():
    """
    Função principal que aciona todas as funcionalidades do Programa.
    """
    exibir_banner()
    menu_interativo()

# Se rodar como script direto (modo debug/local), ainda funciona
if __name__ == "__main__":
    iniciar_programa()