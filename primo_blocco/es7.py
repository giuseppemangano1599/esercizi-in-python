'''Scrivere un programma che converte gradi Fahrenheit 
in gradi Celsius.'''

f = int(input("Inserisci i gradi Fahrenheit: "))

#La formula per i gradi F in gradi C è (gradi Fahrenheit - 32) * (5/9)
c = (f - 32) * (5/9)

print(f, " gradi Fahrenheit sono ", c, " gradi Celsius.")
