# Arquivo que deve ser executado!!!
import os
import platform

#O script que deve ser executado no Laucher
script = 'main.py'

#Verifica o sistema operacional
sistema = platform.system()
print(f"Detectado sistema {sistema}. Abrindo o programa em uma nova janela...")

if sistema == 'Windows':
    os.system(f'start cmd /k python {script}')

elif sistema == 'Linux':
    # Comando para terminais baseados em GNOME (Ubuntu, Fedora, etc.)
    os.system(f'gnome-terminal -- bash -c "python3 {script}; exec bash"')

elif sistema == 'Darwin': #macOs
    os.system(f'osascript -e \'tell app "Terminal" to do script "python3 {script}"\'')
else:
    print(f'Sistema operacional não suportado')
    print('Tentando executar diretamente neste terminal...')
    os.system(f'python3 {script_a_ser_executado}')