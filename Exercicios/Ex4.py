#A intenção aqui é que o input retone um valor inteiro para a variável idade por isso a conversão
idade = int (input("Informe a sua idade:"))
#Depois de estabelecer a condição colocar os dois pontos pra dizer se é verdadeiro ou falso
if idade >= 18:
    print("Acesso autorizado!")
else:
    print("Acesso negado! Por ser menor de idade.")