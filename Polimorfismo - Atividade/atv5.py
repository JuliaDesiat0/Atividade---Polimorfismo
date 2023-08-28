class TransportePublico:
    def pegar_passageiro(self):
        pass

    def largar_passageiro(self):
        pass

class Onibus(TransportePublico):
    def pegar_passageiro(self):
        print("Ônibus: Passageiro embarcando.")

    def largar_passageiro(self):
        print("Ônibus: Passageiro desembarcando.")

class Metro(TransportePublico):
    def pegar_passageiro(self):
        print("Metrô: Passageiro entrando na estação.")

    def largar_passageiro(self):
        print("Metrô: Passageiro saindo na próxima estação.")

onibus = Onibus()
onibus.pegar_passageiro()
onibus.largar_passageiro()

metro = Metro()
metro.pegar_passageiro()
metro.largar_passageiro()
