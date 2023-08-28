class ContaBancaria:
    def calcular_juros(self):
        pass

class ContaPoupanca(ContaBancaria):
    def calcular_juros(self, saldo):
        return saldo * 0.05

class ContaCorrente(ContaBancaria):
    def calcular_juros(self, saldo):
        return saldo * 0.02

conta_poupanca = ContaPoupanca()
saldo_poupanca = 1000
juros_poupanca = conta_poupanca.calcular_juros(saldo_poupanca)
print(f"Juros da Conta Poupança: R${juros_poupanca:.2f}")

conta_corrente = ContaCorrente()
saldo_corrente = 1500
juros_corrente = conta_corrente.calcular_juros(saldo_corrente)
print(f"Juros da Conta Corrente: R${juros_corrente:.2f}")
