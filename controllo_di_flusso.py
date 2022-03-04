# is e == sono differenti; 
# == testa l'ugualianza in base al valore
# is testa l'uguaglianza considerando se due oggetti occupano la stessa locazione
# esempio

a = [1, 10, 100]
b = [1, 10, 100]

a == b
# True

a is b
# False, questo perchè in memoria appaiono in due locazioni diverse perche sono oggetti diversi


## if, elif, else
# IMP--> indentazione (mettere semppre 4 spazi prima dell oggetto della funzione) 
# e idue punti dopo lo statement 

if x == y == z:
    print("Equilatero")
elif x == y or x ==z or y == z:
    print("Isoscele")
else:
    print("Ottuso")

# posso usare piu di un elif

## If annidati

num = float(input("Inserisci un numero: ")

if num >= 0:
    if num == 0:
        print = ("Hai inserito 0")
    else:
        print("Numero positivo")
else:
    print("Numero positivo")    
