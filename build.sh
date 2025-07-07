#!/bin/bash

# --- Configurações ---
APP_NAME="pegada-carbono"
VERSION="1.0.1" # Nova versão para refletir a correção
MAINTAINER="Iago Carvalho <iagobgc@gmail.com>"
ICON_NAME="iconecpc.png"
BUILD_DIR="build_deb"
DEB_NAME="${APP_NAME}_${VERSION}_all.deb"

echo "--- Limpando builds anteriores ---"
rm -rf ${BUILD_DIR}

echo "--- Criando estrutura de pastas ---"
# A estrutura de pastas permanece a mesma
mkdir -p ${BUILD_DIR}/DEBIAN
mkdir -p ${BUILD_DIR}/opt/${APP_NAME}
mkdir -p ${BUILD_DIR}/usr/local/bin
mkdir -p ${BUILD_DIR}/usr/share/applications
mkdir -p ${BUILD_DIR}/usr/share/pixmaps

echo "--- Copiando arquivos da aplicação ---"
# A cópia de arquivos permanece a mesma
cp -r calculadora_app ${BUILD_DIR}/opt/${APP_NAME}/
cp main.py ${BUILD_DIR}/opt/${APP_NAME}/
cp requirements.txt ${BUILD_DIR}/opt/${APP_NAME}/
cp ${ICON_NAME} ${BUILD_DIR}/usr/share/pixmaps/

echo "--- Criando arquivo de controle ---"
# Adicionamos 'python3-venv' como uma dependência de sistema
cat <<EOF > ${BUILD_DIR}/DEBIAN/control
Package: ${APP_NAME}
Version: ${VERSION}
Architecture: all
Maintainer: ${MAINTAINER}
Depends: python3, python3-venv
Description: Uma calculadora de pegada de carbono interativa.
 Este programa permite que usuários estimem sua pegada de carbono mensal
 com base em hábitos de energia, locomoção e alimentação.
EOF

# --- [ALTERAÇÃO CRUCIAL 1] ---
echo "--- Criando script de pós-instalação com ambiente virtual ---"
cat <<EOF > ${BUILD_DIR}/DEBIAN/postinst
#!/bin/bash
APP_DIR="/opt/${APP_NAME}"

echo "Criando ambiente virtual em \${APP_DIR}/venv..."
python3 -m venv \${APP_DIR}/venv

echo "Instalando dependências Python dentro do ambiente virtual..."
\${APP_DIR}/venv/bin/pip install -r \${APP_DIR}/requirements.txt

echo "Instalação de dependências concluída."
exit 0
EOF
chmod +x ${BUILD_DIR}/DEBIAN/postinst

# --- [ALTERAÇÃO CRUCIAL 2] ---
echo "--- Criando o comando executável que usa o ambiente virtual ---"
cat <<EOF > ${BUILD_DIR}/usr/local/bin/${APP_NAME}
#!/bin/bash
# Executa o main.py usando o interpretador Python do ambiente virtual
/opt/${APP_NAME}/venv/bin/python3 /opt/${APP_NAME}/main.py
EOF
chmod +x ${BUILD_DIR}/usr/local/bin/${APP_NAME}

echo "--- Criando atalho de Desktop (.desktop) ---"
# O arquivo .desktop não precisa de alterações
cat <<EOF > ${BUILD_DIR}/usr/share/applications/${APP_NAME}.desktop
[Desktop Entry]
Version=1.0
Name=Calculadora de Pegada de Carbono
Comment=Calcule sua pegada de carbono mensal
Exec=${APP_NAME}
Icon=/usr/share/pixmaps/${ICON_NAME}
Terminal=true
Type=Application
Categories=Utility;Education;
EOF

echo "--- Construindo o pacote .deb ---"
dpkg-deb --build ${BUILD_DIR}

echo "--- Renomeando o pacote final ---"
mv ${BUILD_DIR}.deb ${DEB_NAME}

echo "--- Limpando pasta de build ---"
rm -rf ${BUILD_DIR}

echo ""
echo "✅ Pacote ${DEB_NAME} criado com sucesso! (Compatível com ambientes protegidos)"