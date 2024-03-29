# Variavel global
# Dados dos produtos oferecidos
dadosProdutos = {
    "p": {
        "tamanho": "P",
        "cp": {
            "preco": 9.00
        },
        "ac": {
            "preco": 11.00
        }
    },
    "m": {
        "tamanho": "M",
        "cp": {
            "preco": 14.00
        },
        "ac": {
            "preco": 16.00
        }
    },
    "g": {
        "tamanho": "G",
        "cp": {
            "preco": 18.00
        },
        "ac": {
            "preco": 20.00
        }
    }
}

# Função que vai mostrar o cardapio para o usuario
def cardapio():
    print(faz_linha(21) + "Cardápio" + faz_linha(21))
    print(faz_linha(6) + "| Tamanho |" + " Cupuaçu (CP) |" + " Açaí (AC) |" + faz_linha(6))

    for i in dadosProdutos:
        organiza_preco_tamanho(
            dadosProdutos[i]["tamanho"],
            dadosProdutos[i]["cp"]["preco"],
            dadosProdutos[i]["ac"]["preco"]
        )
    print(faz_linha(50))


# Função que vai organizar o print do cardapio
def organiza_preco_tamanho(tamanho, preco_cp, preco_ac):
    print(
        faz_linha(6) +
        f"|    {tamanho}    |    R${str(preco_cp) + ' ' if preco_cp <= 9 else preco_cp}    |   R${preco_ac}  |" +
        faz_linha(6)
    )


# Função simple que auxilia na criação da interface do usuario
def faz_linha(num):
    return "-"*num


# Função para pegar input com a escola do sabor
def escolha_sabor():
    while True:
        try:
            sabor = input("Escolha um sabor (CP/AC): ").lower().strip()

            if sabor not in ("ac", "cp"):
                raise ValueError("Valor invalido")
            return sabor

        except ValueError:
            print("Sabor invalido, tente novamente\n")
            continue


# Função para pegar input com a escola do tamanho
def escolha_tamanho():
    while True:
        try:
            tamanho = input("Escolha o tamanho (P/M/G): ").lower().strip()

            if tamanho not in ("p", "m", "g"):
                raise ValueError("Valor invalido")
            return tamanho

        except ValueError:
            print("Tamanho invalido, tente novamente\n")
            continue


# Função que inicia o programa
def inicio():
    acumulador = 0
    print("Bem vindo a loja de Gelados do Paulo Junior Lima dos Santos")
    # Chama a função que vai mostrar o cardapio
    cardapio()
    while True:
        # Recebe a escolha do sabor do usuario
        sabor = escolha_sabor()
        # Recebe a escolha do sabor do usuario
        tamanho = escolha_tamanho()
        # Recebe o dado de preço da escolha do usuario
        preco = dadosProdutos[tamanho][sabor]["preco"]

        acumulador += preco
        print(faz_linha(50))
        print(f"Voce pediu um {'CUPUAÇU' if sabor == 'cp' else 'AÇAI'} de tamanho {tamanho.upper()}, no valor de R${preco} ")
        mais = input("Deseja mais alguma coisa? (S - sim / qualquer outra tela): ").lower().strip()
        print(faz_linha(50))

        if mais not in "s":
            break

        continue

    print(f"O total do seu pedido deu R${acumulador}")

inicio()


