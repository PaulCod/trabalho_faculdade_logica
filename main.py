# Primeiro Exercicio

# Função que vai mostrar para o usuario a menssagem
# de boas vindas
def print_boasvindas(nome, ru):
    print_linha()
    print(f"Bem vindo a loja do {nome} RU:{ru}")
    print_linha()


def print_linha():
    print("-"*60)

# Vai validar se o dado de entrada é valido ou não
# e ver se ele é um int ou um float
def validar_numero(menssagem, tipo):
    while True:
        entrada = input(menssagem)
        try:
            if tipo == "float":
                numero = float(entrada)
            elif tipo == "int":
                numero = int(entrada)
            else:
                raise ValueError("Tipo invalido")

            return numero
        except ValueError:
            print("Digite um numero valido")


print_boasvindas("Paulo Junior Lima dos Santos", 4541788)

# Função que inicia o programa
def inicio():
    # vai pegar o valor do produto
    valor_produto = validar_numero("Digite o valor unitario do produto: R$ ", "float")
    # vai pegar a quantidade do produto
    qtd_produto = validar_numero("Digite a quantidade do produto: ", "int")

    textoDesconto = "Não ouve desconto"

    # Valor total sem desconto
    total = valor_produto * qtd_produto


    if total < 2500:
        total_com_desconto = total
    elif total >= 2500 and total < 6000:
        total_com_desconto = total - (total * 0.04)
        textoDesconto = "(4% de desconto)"
    elif total >= 6000 and total < 10000:
        total_com_desconto = total - (total * 0.07)
        textoDesconto = "(7% de desconto)"
    else:
        total_com_desconto = total - (total * 0.11)
        textoDesconto = "(11% de desconto)"

    print_linha()
    print(f"O valor sem desconto foi R${total}")
    print(f"O valor com desconto foi R${total_com_desconto} {textoDesconto}")

inicio()
