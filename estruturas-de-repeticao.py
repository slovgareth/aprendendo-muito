 #receba um numero do teclado e exiba os 2 numeros seguintes

#a = int(input("Informe um número inteiro: "))
#print(a)


#a += 1
#print(a)

#a += 1
#print(a)


#Exmplo usando iterável
texto = input("Informe um texto: ")

VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print()
    print("Executa no final do Laço")
    print()
#exemplo usando range
for numero in range(0,11):
    print(numero, end=" ")

print()    

for numero in range(0, 100, 3):
    print(numero, end= " ")   


#usando comando While

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando ... ")
    elif opcao == 2:
        print("Exibindo o extrato ... ")    

