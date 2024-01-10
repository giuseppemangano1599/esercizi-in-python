'''Scrivere un programma che converte gradi Celsius 
in gradi Fahrenheit.'''

c = int(input("Inserisci i gradi Celsius: "))

#La formula per i gradi C in gradi F è (gradi Celcius) * (9/5) + (32)
f = c * (9 / 5) + 32

print(c, " gradi Celsius sono ", f, " gradi Farenheit.")
