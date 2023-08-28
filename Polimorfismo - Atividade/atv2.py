class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcularValor(self):
        return self.preco


class Produto(Item):
    def __init__(self, nome, preco, quantidade):
        super().__init__(nome, preco)
        self.quantidade = quantidade

    def calcularValor(self):
        return self.preco * self.quantidade


class Servico(Item):
    def __init__(self, nome, preco, horas):
        super().__init__(nome, preco)
        self.horas = horas

    def calcularValor(self):
        return self.preco * self.horas


itens = [Produto("Camiseta", 20.00, 3), Servico("Manutenção", 50.00, 2)]

for item in itens:
    valor_total = item.calcularValor()
    print(f"{item.nome}: Valor total = R${valor_total:.2f}")
