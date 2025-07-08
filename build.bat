@echo off
title Gerador de Executável - Calculadora de Pegada de Carbono

echo 🔄 Limpando arquivos antigos...
rmdir /s /q build
rmdir /s /q dist
del pegada-carbono_1.0.1.spec

echo 🚧 Gerando novo executável...
pyinstaller --onefile --name pegada-carbono_1.0.1 --icon=iconecpc.ico main.py

echo.
echo ✅ Executável gerado com sucesso! Verifique a pasta dist/
pause