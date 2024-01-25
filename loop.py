import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
números = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
símbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(" Bem-vindo ao gerador de senhas difíceis!!")
nr_letras = int(input("Quantas letras você quer na sua senha? \n"))
nr_simbolos = int(input("E quantos símbolos?\n"))
nr_números = int(input(" Por fim, quantos números? \n"))

lista_senhas = []

for char in range(1, nr_letras +1):
    lista_senhas.append(random.choice(letras))
    
for char in range(1, nr_simbolos +1):
    lista_senhas.append(random.choice(símbolos))    
    
for char in range(1, nr_números + 1) :
    lista_senhas.append(random.choice(números))   
    
    
#print(lista_senhas)
random.shuffle(lista_senhas)
#print(lista_senhas)


senha = " "
for char in lista_senhas:
    senha += char
    
print(f"sua senha é: {senha}")
    
    