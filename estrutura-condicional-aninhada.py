conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 1700
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print ("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque Realizado com uso do Cheque especial!")
    else:
        print("Não foi possível realizar o saque! Saldo Insuficiente")
        
elif conta_universitaria:
    if saldo >= saque:
        print("Saldo Realizado com sucesso!")
    else:
        print("Saldo Insuficiente!")  
else:
    print("Sistema não reconheceu o tipo de conta, entre em contato com seu gerente")                     

