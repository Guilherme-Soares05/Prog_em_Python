salario = float (input("Informe o salário: "))

if salario <= 3000:
    print("Com base no seu salário você é programador junior")
#Caso eu queira colocar mais de uma condição eu posso usar o elif
#Caso eu precise estabelecer mais de um parâmetro aí eu utilizo o and     
elif salario > 3000 and salario <= 6000:
    print("Com base no seu salário você é programador pleno")
elif salario > 6000 and salario <= 15000:
    print("Com base no seu salário você é programador senior")
#O else tá funcionando no caso de não ser nenhuma das alternativas    
else:
    print("Com base no seu salário você é gerente de projetos")             