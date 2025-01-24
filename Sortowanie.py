"""utworzenie tablicy z losowymi elementami - liczbami od 0 do 99 typu int

funkcja która posortuje nam tablicę i zwróci ją jako wynik
 
do zwracanaia użyjemy return
 
funkcja do porónania wników i sprawdzenia czy wynik jest prawidłowy - porównanie dwóch list ze sobą
 
funkcja - wypisanie dwóch tablic jedna pod drugą
 
funkcja main - w któej będą wywoływane wszystkie poprzednie funkcje
"""

import math
import random
random.seed(1)


def sortowanie(tab):
    return tab


def losowanie_tablicy(n,minnum,maxnum):
    #n- liczba elementow
    tab = []
    return tab


def porownanie(tab,tab2):
    Czyrowne = False
    return Czyrowne


def wypisanie_tablic(tab,tab2):
    pass


def main():
    los = losowanie_tablicy(n = 20,minnum = 0,maxnum = 99)
    posortowana = sortowanie(tab = los)
    wypisanie_tablic(tab = los,tab2 = posortowana)
    Czy_rowne = porownanie(tab = los,tab2 = posortowana)
    print(Czy_rowne)