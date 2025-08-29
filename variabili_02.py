# 02 Variabili
# - Cos'è e come si usa una variabile
# - Nomenclatura
# - Assegnare multipli valori a variabili

# Una variabile è un contenitore per memorizzare dati.
# In Python, non è necessario dichiarare il tipo di variabile.
# Basta assegnare un valore a una variabile usando l'operatore "=".

# Assegnazione di valori a variabili
x = 5        # Assegna il valore intero 5 alla variabile x
y = "Ciao"   # Assegna la stringa "Ciao" alla variabile y
z = 3.14     # Assegna il valore decimale 3.14 (float) alla variabile z

print(x)  # Stampa 5
print(y)  # Stampa Ciao
print(z)  # Stampa 3.14


# --- Nomenclatura delle variabili ---
# - Deve iniziare con una lettera (a-z, A-Z) o un underscore (_)
# - Può contenere lettere, numeri (0-9) e underscore (_)
# - Non può essere una parola riservata di Python (if, else, while, for, def, return, import, ecc.)
# - È case-sensitive (nome, Nome e NOME sono variabili diverse)
# - Si consiglia di usare nomi significativi e in minuscolo,
#   separando le parole con underscore (es. nome_utente)

# Esempi validi:
nome = "Mario"
eta_utente = 20
_numero = 100

# Esempio non valido:
# 2nome = "Paolo"  # Errore: non può iniziare con un numero


# --- Assegnare multipli valori a variabili ---
a, b, c = 1, 2, 3   # Assegna 1 a a, 2 a b e 3 a c
print(a, b, c)      # Stampa: 1 2 3

# Puoi anche assegnare lo stesso valore a più variabili:
d = e = f = 0
print(d, e, f)  # Stampa: 0 0 0

# È possibile "spacchettare" (unpacking) una lista in più variabili:
citta = ["Roma", "Milano", "Napoli"]
x, y, z = citta
print(x)  # Stampa: Roma
print(y)  # Stampa: Milano
print(z)  # Stampa: Napoli

print("Lista città:", citta)  # Stampa: Lista città: ['Roma', 'Milano', 'Napoli']

# Attenzione: il numero di variabili deve corrispondere al numero di valori!
# a, b = citta   # Errore -> ValueError: troppi valori da assegnare
