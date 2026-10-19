# A Classe: O modelo (a planta)
class celular:

    def __init__(self, marca, modelo, cor, bateria = 100):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

#Asessando, cor , bateria:int = 100):

    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False


# Os objetos Criados apartir da classe (as "casas")
celular1 = celular("Samsung", "Galaxy a23", "preto",bateria= 50)
celular2 = celular("motorola", "Motog", "azul", bateria= 30)
print(celular1.marca)
print(celular1.modelo)
print(celular1.cor)
print(celular1.bateria)
print(celular2.marca)
print(celular2.modelo)
print(celular2.cor)
print(celular2.bateria)