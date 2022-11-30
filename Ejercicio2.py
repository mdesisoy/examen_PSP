#Get a list of files (from the current directory or from all the files in the “home” folder. 
#Process each file: Pista os.listdir():
#ejercicio 1. get size of each file 
#ejercicio 2. count how many vowels(vocales) appear in the file. 
#write (1) and (2) as values in a python dictionary using the filename as a key (1 punto)
#The script should accept the number of threads to use required as user INPUT. (2 puntos)
#Make (2) thread safe using locks (2 puntos)

import os
import threading
import time
import random
import queue
import sys

#get list of files
def get_list_files():
    current_dir = os.getcwd()
    list_files = os.listdir(current_dir)
    return list_files

#ejercicio 1. get size of each file from list_files
def get_size_file(list_files):
    size_files = []
    for file in list_files:
        size_files.append(os.path.getsize(file))
    return size_files

    #file_stats = os.stat(filename)
    #print(file_stats)
    #print(f'File Size in Bytes is {file_stats.st_size}')
    #print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')


#FUNCION VOCALES DE LA WEB
# Python program to count number of vowels,
# newlines and character in textfile
def counting(filename):
    
    # Opening the file in read mode
    txt_file = open(filename, "r")
  
    # Initialize three variables to count number of vowels,
    # lines and characters respectively
    vowel = 0
    line = 0
    character = 0
  
    # Make a vowels list so that we can
    # check whether the character is vowel or not
    vowels_list = ['a', 'e', 'i', 'o', 'u',
                   'A', 'E', 'I', 'O', 'U']
  
    # Iterate over the characters present in file
    for alpha in txt_file.read():
        
        # Checking if the current character is vowel or not
        if alpha in vowels_list:
            vowel += 1
              
        # Checking if the current character is
        # not vowel or new line character
        elif alpha not in vowels_list and alpha != "\n":
            character += 1
              
        # Checking if the current character
        # is new line character or not
        elif alpha == "\n":
            line += 1
  
    # Print the desired output on the console.
    print("Number of vowels in ", filename, " = ", vowel)
    print("New Lines in ", filename, " = ", line)
    print("Number of characters in ", filename, " = ", character)
  
  
# Calling the function counting which gives the desired output
counting('Myfile.txt')
