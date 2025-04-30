acervo = []

def valor_valido():
    quant = int(input("Digite a quantidade de livros disponível:\n"))
    while quant < 0:
        quant = int(input("Quantidade inválida! Por favor, insira um valor válido:\n"))
    return quant 
     
def cadastrar():
    while True:
        codigo = int(input("Digite o código do livro:\n"))
        codigo_existe = False
        
        for livro in acervo:
            if livro['codigo'] == codigo:
                print("Já existe um livro cadastrado com este código. Verifique e digite novamente:\n")
                codigo_existe = True
                break
        if not codigo_existe:
            break

    nome = input("Digite o nome do livro:\n")
    autor = input("Digite o nome do autor:\n")
    quant = valor_valido()
    

    livro = {'codigo': codigo,
             'nome': nome,
             'autor': autor,
             'quant': quant}
             
    acervo.append(livro)

    print("Livro cadastrado com sucesso!")

def consultar():
    codigo = int(input("Informe o código do livro para busca:\n"))
    encontrado = False
    for livro in acervo:
        if livro['codigo'] == codigo:
            print(f"Código: {livro['codigo']}\nNome: {livro['nome']}\nAutor: {livro['autor']}\nQuantidade: {livro['quant']}")
            encontrado = True
            break
    if not encontrado:
        print("Livro não encontrado.")

def atualizar():
    codigo = int(input("Informe o código do livro para alterar sua quantidade:\n"))
    encontrado = False
    
    for livro in acervo:
        if livro['codigo'] == codigo:
            livro['quant'] = valor_valido()
            print("Valor atualizado no estoque.")
            encontrado = True
            break
    if not encontrado:
        print("Livro não encontrado.")

def listar():
    if not acervo:
        print("Nenhum livro cadastrado.")

    for livro in acervo:
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
        
        numero = int(input("Escolha uma opção numérica:\n"))

        if numero == 1:
            cadastrar()
        elif numero == 2:
            consultar()
        elif numero == 3:
            atualizar()
        elif numero == 4:
            listar()
        elif numero == 0:
            print("Até mais!")
            escolha = False
        else:
            print("Opção inválida, tente novamente. \n")

menu()
