# Definição da Classe Pessoa 

class pessoa: 

    # Metodo Construtor
    # é chamado quando criamos um objeto
    def __init__(self, nome, idade, altura):
        # Atribuir a entidade
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def apresentar(self):
        print(f'Olá meu nome é {self.nome} e tenho')
        print(f'{self.idade} anos, e tenho')
        print(f'{self.altura} tudo isso de altura')

p1 = pessoa("Rafael", 34, "1.50")
p2 = pessoa("Guilherme", 7, "1.35")
p3 = pessoa("Alberto", 18, "1.95")


p1.apresentar()
p2.apresentar()
p3.apresentar()


