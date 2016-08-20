nome = input("forneça o nome: ") 
while (len(nome) < 3): 
	print ("Nome inválido") 
	nome = input("forneça o nome: ") 
idade = eval(input("forneça a idade: ")) 
while (idade < 0 or idade > 150): 
	print ("Idade inválida") 
	idade = input("forneça a idade: ") 
salario = eval(input("forneça o salario: "))
while (salario < 0): 
	print ("Salário inválido") 
	salario = input("forneça o salario: ") 
sexo = input("forneça o sexo: ")
while (sexo != "f" and sexo != "m"): 
	print ("Sexo inválido") 
	sexo = input("forneça o sexo: ") 
ecivil = input("forneça o estado civil: ") 
while (ecivil != "s" and ecivil != "c" and ecivil != "v" and ecivil != "d"):
	print ("Estado civil inválido") 
	ecivil = input("forneça o estado civil: ")
