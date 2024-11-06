from baraja import Baraja
from mano import Mano

mibaraja = Baraja()
mibaraja.barajar()

mimano = Mano()
if mibaraja.quedanCartas(): #.quedanCartas() ==True
    micarta = mibaraja.sacarCarta()
    mimano.añadirCarta(micarta)

    mimano.añadirCarta(mibaraja.sacarCarta())

mimano.mostrarMano()
