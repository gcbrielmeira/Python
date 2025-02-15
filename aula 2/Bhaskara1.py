import math

# Função para calcular as raízes usando a fórmula de Bhaskara
def bhaskara(a, b, c):
    # Calculando o discriminante (delta)
    delta = b**2 - 4*a*c
    
    # Verificando se o delta é negativo, indicando que não há raízes reais
    if delta < 0:
        return "Não existem raízes reais"
    
    # Calculando as duas raízes
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    
    return raiz1, raiz2

# Entrada de valores para a, b e c
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Chama a função e exibe as raízes
result = bhaskara(a, b, c)
if isinstance(result, tuple):
    print(f"As raízes da equação são: {result[0]} e {result[1]}")
else:
    print(result)
