'''Chiedere all'utente l'ora (specificando di inserire solo l'ora)
e poi chiedere fra quante ore deve suonare la sveglia.
Il programma deve stampare che ore saranno quando la sveglia suonerà.'''

orario_corrente = int(input("Inserisci l'ora: "))

orario_attesa = int(input("Tra quante ore deve suonare la sveglia? "))

ore = orario_corrente + orario_attesa

print("La sveglia suonerà alle ", ore % 24)