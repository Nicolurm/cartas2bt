import random #random es un modulo
from  carta import Carta

class Baraja:
    def __init__(self):
        self.cartas =[]
        palos=["corazones", "treboles","diamantes", "picas"]
        valores=["As", "2", "3","4", "5", "6","7","8","9",
        "10","Jota", "Reina", "Rey"]

        for palo in palos:
            for valor in valores:
                self.cartas.append(Carta(palo,valor))
    
    def barajar(self):
        random.shuffle(self.cartas)
    
    def mostrarCartas(self):
        for carta in self.cartas:
            print(carta) #No podemos hacer print dentro de un objeto SOS
            
    def contar(self):
        return len(self.cartas)

    def __repr__(self):
        return f"Baraja  de {self.contar()}"

    def sacarCarta(self):
        if len(self.cartas)>0:
            return self.cartas.pop() #al poner .pop el primer elemento se "elimina"
        else:
            return None
    
    def quedanCartas(self):
        return len(self.cartas)!=0 #True si >0; False si =0/ .self se refiere para nombrar a una clase