
### Section 3 : stringhe


# Escape character \ (backslash) per mantenere le "" nella frase che vogliamo stampare
print("Orazio disse \"Cogio ergo sum\"")

# Mi restituisce il numero di caratteri all'interno della mia stringa, compresa vrgola e spazi
len()


## Indexing

# ogni carattere ha associato un indice che rappresenta la posizione, partono da 0

my_string = "Python"

print(my_string[2]) # output t

## Slicing

# posso estrarrre porzioni di stringa, non solo lettere [stard:stop:step]
# start: indice iniziale, stop  indice finale, step : quanto è grande il passo che compio tra due caratteri
# l'indice finale non èe incluso, ci si ferma un passo prima

frase = "Ciao mi chiamo virginia"
print(frase[0:15]) # output "Ciao mi chiamo"

## Metodi per le stringhe
# un metodo è una specie di funzione che si applica all'oggtto con cui viene chiamato 
# sintassi oggetto.metodo()

# esempi
# .lower() tutte le lettere minuscole 
# .upper() tutte le lettere maiuscole
# .find() per trovare lettere, se non c'è restituisce -1, da sempre il primo trovato
# .index() come find ma se non trova cio che cerco mi restituisce un errore
# .rfind() mi restituisce l'ultimo indice relativo alla posizione
# .count() mi restituisce il numero di volte una sottostringa è presente
# .stratswith() mi da un booleano 
# .endswith() mi da un booleano 
# .strip() riuove gli spazi vuoti, ma se definisco cosa puo rimuovere anche sottostringhe
# .replace()

# metodi utilizzati per interpolre vatiabili/espressioni
# .fomat()
# .f-strings()



































