# Calculadora de Pegada de Carbono Simplificada

## 📖 Descrição

Este projeto, desenvolvido no âmbito da disciplina de Algoritmos e Programação de Computadores (APC) da Universidade de Brasília (UnB), consiste em uma ferramenta de console interativa para estimar a pegada de carbono individual de um usuário. A calculadora solicita informações sobre hábitos de consumo em três categorias principais — Energia Elétrica, Locomoção e Alimentação — e, com base em fatores de emissão pré-definidos, fornece uma estimativa mensal em quilogramas de CO₂ equivalente (kg CO₂e).

O objetivo é aplicar os fundamentos de algoritmos e programação na abordagem de um problema ambiental atual, fomentando a conscientização sobre o impacto das atividades cotidianas.

## ✨ Funcionalidades

  * **Launcher Multiplataforma:** Um script de inicialização detecta o sistema operacional (Windows, macOS, Linux) e abre o programa em uma nova janela de terminal dedicada.
  * **Gerenciamento de Usuários:** Crie, visualize, edite e remova perfis de usuário.
  * **Cálculo de Pegada de Carbono:** Calcule a pegada de carbono mensal com base em inputs do usuário.
  * **Persistência de Dados:** Os usuários e suas pegadas de carbono são salvos localmente em um arquivo `JSON`, mantendo os dados entre as sessões.
  * **Interface Interativa:** Utiliza a biblioteca `InquirerPy` para criar uma experiência de uso amigável e guiada no terminal.
  * **Banner de Boas-Vindas:** Exibe uma arte ASCII na inicialização do programa.

## ⚙️ Como Rodar o Projeto

### Pré-requisitos

  * [Python 3.8+](https://www.python.org/downloads/)
  * [Git](https://git-scm.com/downloads/)

### Instalação

1.  Clone o repositório para a sua máquina local:
    ```bash
    git clone https://github.com/IagoBGCarvalho/ProjetoAPC-Calculadora-de-Pegada-de-Carbono-Simplificada.git
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd ProjetoAPC-Calculadora-de-Pegada-de-Carbono-Simplificada
    ```
3.  Instale as dependências necessárias:
    ```bash
    cd documentacao
    ```
    ```bash
    pip install -r requirements.txt
    ```

### Execução

Para iniciar o programa, execute o script `launcher.py`. Ele irá detectar seu sistema operacional e abrir a aplicação em uma nova janela de terminal:

```bash
python launcher.py
```

## 📂 Estrutura de Arquivos

O projeto é organizado de forma modular para promover a separação de responsabilidades:

  * `launcher.py`: **Ponto de entrada principal.** Script "launcher" que abre o programa em um terminal dedicado.
  * `main.py`: Script que é chamado pelo launcher para iniciar a lógica da aplicação.
  * `menu_interativo.py`: Controla todo o fluxo de interação com o usuário, exibindo menus e coordenando as ações.
  * `calculadora.py`: Contém toda a lógica de negócio para o cálculo da pegada de carbono, incluindo os fatores de emissão e as perguntas ao usuário.
  * `database.py`: Gerencia a persistência de dados, cuidando da leitura e escrita no arquivo `usuarios_pegada.json`.
  * `ui_components.py`: Armazena componentes visuais da interface, como o banner ASCII.
  * `usuarios_pegada.json`: Arquivo que funciona como banco de dados local para salvar os dados dos usuários.

## 🧠 Saiba Mais: A Metodologia de Cálculo

A calculadora estima a pegada de carbono usando a fórmula geral:

> **Emissão (kg CO₂e) = Atividade × Fator de Emissão**

Onde "Atividade" é um dado fornecido pelo usuário (ex: km rodados, kWh consumidos) e "Fator de Emissão" é uma constante que representa a quantidade de gases de efeito estufa emitida por unidade daquela atividade.

### Categoria: Energia Elétrica

Calcula as emissões pelo consumo de eletricidade e gás natural.

  * **Eletricidade:** `Potência do Aparelho (kW) × Tempo de Uso (horas) × Fator de Emissão (kg CO₂e/kWh)`
  * **Gás Natural:** `Consumo (m³) × Fator de Emissão (kg CO₂e/m³)`

### Categoria: Locomoção

Calcula as emissões com base na distância percorrida em diferentes modais de transporte.

  * **Fórmula:** `Distância (km) × Fator de Emissão (kg CO₂e/km)`

### Categoria: Alimentação

Calcula as emissões com base na quantidade de alimentos consumidos, considerando o ciclo de vida de cada produto.

  * **Fórmula:** `Quantidade (kg ou L) × Fator de Emissão (kg CO₂e por unidade)`

## 📚 Fontes dos Fatores de Emissão

#### 1\. Energia Elétrica

  * **Fator de Emissão da Rede Elétrica (0,0783 kg CO₂e / kWh):**
      * **Fonte:** Ministério da Ciência, Tecnologia e Inovação (MCTI), Brasil. Fator de emissão médio anual para o Sistema Interligado Nacional (SIN), dados de 2023.
  * **Potência Média dos Aparelhos (Computador, TV, Chuveiro):**
      * **Fonte:** Valores médios baseados em dados do Programa Nacional de Conservação de Energia Elétrica (PROCEL) e do INMETRO.
  * **Fator de Emissão do Gás Natural (2,02 kg CO₂e / m³):**
      * **Fonte:** Ministério da Ciência, Tecnologia e Inovação (MCTI), Brasil. Fator padrão para queima de gás natural no setor residencial.

#### 2\. Locomoção

  * **Fator de Emissão de Veículos (Carro, Ônibus):**
      * **Fonte:** Valores derivados de inventários de emissões veiculares (ex: CETESB) e alinhados com as diretrizes do Programa Brasileiro GHG Protocol, que adaptam fatores para a realidade da frota e dos combustíveis brasileiros.
  * **Fator de Emissão do Metrô:**
      * **Fonte:** Dados baseados em relatórios da Associação Nacional dos Transportadores de Passageiros sobre Trilhos (ANPTrilhos), utilizando o fator de emissão da rede elétrica brasileira (MCTI) para o cálculo.

#### 3\. Alimentação

  * **Fatores de Emissão de Alimentos (Carnes, Fast-Food, etc.):**
      * **Fonte Principal:** Estudo científico de Poore, J., & Nemecek, T. (2018), "Reducing food’s environmental impacts through producers and consumers", publicado na revista *Science*. Os dados são amplamente referenciados pela plataforma acadêmica *Our World in Data*.
      * **Nota:** O fator para "Fast-Food" é uma estimativa calculada com base nos ingredientes de um combo padrão (hambúrguer de carne, queijo, batatas) para representar um cenário realista.

## 👥 Autores

Este projeto foi desenvolvido por:

  * Iago Batista Gomes de Carvalho
  * Pedro Vitor Teixeira
  * Maurício Nogueira da Silva
  * Paulo Morais de Souza Guerra