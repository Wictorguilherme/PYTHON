#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída 
# deve ser conforme o exemplo abaixo

def gerar_tabuada(numero):
    print("tabuada do {numero}")
    for i in range (1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero = int(input("Digite um número de 1 a 10 para gerar a tabuada:"))        
gerar_tabuada(numero)        
    