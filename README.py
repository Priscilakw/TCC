class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.compras = []

    def adicionar_compra(self, compra):
        self.compras.append(compra)

class Compra:
    def __init__(self, produto, valor):
        self.produto = produto
        self.valor = valor

def main():
    clientes = []

    while True:
        print("1. Adicionar Cliente")
        print("2. Registrar Compra")
        print("3. Mostrar Informações de Cliente")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            email = input("Email do cliente: ")
            telefone = input("Telefone do cliente: ")
            novo_cliente = Cliente(nome, email, telefone)
            clientes.append(novo_cliente)
            print("Cliente adicionado com sucesso!")

        elif opcao == "2":
            if not clientes:
                print("Não há clientes cadastrados.")
                continue

            print("Escolha um cliente:")
            for i, cliente in enumerate(clientes):
                print(f"{i+1}. {cliente.nome}")

            escolha_cliente = int(input()) - 1
            if escolha_cliente < 0 or escolha_cliente >= len(clientes):
                print("Escolha inválida.")
                continue

            produto = input("Nome do produto: ")
            valor = float(input("Valor da compra: "))
            nova_compra = Compra(produto, valor)
            clientes[escolha_cliente].adicionar_compra(nova_compra)
            print("Compra registrada com sucesso!")

        elif opcao == "3":
            if not clientes:
                print("Não há clientes cadastrados.")
                continue

            print("Escolha um cliente para mostrar as informações:")
            for i, cliente in enumerate(clientes):
                print(f"{i+1}. {cliente.nome}")

            escolha_cliente = int(input()) - 1
            if escolha_cliente < 0 or escolha_cliente >= len(clientes):
                print("Escolha inválida.")
                continue

            cliente = clientes[escolha_cliente]
            print(f"Nome: {cliente.nome}")
            print(f"Email: {cliente.email}")
            print(f"Telefone: {cliente.telefone}")
            print("Histórico de Compras:")
            for compra in cliente.compras:
                print(f"Produto: {compra.produto}, Valor: {compra.valor}")

        elif opcao == "4":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
