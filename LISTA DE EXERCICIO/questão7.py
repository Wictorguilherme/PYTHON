#Faça um programa que receba o valor de uma dívida e mostre uma tabela com
#os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

valor_da_divida = float(input("Digite o valor da dívida: R$ "))
juros = float(input("Digite a taxa de juros (%): "))
quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))

def calcular_juros(valor_divida, juros):
    return valor_divida * (juros / 100)

def calcular_parcela(valor_da_divida, quantidade_parcelas):
    return valor_da_divida / quantidade_parcelas

def mostrar_tabela(valor_da_divida, juros, quantidade_parcelas):
    valor_juros = calcular_juros(valor_da_divida, juros)
    valor_parcela = calcular_parcela(valor_da_divida + valor_juros, quantidade_parcelas)

    print("Tabela de Dívida:")
    print("---------------")
    print(f"Valor da Dívida: R$ {valor_da_divida:.2f}")
    print(f"Valor dos Juros: R$ {valor_juros:.2f}")
    print(f"Quantidade de Parcelas: {quantidade_parcelas}")
    print(f"Valor da Parcela: R$ {valor_parcela:.2f}")
    print("---------------")

mostrar_tabela(valor_da_divida, juros, quantidade_parcelas)