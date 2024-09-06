# def exibir_mensagem():
#     print("Olá Mundo!")
    
# def exibir_mensagem_2(nome):
#     print(f"Seja Bem vindo {nome}!")    
    
# def exibir_mensagem_3(nome="Anônimo"):
#     print(f"Seja bem vindo {nome}!") 
    
# exibir_mensagem()
# exibir_mensagem_2(nome="Rafael")
# exibir_mensagem_3()
# exibir_mensagem_3(nome="Chappie")  

#####################################################

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero +1
    
    return antecessor, sucessor

def func_3():
    print("Olá Mundo")
    return None

print(calcular_total([10, 20, 34])) #64
print(retorna_antecessor_e_sucessor(10)) #(9, 11)

print(func_3()) #nome

    
    