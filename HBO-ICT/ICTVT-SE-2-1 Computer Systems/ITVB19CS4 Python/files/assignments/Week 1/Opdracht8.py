print("Temperatuur: ")
T = input()
print("Waarde van Beaufort: ")
B = input()

if T.replace('.','',1).strip('-').isdigit() and B.replace('.','',1).strip('-').isdigit():
    temp = 13 + 0.62 * float(T) - 14 * float(B) ** 0.24 + 0.47 * float(T) * float(B) ** 0.24
    print(round(temp.real, 2), "°C")
else:
    print("een van de gegeven waardes is geen (decimaal) getal.")
