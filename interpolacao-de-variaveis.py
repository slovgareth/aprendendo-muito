#Old Style %

nome = "Rafael"
idade = 40
profissao = "Analista de TI"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

#Método format

print("Olá, me chamo {}. Eu tenho {} de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
print("Olá, me chamo {3}. Eu tenho {1} de idade, trabalho como {0} e estou matriculado no curso de {2}.".format(nome, idade, profissao, linguagem))

# #Método f-string

print(f"Olá, me chamo {nome}. Eu tenho {idade} de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

#formatar string com f-string

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")

print(f"Valor de PI: {PI:10.2f}")