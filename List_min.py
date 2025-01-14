import random
lista = []
for i in range(10):
    x = random.random()
    lista.append(x)


liczba = lista[0]
for j in range(10):
    if liczba > lista[j]:
        liczba = lista[j]
print(lista)
print("Najmniejsza liczba w liscie to:",liczba)
print("Najmniejsza wedlug pythona:",min(lista))