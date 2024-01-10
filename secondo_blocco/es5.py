'''Scrivere un programma che stampi tutte le possibili triple di numeri x,y,z 
dove x varia tre 5 e 10,
y varia tra 6 e 12, 
z varia tra 7 e 13 '''

for x in range(5, 11):
    for y in range(6, 13):
        for z in range(7, 14):
            print(x, y, z)