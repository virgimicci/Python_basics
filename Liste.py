# Indexing e Negative indexing
# estrarre elementi (ad ogni elemento è associato un indice)

# Recap: si parte da 0 con il primo elemento, posso esstrarre l'ultimo elemento con il neg index -1


# Slicing con le liste, sintassi [start:stop:step] dove start indice iniziale (compreso), stop il finale che non è incluso
# lo step di defoult è sempre uguale a 1 

lista = ["Andrea", "Luca", "Michele", "Roberto"]

print(lista[2:4]) #lista dall elemento 2 al 3
print(lista[::2]) # sarebbe tutta la lista con sep 2

### Funzione built-in di Py dir() per conoscere attributi e metodi di un oggetto ###
# Attributi: danno info su un oggetto, non lo modificano
# Metodi: modificano/fanno azioni su di essi

print(dir(lista)) # Questa lista contiene tutti gli attributi e metodiche possiamo utilizzare suldata type liste
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', 
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
# '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
  
# Metodi: append, extend e insert -> aggiungono elementi

lista.append("Marco")
print(lista)
# ['Andrea', 'Luca', 'Michele', 'Roberto', 'Marco'] Modifica la lista gia esistente
# posso aggiungere solo un elemento alla volta

lista.extend(["Marco", "Luigi"]) # mi permette di aggiungere piu di un elemento

lista.insert(0, "Marco") # mi permette di aggiungere elementi in una posizione qualsiasi
# devo inserirte unindice per identificare la posizione

# Metodi: clear, pop, remove -> rimuovono elementi

lista.clear() # elimina tutti gli elementi

lista.pop() # di defoult elimina l'ultimo elemento
lista.pop(1) # definendo l'indice posso scegliere quale elemento eliminare
# elimina solo un elemento alla volta

lista.remove("Luigi") # elimina solo un elemento alla volta

# Keywork del, metodoalternativo per eliminare elementi in base all0indice
del lista[0]
# rispetto a .pop posso eliminare piu di un elementoalla volta

del lista[0:2]

# Metodi: index e count
lista.index("Michele") # trova l'indice dell'elemento Michele

lista.index("Michele") # mi dice quante volte è presente Michele nella lista 

# Metodi: reverse, sort e sorted

lista.reverse() # inverte l'ordine della lista 

lista.sort() # ordina gli elementi, di defoult ascendente 
lista.sort(reverse= True) # li ordina in maniera discendente

# la funzione sorted crea una nuova lista e non modifica in plance

lista = [22, 3, 67, 4]
lista_ordinata = sorted(lista)

print(lista)
# [22, 3, 67, 4]
print(lista_ordinata)
# [3, 4, 22, 67]

# Metodo copy -> crea una copia superficiale della nostra lista








