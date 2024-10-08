

maximo_itens = 50
preco_unitario = 1.99



def gerar_tabela(max_itens, preco_unitario):
    tabela_preco = {}
    for i in range(1, max_itens + 1):
        tabela_preco[i] = preco_unitario * i
    return tabela_preco

def imprimir_tabela_preco(tabela_preco):
    print("Loja - Tabela de preços")
    for itens, preco in tabela_preco.items():
        print(f"{itens} - R$ {preco:.2f}")

def calcular_conta(tabela_preco, quantidade_itens):
    if quantidade_itens in tabela_preco:
        return tabela_preco[quantidade_itens]
    else:
        return "Quantidade de itens não encontrada na tabela"


tabela_preco = gerar_tabela(maximo_itens, preco_unitario)


imprimir_tabela_preco(tabela_preco)


quantidade_itens = int(input("Digite a quantidade de itens: "))
preco_conta = calcular_conta(tabela_preco, quantidade_itens)
print(f"Valor da conta: R$ {preco_conta:.2f}")