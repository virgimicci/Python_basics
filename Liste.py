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
  
# Metodi: append, extend e insert

