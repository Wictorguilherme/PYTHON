#Faça um programa que peça 10 números inteiros, calcule e mostre a
#quantidade de números pares e a quantidade de números ímpares.

def quantidade():
    impares=0 
    pares=0
    for n in range(10):
        numero= int(input("Digite no total 10 numeros: "))
        
        if numero % 2 == 0:
            pares +=1
        else:
            impares += 1

    print(f"Quantidade de números ímpares: {impares}")
    print(f"Quantidade de números pares: {pares}")
quantidade()