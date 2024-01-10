'''Scrivere un programma che calcola l'area del cerchio. 
Chiedere all'utente il raggio e stampare la risposta.'''

#chiedo di inserire il raggio
r = int(input("Inserisci il raggio: "))

#L'area del cerchio è Pi(3,14) * r**2
A = 3.14 * (r**2)

print("L'area del cerchio è ", A)