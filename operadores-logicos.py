saldo = 1000
saque = 200
limite = 100

#operador and e or

print (saldo >= saque and saque <= limite)
print (saldo >= saque or saque <= limite)

#operadro de negacao

contatos_emergencia = []

print(not 1000 > 1500)
print(not contatos_emergencia)
print(not "saque 1500;")
print(not "")

#parenteses

print (saldo >= saque and saque <= limite) and (saldo >= saque or saque <= limite) or (saldo >= saque or saque <= limite)
print (saldo >= saque and saque <= limite) and saldo >= saque or saque <= limite or (saldo >= saque or saque <= limite)
print (saldo >= saque and saque <= limite) and saldo >= saque or saque <= limite or (saldo >= saque or saque <= limite)
print (saldo >= saque and saque <= limite) and saldo >= saque or saque <= limite or saldo >= saque or saque <= limite