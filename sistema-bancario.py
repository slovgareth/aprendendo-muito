class SistemaBancario:
    def __init__(self):
        self.saldo = 0.0
        self.movimentacoes = []
        self.saques_diarios = 0
        self.limite_saques_diarios = 3
        self.limite_saque = 500.0

    def formatar_moeda(self, valor):
        return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

    def depositar(self, valor):
        if valor <= 0:
            print("Erro: O valor do depósito deve ser positivo.")
            return
        
        self.saldo += valor
        self.movimentacoes.append(f"Depósito: {self.formatar_moeda(valor)}")
        print(f"Depósito realizado com sucesso: {self.formatar_moeda(valor)}")

    def sacar(self, valor):
        if self.saques_diarios >= self.limite_saques_diarios:
            print("Erro: Limite diário de saques atingido.")
            return

        if valor > self.saldo:
            print("Erro: Saldo insuficiente para saque.")
            return

        if valor > self.limite_saque:
            print(f"Erro: O valor máximo para saque é {self.formatar_moeda(self.limite_saque)}.")
            return

        self.saldo -= valor
        self.saques_diarios += 1
        self.movimentacoes.append(f"Saque: {self.formatar_moeda(valor)}")
        print(f"Saque realizado com sucesso: {self.formatar_moeda(valor)}")

    def extrato(self):
        if not self.movimentacoes:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for movimento in self.movimentacoes:
                print(movimento)
        print(f"Saldo atual: {self.formatar_moeda(self.saldo)}")

def main():
    banco = SistemaBancario()

    while True:
        print("\nMenu:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            try:
                valor = float(input("Digite o valor do depósito: ").strip())
                banco.depositar(valor)
            except ValueError:
                print("Erro: Valor inválido. Digite um número.")
        
        elif opcao == "2":
            try:
                valor = float(input("Digite o valor do saque: ").strip())
                banco.sacar(valor)
            except ValueError:
                print("Erro: Valor inválido. Digite um número.")
        
        elif opcao == "3":
            banco.extrato()
        
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        
        else:
            print("Erro: Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
