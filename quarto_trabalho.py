
# Variaveis globais
# Dicionário contendo as opções do menu principal
opcoes_principal = {
    "1": {
        "menssagem": "Cadastrar Livro",
    },
    "2": {
        "menssagem": "Consultar Livro(s)"
    },
    "3": {
        "menssagem": "Remover Livro"
    },
    "4": {
        "menssagem": "Sair"
    }
}

# Dicionário contendo as opções do menu de consulta
opcoes_consulta = {
    "1": {
        "menssagem": "Consultar Todos os Livros"
    },
    "2": {
        "menssagem": "Consultar Livros Por ID"
    },
    "3": {
        "menssagem": "Consultar Livro(s) Por Autor"
    },
    "4": {
        "menssagem": "Retornar"
    }
}

# Lista para armazenar os livros cadastrados
lista_livro = []




# Funções utilitarias
# Função simple que auxilia na criação da interface de usuario criando as linhas
def faz_linha(num_caractere, caractere):
    return str(caractere) * num_caractere


# Função que pega o input do usuario no cadastro do livro
def dados_input(texto, mensagemErro):
    while True:
        try:
            dado = input(texto)
            if len(dado) < 1:
                raise ValueError("dado vazio")
            return dado.strip().title()
        except ValueError:
            print(f"{mensagemErro} precisa ter ao menos 1 caractere")


# Função para acrecentar no id a cada novo cadastro
def acrecenta_id(id_global):
    return id_global + 1


# Função que cria o cabeçalho de todos os menus, como o MENU PRINCIPAL, MENU DE CONSULTA e MENU REMOVER LIVRO
def cria_header(mensagem, num_caractere):
    print(faz_linha(num_caractere, "-") + mensagem + faz_linha(num_caractere, "-"))


# Função que mostra as opções disponíveis para o usuário
def mostra_opcoes(opcoes):
    for i in opcoes:
        print(f"{i} - {opcoes[i]['menssagem']}")


# Função que pega input do usuario tanto no MENU PRINCIPAL quanto no MENU DE CONSULTA
def pega_opcoes(opcoes, mensagem, num_caractere):
    while True:
        try:
            mostra_opcoes(opcoes)
            escolha_usuario = input("Escolha a opção desejada: ")

            if escolha_usuario not in opcoes:
                raise ValueError("Opção invalida")
            return escolha_usuario
        except ValueError:
            print(faz_linha(45, "-"))
            print("Opção Invalida, Tente Novamente")
            cria_header(mensagem, num_caractere)




# Funções relacionadas ao cadastro de novo livro
# Função para cadastrar livros
def cadastra_livro(id_global):
    while True:
        cria_header("MENU DE CADASTRO DE LIVRO", 14)
        print(f"O id do livro {id_global}")
        autor = dados_input("Digite o nome do autor: ", "Autor")
        nome_livro = dados_input("Digite o nome do livro: ", "Nome do livro")
        editora = dados_input("Digite o nome da editora: ", "Editora")

        lista_livro.append({
            "id": id_global,
            "autor": autor,
            "nome_livro": nome_livro,
            "editora": editora
        })

        print(faz_linha(30, "-"))
        print("Livro cadastrado com sucesso!!!")
        break




# Funções relacionadas a consulta
# Função para exibir o MENU DE CONSULTA para o usuario
def consulta_livro():
    while True:
        cria_header("MENU DE CONSULTA", 19)
        escolha_consulta = pega_opcoes(opcoes_consulta, "MENU DE CONSULTA", 19)

        if escolha_consulta == "1":
            if lista_livro == []:
                print(faz_linha(25, "-"))
                print("Nenhum livro cadastrado")
                continue

            for livro in lista_livro:
                # print(faz_linha(25, "-"))
                mostrar_livro(livro)

            continue
        elif escolha_consulta == "2":
            print(faz_linha(25, "-"))
            livro = consulta_por_id("Digite o id do livro: ")
            if livro is None:
                print(faz_linha(25, "-"))
                print("Livro não existe")
            else:
                mostrar_livro(livro)

            continue
        elif escolha_consulta == "3":
            livros = consulta_por_autor()
            if livros is None:
                print(faz_linha(25, "-"))
                print("Nenhum livro com esse autor encontrado")
                continue

            for livro in livros:
                mostrar_livro(livro)

            continue
        elif escolha_consulta == "4":
            print("Retornando...")
            break


# Função para consultar livros por ID
def consulta_por_id(texto):
    while True:
        try:
            id = int(input(texto))
            for livro in lista_livro:
                if livro["id"] == id:
                    return livro

            return None

        except ValueError:
            print("O ID precisa ser um numero inteiro")


# Função para consultar livros por autor
def consulta_por_autor():
    livros_autor = []
    autor = input("Digite o nome do autor: ").strip().title()
    for livro in lista_livro:
        if livro["autor"] == autor:
            livros_autor.append(livro)

    if livros_autor == []:
        return None

    return livros_autor


# Função para exibir os dados de um livro
def mostrar_livro(livro):
    print(faz_linha(25, "-"))
    print(f"ID: {livro['id']}")
    print(f"Autor: {livro['autor']}")
    print(f"Livro: {livro['nome_livro']}")
    print(f"Editora: {livro['editora']}")




# Funções relacionadas a remoção de livros
# Função para remover livro de acordo com o id
def remover_livro():
    try:
        cria_header("MENU REMOVER LIVRO", 20)
        livro = consulta_por_id("Digite o id do livro que deseja excluir: ")
        if livro is None:
            print(faz_linha(25, "-"))
            print("Livro não existe!!")
            return

        lista_livro.remove(livro)
        print("Livro removido com sucesso!!!")

    except ValueError:
        print("O id deve ser um inteiro!!!")



# Função Principal
# Função que inicia o programa
def inicio():
    id_global = 0
    print("Bem vindo ao controle de livros do Paulo Junior Lima dos Santos  RU: 4541788")

    while True:
        cria_header("MENU PRINCIPAL", 20)
        escolha_principal = pega_opcoes(opcoes_principal, "MENU PRINCIPAL", 20)

        if escolha_principal == "1":
            cadastra_livro(id_global)
            id_global = acrecenta_id(id_global)
        elif escolha_principal == "2":
            consulta_livro()
        elif escolha_principal == "3":
            remover_livro()
        elif escolha_principal == "4":
            print("Encerrando o programa...")
            break


inicio()



