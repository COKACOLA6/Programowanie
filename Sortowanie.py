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


def babelkowe(tab):
    n = len(tab) 
    for i in range(n):
        for j in range(n - 1):
            if tab[j] < tab[j+1]:
                continue
            else:
                temp = tab[j+1]
                tab[j+1] = tab[j]
                tab[j] = temp
    return tab



def sortowanie(tab):
    return sorted(tab)


def losowanie_tablicy(n,minnum,maxnum):
    #n- liczba elementow
    rozpietosc = maxnum - minnum
    tab = []
    i = 0
    while i < n:
        tab.append(round(random.random()*rozpietosc)+minnum)
        i+=1
    return tab


def porownanie(tab,tab2):
    if tab == tab2:
        Czyrowne = True
    else:
        Czyrowne = False
    return Czyrowne


def wypisanie_tablic(tab,tab2):
    print("tablica1:",tab)
    print("tablica2:",tab2)


def main():
    los = losowanie_tablicy(n = 20,minnum = 35,maxnum = 70)
    posortowana = sortowanie(tab = los)
    wypisanie_tablic(tab = los,tab2 = posortowana)
    #Sprawdzamy czy wyjściowa tablica jest posortowana
    Czy_rowne = porownanie(tab = sorted(los),tab2 = posortowana)
    print("Sprawdzamy czy nasza funkcja posortowała w prawidłowy sposób")
    print(Czy_rowne)
main()