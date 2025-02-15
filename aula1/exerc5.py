
# Numeros Pares em um intervalo

"""
Solicite dois numeros inteiros ao usuario
representando o inicio e o fim de um intervalo
mostre todos os numeros pares nesse intervalo
(incluindo limite inicial) e final, se forem pares)
"""

print("Me fale um numero")
n1 = int( input())

print("me fale o segundo numero")
n2 = int(input())

print("digite o numero pares no intervalo de ", n1, "a", n2 , ":")


for num in range(n1, n2 + 1):
    if num % 2 == 0:
        print(num)    

