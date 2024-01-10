'''La formula per il calcolo del saldo finale se qualcuno 
sta guadagnando interessi è data da Wikipedia come segue.

A = P (1 + r/n)**nt

Scrivere un programma Python che assegna il saldo iniziale 10000 a una variabile P, 
assegna a n il valore 12 e assegna a r l'interesse del 8% (0.08). 
Chiedere all'utente il numero di anni, t. 
Calcolare e stampare l'ammontare finale dopo t anni.'''

P = 10000
n = 12
r = 0.08

t = int(input("Inserisci gli anni: "))

A = P*(1 + (r/n))**(n*t)

print(A)

