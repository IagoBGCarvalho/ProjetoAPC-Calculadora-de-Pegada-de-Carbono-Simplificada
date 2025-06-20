def iniciar_calculo_pegada():
    """
    Função principal que executa a lógica da calculadora de pegada de carbono.
    Pede ao usuário os dados de consumo de energia, locomoção e alimentação.
    """
    print("\n--- Iniciando Calculadora de Pegada de Carbono ---")
    
    # Por enquanto, para teste, apenas retorna um valor de exemplo.
    pegada_exemplo = 350.50
    
    print(f"Cálculo finalizado! Pegada calculada: {pegada_exemplo} kg de CO₂.")
    return pegada_exemplo