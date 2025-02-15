# calculadora de IMC

"""
Solicite o peso em kg e altura do usuario em metros 
Caucule o IMC ( Indice de Massa Corporal )
peso / (altura = altura) 

exibir IMC
"""
n1 = float(input("digite o seu peso"))
n2 = float(input("digite a sua altura"))
IMC = n1/(n2*n2)
print("o seu IMC é: ", IMC)

if IMC < 18.5 : 
    print("seu IMC é magreza")
elif IMC > 18.5 and IMC < 24.9 : 
    print("seu IMC é Normal")

