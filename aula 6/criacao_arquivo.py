import csv
# criar e escrever um arquivo txt
# w -> Write -> Escrita
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Nome,Idade, Cidade\n")
    arquivo.write("Alberto,92,Chique-Chique/BA\n")
    arquivo.write("Arthur,28, Arrail/RJ\n")
    arquivo.write("Matheus,28,Cotia/SP\n")

    # Ler o conteudo
    # r -> Read -> Ler
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    print("COnteudo do Arquivo txt:")
    print(arquivo.read())

# Criando arqivo csv
dados = [
    [ "Nome", "idade", "Cidade"],
    [" Carlos", "32", "Santa Isabel"],
    ["Tulio", "53", "Carapikuiba"],
    ["Rafael", "18", "Serra do taboao"]
]

# Criar arquivo csv
with open("dados.csv", "w", newline="", encoding="utf-8") as csvarquivo:
    escritor = csv.writer(csvarquivo)
    escritor.writerows(dados)

# Ler o arquivo csv
with open("dados.csv", "r", encoding="utf-8") as csvarquivo:
    leitor = csv.reader(csvarquivo)
    print("\nConteudo do Arquivo CSV")
    for linha in leitor:
        print(linha)
    