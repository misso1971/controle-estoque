# Controle de Estoque Básico
# Autor: Edmilson
# Objetivo: Demonstrar lógica simples em Python para área de logística

# Dicionário representando o estoque inicial
estoque = {
    "Caixa": 10,
    "Palete": 5,
    "Notebook": 3
}

def mostrar_estoque():
    print("\n=== Estoque Atual ===")
    for item, quantidade in estoque.items():
        print(f"{item}: {quantidade} unidades")

def adicionar_item(item, quantidade):
    if item in estoque:
        estoque[item] += quantidade
    else:
        estoque[item] = quantidade
    print(f"\nAdicionado {quantidade} unidades de {item}.")

def retirar_item(item, quantidade):
    if item in estoque and estoque[item] >= quantidade:
        estoque[item] -= quantidade
        print(f"\nRetirado {quantidade} unidades de {item}.")
    else:
        print(f"\nNão foi possível retirar {quantidade} unidades de {item}.")

# Exemplo de uso
mostrar_estoque()
adicionar_item("Caixa", 5)
retirar_item("Notebook", 2)
mostrar_estoque()

