#!/bin/bash

# --- Configurações ---
APP_NAME="pegada-carbono"
VERSION="1.0.0" # Mude a versão aqui quando fizer alterações importantes
MAINTAINER="Iago Carvalho <iagobgc@gmail.com>"
ICON_NAME="iconecpc.png" # Verifique se o seu ícone .png está na raiz com este nome
BUILD_DIR="build_deb"
DEB_NAME="${APP_NAME}_${VERSION}_all.deb"

echo "--- Limpando builds anteriores ---"
rm -rf ${BUILD_DIR}

echo "--- Criando estrutura de pastas ---"
mkdir -p ${BUILD_DIR}/DEBIAN
mkdir -p ${BUILD_DIR}/opt/${APP_NAME}
mkdir -p ${BUILD_DIR}/usr/local/bin
# --- [NOVO] Adicionando pastas para integração de desktop ---
mkdir -p ${BUILD_DIR}/usr/share/applications
mkdir -p ${BUILD_DIR}/usr/share/pixmaps

echo "--- Copiando arquivos da aplicação ---"
cp -r calculadora_app ${BUILD_DIR}/opt/${APP_NAME}/
cp main.py ${BUILD_DIR}/opt/${APP_NAME}/
cp requirements.txt ${BUILD_DIR}/opt/${APP_NAME}/
# --- [NOVO] Copiando o ícone da aplicação ---
cp ${ICON_NAME} ${BUILD_DIR}/usr/share/pixmaps/

echo "--- Criando arquivo de controle ---"
cat <<EOF > ${BUILD_DIR}/DEBIAN/control
Package: ${APP_NAME}
Version: ${VERSION}
Architecture: all
Maintainer: ${MAINTAINER}
Depends: python3, python3-pip
Description: Uma calculadora de pegada de carbono interativa.
 Este programa permite que usuários estimem sua pegada de carbono mensal
 com base em hábitos de energia, locomoção e alimentação.
EOF

echo "--- Criando script de pós-instalação ---"
cat <<EOF > ${BUILD_DIR}/DEBIAN/postinst
#!/bin/bash
echo "Instalando dependências Python via pip..."
pip3 install -r /opt/${APP_NAME}/requirements.txt
echo "Instalação de dependências concluída."
exit 0
EOF
chmod +x ${BUILD_DIR}/DEBIAN/postinst

echo "--- Criando o comando executável ---"
cat <<EOF > ${BUILD_DIR}/usr/local/bin/${APP_NAME}
#!/bin/bash
python3 /opt/${APP_NAME}/main.py
EOF
chmod +x ${BUILD_DIR}/usr/local/bin/${APP_NAME}

# --- [NOVO] Criando atalho de Desktop (.desktop) ---
echo "--- Criando atalho de Desktop (.desktop) ---"
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
echo "✅ Pacote ${DEB_NAME} criado com sucesso!"