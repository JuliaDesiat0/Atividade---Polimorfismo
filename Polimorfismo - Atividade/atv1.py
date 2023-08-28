class AnimalAquatico:
    def nadando(self):
        pass
class Peixe(AnimalAquatico):
    def nadando(self):
        return "O peixe está nadando."

class Tartaruga(AnimalAquatico):
    def nadando(self):
        return "A tartaruga está nadando devagar."

animais_aquaticos = [Peixe(), Tartaruga()]

for animal in animais_aquaticos:
    print(animal.nadando())
