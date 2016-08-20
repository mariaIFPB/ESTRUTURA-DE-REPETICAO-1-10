Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>  nome = str(input("digite um nome de usuario:"))
senha = str(input("digite uma senha:"))
while(senha == nome):
	print("erro")
	nome= str(input("digite um nome de usuario:"))
	senha = str(input("digite uma senha:"))
