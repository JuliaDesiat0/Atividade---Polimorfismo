class Calculo:
    def calcular(self, *args):
        pass

class Soma(Calculo):
    def calcular(self, *args):
        return sum(args)

class Multiplicacao(Calculo):
    def calcular(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

# Exemplo de uso
soma_calculo = Soma()
resultado_soma = soma_calculo.calcular(5, 10, 15)
print(f"Soma: {resultado_soma}")

multiplicacao_calculo = Multiplicacao()
resultado_multiplicacao = multiplicacao_calculo.calcular(2, 3, 4)
print(f"Multiplicação: {resultado_multiplicacao}")
