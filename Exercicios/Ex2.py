#input é utilzado para ler informações via teclado
#Pergunta o nome do usuário 
nome = input("Informe seu nome:")
#Pergunta a idade do usuário 
#As vezes quando o print retorna o que foi escrito ele retona como String
#Para arrumar isso podemos colocar o tipo da variável depois de declara-la 
idade = int (input("Informe sua idade:"))
#Pergunta a altura do usuário
altura = float (input("Informe a sua altura:"))
print (nome)
#Para saber o tipo do conteúdo é só colocar o type no print
print (type (idade))
print (altura)