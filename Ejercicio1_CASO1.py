#Importar clases de Ejercicio 1 y hacer el caso uno con las variables globales del variables
#1:1   con PT=1  CT=4 y X=3 

import threading
import time
import random
import queue
import Ejercicio1_clases

def main():
    PT=1
    CT=4
    X=3
    cola = queue.Queue()
    productor = Ejercicio1_clases.Productor(cola)
    consumidor = Ejercicio1_clases.Consumidor(cola)
    productor.start()
    consumidor.start()
    productor.join()
    consumidor.join()

if __name__ == "__main__":
    main()







