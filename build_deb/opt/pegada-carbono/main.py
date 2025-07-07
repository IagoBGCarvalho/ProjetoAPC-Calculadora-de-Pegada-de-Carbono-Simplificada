# Arquivo que deve ser executado !!!
from calculadora_app.menu_interativo import menu_interativo
from calculadora_app.ui_components import exibir_banner

if __name__ == "__main__":
    """
    Ponto de entrada principal do programa.
    """
    exibir_banner()
    menu_interativo()