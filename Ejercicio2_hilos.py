import os
import multiprocessing


#LISTA DE FICHERO
def get_listaFicheros():
    directorio= os.getcwd()
    listaFicheros = os.listdir(directorio)
    listaFicheros = [f for f in listaFicheros if f.endswith('.txt')]
    return listaFicheros

#Obtener el tamaño de cada fichero de la lista de listaFicheros
def get_tamanyoFicheros(listaFicheros):
    tamanyoFicheros = []
    for f in listaFicheros:
        tamanyoFicheros.append(os.path.getsize(f))
    return tamanyoFicheros


#FUNCION VOCALES DE LA WEB
# Python program to count number of vowels,
# newlines and character in textfile
def counting(filename):
    
    # Opening the file in read mode
    txt_file = open(filename, "r")
  
    # Initialize three variables to count number of vowels,
    # lines and characters respectively
    vowel = 0
  
    # Make a vowels list so that we can
    # check whether the character is vowel or not
    vowels_list = ['a', 'e', 'i', 'o', 'u',
                   'A', 'E', 'I', 'O', 'U']
  
    # Iterate over the characters present in file
    for alpha in txt_file.read():
        
        # Checking if the current character is vowel or not
        if alpha in vowels_list:
            vowel += 1
  
    return vowel


#Numero de hilos requeridos por el usuario
def get_numHilos():
    num_hilos = int(input("Introduzca el numero de hilos: "))
    return num_hilos

#crear hilos segun get_numHilo con lock para crear el diccionario
def worker(listaFicheros, tamanyoFicheros, dic, lock):
    for i in range(len(listaFicheros)):
        dic[listaFicheros[i]] = tamanyoFicheros[i], counting(listaFicheros[i])
    lock.release()


def main():
    listaFicheros = get_listaFicheros()
    tamanyoFicheros = get_tamanyoFicheros(listaFicheros)
    num_hilos = get_numHilos()
    dic = {}
    lock = multiprocessing.Lock()
    lock.acquire()
    for i in range(num_hilos):
        p = multiprocessing.Process(target=worker, args=(listaFicheros, tamanyoFicheros, dic, lock))
        p.start()
    lock.acquire()
    print(dic)

if __name__ == "__main__":
    main()

