#: A população de um país A é de 80.000 habitantes, com uma taxa anual de
#crescimento de 3%. A população do país B é de 200.000 habitantes, com uma taxa de crescimento de
#1.5%. Faça um programa que calcule quantos anos serão necessários para que a população do país A
#ultrapasse ou iguale a população do país B, mantendo as taxas de crescimento.

populacao_pais_a = 80000
taxa_crescimento_pais_a = 3
populacao_pais_b = 200000
taxa_crescimento_pais_b = 1.5

def calcular_anos(pais_a, taxa_a, pais_b, taxa_b):
    anos = 0
    while pais_a <= pais_b:
        pais_a = pais_a + (pais_a * taxa_a / 100)
        pais_b = pais_b + (pais_b * taxa_b / 100)
        anos += 1
    return anos

anos_necessarios = calcular_anos(populacao_pais_a, taxa_crescimento_pais_a, populacao_pais_b, taxa_crescimento_pais_b)

print(f"Serão necessários {anos_necessarios} anos.")