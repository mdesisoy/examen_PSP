#Implementa en python un código de Productor Consumidor mediante cola sincronizada tal que:
#-El productor produce números mayor que 10 y menor que 1000, el productor produce 10 números cada vez que los almacena en la cola y el tiempo de espera 
# entre la generación de un numero y otro es de PT segundos (1 punto)
#-El consumidor lee X números de la cola de golpe, calcula el MCD de esos X números .(1,5 punto)

#El tiempo de espera entre la lectura de X elementos cola y la siguiente lectura de los siguientes X elementos es de  CT segundos (1 punto)
#Prueba el algoritmo con los distintos casos usando una relación de productor:consumidor de     
#1:1   con PT=1  CT=4 y X=3 (0,5 puntos) CASO 1

import threading
import time
import random
import queue

#Variables globales CASO 1
PT=None
CT=None
X=None

#Funcion que calcula el MCD de una lista de n numeros
def mcd(lista):
    if len(lista)==1:
        return lista[0]
    else:
        mcd1=mcd(lista[1:])
        mcd2=lista[0]
        while mcd2!=0:
            mcd1,mcd2=mcd2,mcd1%mcd2
        return mcd1


class Productor(threading.Thread):
    def __init__(self, cola):
        threading.Thread.__init__(self)
        self.cola = cola

    def run(self):
        for i in range(10):
            numero=random.randint(10,1000)
            self.cola.put(numero)
            print("Productor produce: ",numero)
            time.sleep(PT)
        print("Productor termina")


class Consumidor(threading.Thread):
    def __init__(self, cola):
        threading.Thread.__init__(self)
        self.cola = cola

    def run (self):
        lista=[]
        for i in range(10):
            for j in range(X):
                numero=self.cola.get()
                lista.append(numero)
                print("Consumidor lee: ",numero)
            print("MCD de ",lista," es: ",mcd(lista))
            lista=[]
            time.sleep(CT)
        print("Consumidor termina") #No lo va a sacar porque el consumidor se queda esperando a que el productor le de algo

def main():
    global PT, CT, X
    PT=1
    CT=4
    X=3
    cola = queue.Queue()
    productor = Productor(cola)
    consumidor = Consumidor(cola)
    productor.start()
    consumidor.start()
    productor.join()
    consumidor.join()

if __name__ == "__main__":
    main()





