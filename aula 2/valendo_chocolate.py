
# Verificar se uma palavra é um polidromo
# caso seja, exiba "não é um palindromo"
# A verificação deve ser case Sensitive

#valendo = barra de chocolate

def eh_palindromo(texto):
    # Remove espaços e converte para minúsculas
    texto = texto.replace(" ", "").lower()
    # Verifica se o texto é igual ao seu reverso
    return texto == texto[::-1]

# Exemplo de uso
palavra = input("digite a sua palavra:")
if eh_palindromo(palavra):
    print(f'"{palavra}" é um palíndromo!')
else:
    print(f'"{palavra}" não é um palíndromo.')
