from src.controller import produto_controller

def exibir_menu():
     print("\n=== MENU ===")
     print("1 - Cadastrar Produto")
     print("2 - Listar Produto")
     print( "3 - Atualizar Produto")
     print("4 - Deletar Produto")
     print("0 - sair")

def listar_produtos():
     print("\n--- Lista de Produtos ---")
     produtos = produto_controller.listar_produtos()
     if produtos:
          for produto in produtos:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, preco {produto['preco']}")
     else:
        print("nao existe produtos cadastrado")

def cadastrar_produto():
     print("\n--- Cadastrar produto ---") 
     nome = input("digite o nome: ")
     preco = input("digite o preco:")
     novo_id = produto_controller.Cadastrar_produtos(nome, preco)
     print(f"produto cadastrado co sucesso com novo ID{novo_id}")



def opcao_atualizar():
     print("\nATUALIZAR O PRODUTO")
     produto_id = input("Digite o ID do produto")
     nome = input("Digite o nome do produto")
     preco = input(" Digite o preco do produto")

     linhas = produto_controller.atualizar_produto(produto_id, nome, preco)
     if linhas > 0: # quantidade de linhas modificadas
          print(" produto atualizado com sucesso! ")
     else:
          print("Nenhum produto foi atualizado")

     #main -> inicializa o projeto

def main():
     print("passou aqui")

     #while true para repetir o mesmo que a opção digitada esteja errada
     while True: 
          exibir_menu()
          opc = input("escolha uma opção: ")
               
          if  opc == "1":
               cadastrar_produto()
          elif opc == "2":
               listar_produtos()
          elif opc == "3":
               opcao_atualizar()
          elif opc == "0":
               print("saindo do sistema...")
               #sys.exist(0)
          else:
               print("opção invalida, tente novamente...")


main()
