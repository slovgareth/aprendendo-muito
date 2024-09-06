#saldo  2000
#saque = float(input("Informe o Valor da grana que quer tirar: "))

#if saldo >= saque:
 #   print ("Realizando saque!")

#else: saldo
#    print("Saldo Insuficiente")

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17 and 16

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar CNH")   

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar CNH.")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer Aulas Teóticas, mas não pode fazer aulas praticas")  
else:
    print("Ainda não pode tirar a CNG")          
        

