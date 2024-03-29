# Variaveis globais
# Dicionário contendo as opções do menu principal
todos_servicos = {
    "DIG": {
        "tipo": "Digitalização",
        "preco": 1.10
    },
    "ICO": {
        "tipo": "Impressão Colorida",
        "preco": 1.00
    },
    "IBO": {
        "tipo": "Impressão Preto e Branco",
        "preco": 0.40
    },
    "FOT": {
        "tipo": "Fotocópia",
        "preco": 0.20
    }
}
servicos_extra = {
    "1": {
        "tipo": "Encardenação simples",
        "preco": 15.00
    },
    "2": {
        "tipo": "Encardenação capa dura",
        "preco": 40.00
    },
    "0": {
        "tipo": "Não querer mais nada",
        "preco": 0
    },
}

# Função que itera sobre as bibliotecas com informações de serviços
def mostra_servico(servicos):
    for i in servicos:
        print(f"{i} - {servicos[i]['tipo']}")


# Função que pega a escolha do servico do usuario
def escolha_servico():
    while True:
        try:
            mostra_servico(todos_servicos)
            servico = input("Escolha qual tipo de servico deseja: ").upper().strip()

            if servico not in todos_servicos:
                raise ValueError("Opção invalida")

            return todos_servicos[servico]
        except ValueError:
            print("Servico invalido, tente novamente")
            continue


# Função que ira pegar o numero de paginas e ira retornar o numero de paginas com o descoto
def num_pagina():
    while True:
        try:
            num_pagina = int(input("Digite o numero de paginas: "))

            if num_pagina >= 20 and num_pagina < 200:
                num_pagina_desconto = num_pagina - (num_pagina * 0.15)
            elif num_pagina >= 200 and num_pagina < 2000:
                num_pagina_desconto = num_pagina - (num_pagina * 0.2)
            elif num_pagina >= 2000 and num_pagina < 20000:
                num_pagina_desconto = num_pagina - (num_pagina * 0.25)
            elif num_pagina >= 20000:
                raise Exception("Excedeu numero de paginas")

            return num_pagina_desconto
        except ValueError:
            print("Numero de paginas invalido. Tente novamente")
        except Exception:
            print("Não aceitamos mais do que 20000 paginas. Tente novamente")



# Função que pergunta ao usuario se ele deseja serviço extra
def servico_extra():
    while True:
        try:
            print("Deseja algum servico extra?")
            mostra_servico(servicos_extra)
            extra = input("Escolha uma opção: ")

            if extra not in ("1", "2", "0"):
                raise ValueError("Opção invalida")

            return servicos_extra[extra]
        except ValueError:
            print("Opção invalida, Tente novamente")


# Função simple que auxilia na criação da interface de usuario criando as linhas
def faz_linha(num):
    print('-'*num)

# Função que inicia o programa
def inicio():

    print("Bem vindo a papelaria do Paulo Junior Lima dos Santos  RU:4541788")

    while True:
        try:
            servico = escolha_servico()
            paginas = num_pagina()
            extra = servico_extra()

            total_com_desconto = (paginas * servico["preco"]) + extra["preco"]

            print(f"Preço do servico: {servico['preco']} + Paginas com desconto: {paginas} + Servico extra: {extra['preco']}")
            print(f"Total: {total_com_desconto}")

            break
        except ValueError:
            print("Ocorreu um erro,  tente novamente")


inicio()


