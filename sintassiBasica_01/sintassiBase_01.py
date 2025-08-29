# 01 Sintassi base
# - Commenti
# - Input da utente
# - Stampa su schermo
# - Indentazione
# - Assenza di punto e virgola


# --- Commenti ---
# I commenti in Python si scrivono con il simbolo "#".
# Servono per aggiungere note al codice senza influenzarne l’esecuzione.
# 
# Per commentare più righe in VS Code:
#   - Seleziona le righe
#   - Premi Ctrl + ù  (oppure Ctrl + / su tastiere diverse)


# --- Input da utente ---
# La funzione input() permette di inserire dati da tastiera.
# Tutto ciò che viene inserito viene letto come stringa (str).
nome = input("Inserisci il tuo nome: ")
print("Ciao,", nome)  # Stampa un saluto con il nome inserito


# --- Stampa su schermo ---
# La funzione print() serve per stampare messaggi o valori sul terminale.
print("Questo è un messaggio di esempio.")
numero = 10
print("Il numero è:", numero)  # Stampa: Il numero è: 10


# --- Indentazione ---
# In Python l’indentazione (spaziatura a inizio riga) è fondamentale.
# Non si usano parentesi graffe come in altri linguaggi (C, Java...).
# Ogni blocco di codice (if, for, funzioni, ecc.) deve avere un rientro coerente.
if nome == "Mario":
    print("Hai inserito Mario!")
else:
    print("Nome diverso da Mario.")


# --- Punto e virgola ---
# In Python NON è necessario (né consigliato) mettere il punto e virgola alla fine delle istruzioni.
# Esempio corretto:
x = 5
print(x)

# Anche se Python permette di usarlo, si evita per convenzione:
y = 10; print(y)  # Funziona, ma non si usa in un codice pulito
