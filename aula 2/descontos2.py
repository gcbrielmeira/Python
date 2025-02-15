
# Função para calcular o valor com desconto conforme as condições
def calcular_desconto(preco_original):
    # Definindo o valor do desconto de acordo com o preço
    if preco_original > 80000:
        percentual_desconto = 60
    elif preco_original > 50000:
        percentual_desconto = 30
    else:
        percentual_desconto = 0  # Sem desconto, caso o preço seja menor ou igual a 50k

    # Calculando o valor do desconto e o preço com o desconto
    desconto = (percentual_desconto / 100) * preco_original
    preco_com_desconto = preco_original - desconto
    
    return preco_com_desconto, desconto, percentual_desconto

# Entrada de dados
preco_original = float(input("Digite o preço original do produto: R$ "))

# Calculando o preço com desconto
preco_com_desconto, desconto, percentual_desconto = calcular_desconto(preco_original)

# Exibindo os resultados
if percentual_desconto > 0:
    print(f"Desconto de {percentual_desconto}% aplicado!")
else:
    print("Nenhum desconto aplicado.")

print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Preço com desconto: R$ {preco_com_desconto:.2f}")
