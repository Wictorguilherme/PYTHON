#: Faça um programa que peça um número inteiro e determine se ele é ou não
#um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

def verificar_primo(num):
    flag = True
    
    for i in range(2, int(num/2)+1):
        if ((num % i) == 0):
            flag = False
    return flag            

numero = int(input("Digite um número inteiro: "))
if(verificar_primo(numero)):
    print("O número informado é um número primo.")
else:
    print("O número informado não é um número primo.")    
    

                
