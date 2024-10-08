#: Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se
#que esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00. Faça um programa
#que determine o salário desse funcionário em 2025, sabendo que:

salario_inicial = 1000
ano_da_contratacao = 1995
ano_atual = 2025
taxa_de_aumento = 1.5

def calculo_salarial(salario_inicial, taxa_aumento, anos):
    salario_atual = salario_inicial
    for i in range(anos):
        salario_atual = salario_atual + (salario_atual * taxa_aumento / 100)
    return salario_atual

anos_trabalho = ano_atual - ano_da_contratacao

salario_atual = calculo_salarial(salario_inicial, taxa_de_aumento, anos_trabalho)

print(f"O salário em {ano_atual} é de R$ {salario_atual:.2f}")