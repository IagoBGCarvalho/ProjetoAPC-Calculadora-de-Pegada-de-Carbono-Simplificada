# Calculadora de Pegada de Carbono Simplificada

[](https://www.google.com/search?q=https://github.com/IagoBGCarvalho/ProjetoAPC-Calculadora-de-Pegada-de-Carbono-Simplificada/releases)

## 📖 Descrição

Este projeto é uma ferramenta de console interativa, desenvolvida em Python, para estimar a pegada de carbono individual. A aplicação permite que os usuários calculem seu impacto ambiental mensal com base em hábitos de consumo em três áreas: **Energia Elétrica**, **Locomoção** e **Alimentação**.

Além do cálculo, o programa oferece **relatórios gráficos** gerados com `matplotlib` para uma visualização clara dos dados e salva o progresso dos usuários localmente. Desenvolvido no âmbito da disciplina de Algoritmos e Programação de Computadores (APC) da Universidade de Brasília (UnB), o projeto visa aplicar conceitos de programação para fomentar a conscientização ambiental.

## ✨ Funcionalidades Principais

  * **Instalação Simplificada:** Versões executáveis para Windows (`.exe`) e pacotes para Linux (`.deb`) disponíveis na seção de **Releases**, eliminando a necessidade de instalar Python ou dependências.
  * **Relatórios Gráficos:** Visualização da pegada de carbono através de gráficos de pizza, detalhando a contribuição de cada categoria para o total de emissões.
  * **Interface Interativa:** Experiência de usuário amigável no terminal, construída com a biblioteca `InquirerPy`.
  * **Gerenciamento de Usuários:** Crie, visualize, edite e remova múltiplos perfis.
  * **Persistência de Dados:** Os dados são salvos em um arquivo JSON local, mantendo o histórico dos usuários entre as sessões.
  * **Acesso à Documentação:** Uma opção "Saiba Mais" no menu principal redireciona o usuário para este repositório para total transparência sobre a metodologia.

## 🚀 Como Usar o Programa

Existem duas maneiras de usar a calculadora: através do instalador (recomendado para usuários) ou executando o código-fonte (para desenvolvedores).

### Opção 1: Para Usuários (Recomendado)

Esta é a maneira mais fácil de usar o programa, sem precisar instalar Python.

1.  Acesse a página de [**Releases**](https://www.google.com/search?q=https://github.com/IagoBGCarvalho/ProjetoAPC-Calculadora-de-Pegada-de-Carbono-Simplificada/releases) do repositório.
2.  Baixe o arquivo apropriado para o seu sistema operacional:
      * Para **Windows**: Baixe o arquivo `.exe`.
      * Para **Linux (Debian/Ubuntu)**: Baixe o arquivo `.deb`.
3.  **Para executar:**
      * **Windows:** Dê um duplo clique no arquivo `.exe` para iniciar a aplicação.
      * **Linux:** Instale o pacote com o comando `sudo dpkg -i nome_do_arquivo.deb` e depois execute o programa no terminal com o comando `pegada-carbono`.

### Opção 2: Para Desenvolvedores (Rodando do Código-Fonte)

Esta opção é para quem deseja executar o código diretamente, modificar ou contribuir.

#### Pré-requisitos

  * [Python 3.8+](https://www.python.org/downloads/)
  * [Git](https://git-scm.com/downloads/)

#### Instalação e Execução

1.  Clone o repositório:
    ```bash
    git clone https://github.com/IagoBGCarvalho/ProjetoAPC-Calculadora-de-Pegada-de-Carbono-Simplificada.git
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd ProjetoAPC-Calculadora-de-Pegada-de-Carbono-Simplificada
    ```
3.  Instale as dependências (incluindo `matplotlib`):
    ```bash
    pip install -r requirements.txt
    ```
4.  Execute o script principal `main.py`:
    ```bash
    python main.py
    ```

## 📂 Estrutura de Arquivos

O projeto é organizado de forma modular para promover a separação de responsabilidades:

  * `main.py`: **Ponto de entrada principal do programa.** Localizado na raiz do projeto, é responsável por iniciar a aplicação.
  * `calculadora_app/`: **Pasta que contém o código-fonte.** Agrupa todos os módulos que fazem a calculadora funcionar.
      * `menu_interativo.py`: Controla todo o fluxo de interação com o usuário.
      * `calculadora.py`: Contém a lógica de negócio para o cálculo da pegada de carbono.
      * `database.py`: Gerencia a leitura e escrita dos dados dos usuários.
      * `ui_components.py`: Armazena componentes visuais, como o banner ASCII e os gráficos.
  * `usuarios_pegada.json`: Arquivo que funciona como banco de dados local.

## 🧠 Saiba Mais: A Metodologia de Cálculo

A calculadora estima a pegada de carbono usando a fórmula geral:

> **Emissão (kg CO₂e) = Atividade × Fator de Emissão**

Onde "Atividade" é um dado fornecido pelo usuário (ex: km rodados) e "Fator de Emissão" é uma constante que representa a quantidade de CO₂ emitida por unidade daquela atividade. As fontes para esses fatores estão detalhadas abaixo.

## 📚 Fontes dos Fatores de Emissão

#### 1\. Energia Elétrica

  * **Fator da Rede Elétrica (0,0783 kg CO₂e / kWh):** Ministério da Ciência, Tecnologia e Inovação (MCTI), Brasil. Média do Sistema Interligado Nacional (SIN) para 2023.
  * **Potência dos Aparelhos:** Valores médios baseados em dados do PROCEL e INMETRO.
  * **Fator do Gás Natural (2,02 kg CO₂e / m³):** MCTI, Brasil. Fator padrão para o setor residencial.

#### 2\. Locomoção

  * **Fatores de Veículos:** Valores derivados de inventários da CETESB e alinhados com o Programa Brasileiro GHG Protocol para a frota e combustíveis nacionais.
  * **Fator do Metrô:** Dados baseados em relatórios da ANPTrilhos, utilizando o fator de emissão da rede elétrica brasileira (MCTI).

#### 3\. Alimentação

  * **Fatores de Alimentos:** Fonte principal baseada no estudo de Poore, J., & Nemecek, T. (2018), "Reducing food’s environmental impacts through producers and consumers", publicado na revista *Science* e referenciado por *Our World in Data*.

## 👥 Autores

Este projeto foi desenvolvido por:

  * Iago Batista Gomes de Carvalho
  * Pedro Vitor Teixeira
  * Maurício Nogueira da Silva
  * Paulo Morais de Souza Guerra