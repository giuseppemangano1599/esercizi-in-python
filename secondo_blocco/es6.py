'''Scrivere un programma che stampi tutte le possibili coppie di numeri x, y 
con x e y tra 0 e 10, 
dove x è pari e y è dispari.'''

#x numero pari
for x in range (0, 11, 2):
    
    #y numero dispari
    for y in range (1, 11, 2):
        print(x, y)