from InquirerPy import inquirer

# --- CONSTANTES DE EMISSÃO (Valores médios em kg de CO₂ equivalente) ---
# Fontes: Fatores compilados a partir do Ministério da Ciência, Tecnologia e Inovação (MCTI) do Brasil (2023)
# para energia e transporte, e estudos acadêmicos internacionais (ex: Our World in Data) para alimentação.

# 1. Fatores de Energia Elétrica e Gás
FATOR_ENERGIA_BR = 0.0783      # kg CO₂e por kWh (Média do Sistema Interligado Nacional 2023)
POTENCIA_COMPUTADOR = 0.150     # kW (Desktop + Monitor)
POTENCIA_TV = 0.100             # kW (TV de LED ~40 polegadas)
POTENCIA_CHUVEIRO = 5.5         # kW
FATOR_GAS_NATURAL = 2.02        # kg CO₂e por m³
CONSUMO_GAS_BANHO = 0.2         # m³ por banho de 10 min

# 2. Fatores de Locomoção (por km)
FATOR_CARRO_GASOLINA = 0.168
FATOR_ONIBUS_URBANO = 0.088     # por passageiro.km
FATOR_METRO = 0.011             # por passageiro.km

# 3. Fatores de Alimentação (por kg ou L)
FATOR_CARNE_BOVINA = 99.48
FATOR_CARNE_SUINA = 12.31
FATOR_REFRIGERANTE = 0.59       # por Litro
FATOR_COMBO_FASTFOOD = 16.7     # Emissão média para um combo (X-Salada + Fritas)

def _obter_numero_validado(mensagem):
    """
    Pede um número ao usuário de forma segura, garantindo que a entrada seja válida.
    Retorna 0 se a entrada estiver vazia.
    """
    while True:
        valor_str = inquirer.text(message=mensagem).execute()
        if not valor_str:
            return 0.0
        
        try:
            # Substitui vírgula por ponto para aceitar ambos formatos decimais
            return float(valor_str.replace(',', '.'))
        except ValueError:
            print("❌ Entrada inválida. Por favor, digite apenas números.")


def _calcular_energia():
    """Calcula a pegada de carbono relacionada ao consumo de energia."""
    print("\n--- 💡 Categoria: Energia Elétrica ---")
    print("Por favor, informe seu consumo MENSAL para os itens abaixo.")

    horas_pc = _obter_numero_validado("Horas de uso do computador por mês:")
    horas_tv = _obter_numero_validado("Horas de uso da TV por mês:")
    minutos_chuveiro_eletrico = _obter_numero_validado("Minutos de banho em chuveiro ELÉTRICO por mês:")
    qtd_banhos_gas = _obter_numero_validado("Número de banhos em chuveiro a GÁS por mês:")

    # Cálculo do consumo em kWh
    consumo_pc = POTENCIA_COMPUTADOR * horas_pc
    consumo_tv = POTENCIA_TV * horas_tv
    consumo_chuveiro = POTENCIA_CHUVEIRO * (minutos_chuveiro_eletrico / 60) # Converte minutos para horas
    
    # Emissão da energia elétrica
    emissao_eletrica = (consumo_pc + consumo_tv + consumo_chuveiro) * FATOR_ENERGIA_BR
    
    # Emissão do gás
    consumo_gas = CONSUMO_GAS_BANHO * qtd_banhos_gas
    emissao_gas = consumo_gas * FATOR_GAS_NATURAL

    subtotal = emissao_eletrica + emissao_gas
    print(f"Subtotal de Energia: {subtotal:.2f} kg de CO₂e")
    return subtotal


def _calcular_locomocao():
    """Calcula a pegada de carbono relacionada à locomoção."""
    print("\n--- 🚗 Categoria: Locomoção ---")
    print("Por favor, informe suas distâncias percorridas por MÊS em km.")

    km_carro = _obter_numero_validado("Quilômetros rodados de carro (gasolina):")
    km_onibus = _obter_numero_validado("Quilômetros rodados de ônibus urbano:")
    km_metro = _obter_numero_validado("Quilômetros rodados de metrô/trem:")

    emissao_carro = km_carro * FATOR_CARRO_GASOLINA
    emissao_onibus = km_onibus * FATOR_ONIBUS_URBANO
    emissao_metro = km_metro * FATOR_METRO

    subtotal = emissao_carro + emissao_onibus + emissao_metro
    print(f"Subtotal de Locomoção: {subtotal:.2f} kg de CO₂e")
    return subtotal


def _calcular_alimentacao():
    """Calcula a pegada de carbono relacionada à alimentação."""
    print("\n--- 🍔 Categoria: Alimentação ---")
    print("Por favor, informe seu consumo MENSAL aproximado.")

    kg_carne_bovina = _obter_numero_validado("Kg de carne bovina consumidos por mês:")
    kg_carne_suina = _obter_numero_validado("Kg de carne suína consumidos por mês:")
    qtd_fast_food = _obter_numero_validado("Número de combos de fast-food (com carne) por mês:")
    litros_refri = _obter_numero_validado("Litros de refrigerante consumidos por mês:")

    emissao_bovina = kg_carne_bovina * FATOR_CARNE_BOVINA
    emissao_suina = kg_carne_suina * FATOR_CARNE_SUINA
    emissao_fast_food = qtd_fast_food * FATOR_COMBO_FASTFOOD
    emissao_refri = litros_refri * FATOR_REFRIGERANTE
    
    subtotal = emissao_bovina + emissao_suina + emissao_fast_food + emissao_refri
    print(f"Subtotal de Alimentação: {subtotal:.2f} kg de CO₂e")
    return subtotal


def iniciar_calculo_pegada():
    """
    Função principal que executa a lógica da calculadora de pegada de carbono.
    Chama as funções de cada categoria e soma os resultados para a pegada mensal.
    """
    print("\n=======================================================")
    print("    Iniciando Calculadora de Pegada de Carbono     ")
    print("=======================================================")
    
    # Chama as funções de cálculo para cada categoria
    pegada_energia = _calcular_energia()
    pegada_locomocao = _calcular_locomocao()
    pegada_alimentacao = _calcular_alimentacao()

    # Soma os subtotais para obter a pegada mensal
    pegada_mensal_total = pegada_energia + pegada_locomocao + pegada_alimentacao
    
    print("\n-------------------------------------------------------")
    print(f"Sua pegada de carbono MENSAL estimada é de: {pegada_mensal_total:.2f} kg de CO₂e")
    print("-------------------------------------------------------")
    
    # Retorna o valor mensal para ser salvo no banco de dados
    return pegada_mensal_total