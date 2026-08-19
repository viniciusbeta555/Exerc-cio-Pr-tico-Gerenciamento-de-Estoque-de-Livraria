#  Sistema de Gerenciamento de Acervo de Livros

## Sobre o projeto

Este projeto consiste em um **sistema simples de gerenciamento de acervo de livros**, desenvolvido em Python e executado diretamente pelo terminal.

O programa permite cadastrar livros, consultar informações, atualizar a quantidade disponível em estoque e listar todos os livros cadastrados. Cada livro possui um código único, nome, autor e quantidade disponível.

O sistema utiliza conceitos fundamentais da linguagem Python, como:

* Funções;
* Listas;
* Dicionários;
* Estruturas condicionais (`if`, `elif` e `else`);
* Laços de repetição (`while` e `for`);
* Validação de dados;
* Entrada e saída de informações.

---

## Como o sistema funciona

O programa utiliza uma lista chamada `acervo` para armazenar todos os livros cadastrados:

```python
acervo = []
```

Cada livro é armazenado dentro dessa lista como um dicionário contendo as seguintes informações:

* `codigo`: código de identificação do livro;
* `nome`: nome do livro;
* `autor`: nome do autor;
* `quant`: quantidade disponível.

Um exemplo de livro armazenado seria:

```python
{
    'codigo': 1,
    'nome': 'Dom Casmurro',
    'autor': 'Machado de Assis',
    'quant': 5
}
```

---

## Validação da quantidade

A função `valor_valido()` é responsável por solicitar e validar a quantidade de livros disponível.

```python
def valor_valido():
    quant = int(input("Digite a quantidade de livros disponível:\n"))
    
    while quant < 0:
        quant = int(input("Quantidade inválida! Por favor, insira um valor válido:\n"))
        
    return quant
```

O programa não permite que a quantidade seja negativa. Caso o usuário informe um número menor que zero, será solicitado um novo valor até que uma quantidade válida seja digitada.

---

## Cadastro de livros

A função `cadastrar()` permite adicionar um novo livro ao acervo.

Durante o cadastro, o sistema solicita:

1. Código do livro;
2. Nome;
3. Nome do autor;
4. Quantidade disponível.

### Código único

Antes de cadastrar um livro, o programa verifica se já existe outro livro utilizando o mesmo código.

```python
for livro in acervo:
    if livro['codigo'] == codigo:
```

Caso o código já exista, o usuário deve informar outro código. Isso garante que cada livro possua uma identificação única dentro do sistema.

Após a validação, os dados são organizados em um dicionário:

```python
livro = {
    'codigo': codigo,
    'nome': nome,
    'autor': autor,
    'quant': quant
}
```

Em seguida, o livro é adicionado à lista `acervo`:

```python
acervo.append(livro)
```

---

## Consulta de livros

A função `consultar()` permite buscar um livro através do seu código.

O usuário informa o código desejado e o programa percorre o acervo utilizando um laço `for`.

Se o livro for encontrado, suas informações são exibidas:

```text
Código: 1
Nome: Dom Casmurro
Autor: Machado de Assis
Quantidade: 5
```

Caso nenhum livro possua o código informado, o sistema exibe a mensagem:

```text
Livro não encontrado.
```

---

## Atualização do estoque

A função `atualizar()` permite alterar a quantidade disponível de um livro.

O usuário informa o código do livro e o sistema realiza uma busca no acervo. Caso o livro seja encontrado, uma nova quantidade é solicitada utilizando a função `valor_valido()`.

```python
livro['quant'] = valor_valido()
```

Assim, a quantidade armazenada anteriormente é substituída pelo novo valor informado.

Caso o código não seja encontrado, o sistema informa que o livro não existe no acervo.

---

## Listagem de livros

A função `listar()` exibe todos os livros cadastrados.

Primeiramente, o programa verifica se a lista `acervo` está vazia:

```python
if not acervo:
    print("Nenhum livro cadastrado.")
```

Caso existam livros cadastrados, o sistema percorre a lista e exibe as informações de cada um:

```text
Código: 1 | Nome: Dom Casmurro | Autor: Machado de Assis | Quantidade: 5
Código: 2 | Nome: O Hobbit | Autor: J.R.R. Tolkien | Quantidade: 3
```

---

## Menu principal

A função `menu()` controla a interação principal com o usuário.

Ao iniciar o programa, as seguintes opções são apresentadas:

```text
Menu:

1 - Cadastrar livro
2 - Consultar livro
3 - Atualizar estoque
4 - Exibir todos os livros
0 - Sair
```

De acordo com a opção escolhida, o programa chama a função correspondente.

| Opção | Funcionalidade                     |
| ----- | ---------------------------------- |
| `1`   | Cadastrar um novo livro            |
| `2`   | Consultar um livro pelo código     |
| `3`   | Atualizar a quantidade em estoque  |
| `4`   | Exibir todos os livros cadastrados |
| `0`   | Encerrar o programa                |

O menu permanece em execução dentro de um laço `while` até que o usuário escolha a opção `0`.

---

## Como executar o projeto

1. Certifique-se de ter o **Python** instalado no computador.
2. Salve o código em um arquivo com extensão `.py`, por exemplo:

```text
acervo.py
```

3. Abra o terminal na pasta onde o arquivo foi salvo.
4. Execute o seguinte comando:

```bash
python acervo.py
```

5. Utilize as opções do menu para gerenciar o acervo de livros.

---

## 🧪 Exemplo de utilização

Um possível fluxo de uso seria:

```text
Menu:
1 - Cadastrar livro
2 - Consultar livro
3 - Atualizar estoque
4 - Exibir todos os livros
0 - Sair

Escolha uma opção numérica:
1

Digite o código do livro:
101

Digite o nome do livro:
O Hobbit

Digite o nome do autor:
J.R.R. Tolkien

Digite a quantidade de livros disponível:
5

Livro cadastrado com sucesso!
```

Depois disso, o livro ficará armazenado no acervo e poderá ser consultado, atualizado ou exibido junto aos demais livros cadastrados.

---

## Possíveis melhorias

Algumas melhorias que podem ser adicionadas futuramente ao sistema incluem:

* Validação para impedir a inserção de letras em campos numéricos;
* Opção para remover livros do acervo;
* Alteração do nome ou autor de um livro;
* Busca por nome ou autor;
* Organização dos livros em ordem alfabética;
* Salvamento dos dados em arquivos;
* Utilização de banco de dados;
* Criação de uma interface gráfica ou aplicação web.

---


## Objetivo

O objetivo do projeto é aplicar conceitos fundamentais de programação em Python por meio da criação de um sistema de gerenciamento de livros.

A aplicação demonstra, na prática, como utilizar **listas e dicionários para armazenar dados**, além de **funções, estruturas condicionais, laços de repetição e validação de informações** para construir um sistema interativo executado pelo terminal.
