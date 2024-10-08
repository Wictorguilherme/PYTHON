#Desenvolver um programa para verificar a nota do aluno em uma prova com
#10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com
#o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
#Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
#Após todos os alunos terem respondido informar:
#a. Maior e Menor Acerto;
#b. Total de Alunos que utilizaram o sistema;
#c. A Média das Notas da Turma.
#Gabarito da Prova:
#01 - A
#02 - B
#03 - C
#04 - D
#05 - E
#06 - E
#07 - D
#08 - C
#09 - B
#10 - A

gabarito = {'1':'A', '2':'B', '3':'C', '4':'D', '5':'E', '6':'E', '7':'D',
            '8':'C', '9': 'B', '10':'A'}

notas = []

sair = 'S'

while sair.upper() !='N':
    aluno = input('Digite o seu nome: ')
    respostas = []
    
    for res in range(1,11):
        resposta_da__questao = input("Digite a resposta " + str(res) + "(digite uma letra de A e E )")
        respostas.append(resposta_da__questao)
        
    posicao = 1
    acerto = 0
    for resposta in respostas:
        resposta = resposta.upper()
    
        if resposta == gabarito[str(posicao)]:
            acerto += 1
    
    notas.append([aluno, acerto])   
    
    print('Ira inserir outra nota de outro aluno? ')
    sair = input("Digite 'S' para sim e 'N' para não: ")     
    print("")      
         
quantidade_de_alunos = len(notas)

aluno_maior = ''
aluno_menor = '' 
iguais_maior = 0
iguais_menor = 0
maior = 0
menor = 10
soma = 0

for nota in notas:
    if nota[1] > maior:
        maior = nota[1]  
        aluno_maior = nota[0]
    
    if nota[1] < menor:
        menor = nota[1]
        aluno_menor = nota[0]
        
        soma += nota[1]
        
for nota in notas:
    if nota[1] == maior:
        iguais_maior += 1
    if nota[1] == menor:
        iguais_menor += 1

media = soma/quantidade_de_alunos 

print("*********************")   
print("O maior acerto foi do " + aluno_maior + " com a nota " + str(maior))   
print(str(iguais_maior) + " notas foram iguais a de " + aluno_maior + ".")   
print("O menor acerto foi do aluno " + aluno_menor + " com a nota " +str(menor) + ".")   
print(str(iguais_menor) + " notas foram iguais a de " + aluno_menor + ".")   
print(str(quantidade_de_alunos) + " alunos foram inseridos no sistema.")   
print("A média da turma é igual a " + str(media) + ".")   
print("********************")        
                          