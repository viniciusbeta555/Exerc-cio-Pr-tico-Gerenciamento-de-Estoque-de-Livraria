livros = []
def cadastro():
    codigo = int(input("Digite o codigo do livro: "))
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    quant = int(input("Digite a quantidade de livros disponivel: "))
    if quant < 0:
        while quant < 0:
            quant = int(input("Quantidade invalida! Por favor, insira um valor valido."))

    livro = {'codigo': codigo,
             'nome': nome,
             'autor': autor,
             'quant': quant}
    livros.append(livro)

    print("Livro cadastrado com sucesso!")

def consulta():
    codigo = int(input("Informe o codigo do livro para busca: "))
    encontrado = False
    for livro in livros:
        if livro['codigo'] == codigo:
            print(f"Código: {livro['codigo']}\nNome: {livro['nome']}\nAutor: {livro['autor']}\nQuantidade: {livro['quant']}")
            encontrado = True
            break
    if not encontrado:
        print("Livro não encontrado.")

def atualizar():
    codigo = int(input("Informe o codigo do livro pata alterar sua quantidade: "))
    for i, livro in enumerate(livros):
        if livro['codigo'] == codigo:
            quantidade = int(input("Digite a nova quantidade: "))
            while quantidade < 0:
                    quantidade = int(input("Quantidade invalida! Por favor, insira um valor valido."))
            livro['quant'] = quantidade
            print("Estoque atualizado.")
        else:
            print("Livro não encontrado.")

def listar():
    if not livros:
        print("Nenhum livro cadastrado.")

    for livro in livros:
        print(f"Código: {livro['codigo']} | Nome: {livro['nome']} | Autor: {livro['autor']} | Quantidade: {livro['quant']}")

def menu():
    escolha = True
    while escolha == True:
        print("\nMenu:")
        print("1 - Cadastrar livro")
        print("2 - Consultar livro")
        print("3 - Atualizar estoque")
        print("4 - Exibir todos os livros")
        print("0 - Sair")
        numero = int(input("Escolha uma opção numerica: "))

        if numero == 1:
            cadastro()
        elif numero == 2:
            consulta()
        elif numero == 3:
            atualizar()
        elif numero == 4:
            listar()
        elif numero == 0:
            print("Ate mais!")
            escolha = False
        else:
            print("Opção invalida, tente novamente.")

menu()