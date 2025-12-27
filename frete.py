# Calculadora Básica de Frete
# Autor: Edmilson
# Objetivo: Demonstrar lógica simples em Python aplicada à logística

def calcular_frete(distancia_km, peso_kg, modal="rodoviario"):
    """
    Calcula o custo de frete com base em distância, peso e modal.
    Valores fictícios para estudo.
    """
    # Tabelas de tarifas (valores de exemplo)
    tarifa_base = {
        "rodoviario": 50,
        "aereo": 150,
        "maritimo": 100
    }
    custo_por_km = {
        "rodoviario": 0.8,
        "aereo": 2.5,
        "maritimo": 0.5
    }
    custo_por_kg = {
        "rodoviario": 0.4,
        "aereo": 1.2,
        "maritimo": 0.3
    }

    if modal not in tarifa_base:
        raise ValueError("Modal inválido. Use: rodoviario, aereo ou maritimo.")

    # Cálculo do frete
    base = tarifa_base[modal]
    custo_distancia = custo_por_km[modal] * distancia_km
    custo_peso = custo_por_kg[modal] * peso_kg
    total = base + custo_distancia + custo_peso

    return round(total, 2)

# Exemplo de uso
print("=== Calculadora de Frete ===")
print("Rodoviário:", calcular_frete(350, 12, "rodoviario"))
print("Aéreo:", calcular_frete(350, 12, "aereo"))
print("Marítimo:", calcular_frete(350, 12, "maritimo"))
