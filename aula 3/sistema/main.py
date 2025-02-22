from app.controllers.clienteController import clienteController


def exibir_menu():
    print("\n=== MENU ===")
    print("1 - Cadastrar cliente ")
    print("2 - Listar Clientes")
    print("3 - Cadastrar Produtos")
    print("4 - Listar produtos")
    print("0 - Sair do Sistema")

def main():
    cntrlCliente = clienteController()
    

    while True:
        exibir_menu()
        opc=input("Escolha uma opção: ")
        
        if opc == "1":
            nome=input("Nome do Cliente: ")
            email=input("E-mail: ")
            idade=int(input("idade: "))
    #salvariamos no banco de dados
            cntrlCliente.criar_cliente(nome, email, idade)
    
        elif opc =="2":
    #listar do banco de dados os clientes
            for index, cliente in enumerate(cliente, 1): 
                #index -> Posicao atual do cliente listado
                # __str__ -> cliente ->(nome-"", email-"", idade-"" )
                print(f"(index). (cliente)")
        
        elif opc=="3":
            nome= input("Nome do Produto: ")
            preco =float(input("preço: "))

        elif opc == "4":
    #listar do banco de dados os produtos
            print("listar")
        elif opc == "0": 
            break
        else:
            print("Opção invalida. Tente Novamente.")
 
 # python main.py

if __name__ == "__main__":
    main()