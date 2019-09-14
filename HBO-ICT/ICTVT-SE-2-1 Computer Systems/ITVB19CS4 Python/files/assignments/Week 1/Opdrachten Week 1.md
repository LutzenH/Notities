## Python - Opdrachten Week 1

### Opgave 1: Lijsten maken

a) Maak een lijst met elementen 2, 3 en 4

`list = [2, 3, 4]`

b) maak een lijst met elementen 'red', 'green'en 'blue'

`list = ['red', 'green', 'blue']`

c) maak een lijst met elementen 3, 4 en 5 waarbij range() wordt gebruikt

`list = [*range(3, 6)]`

d) maak een lijst met elementen 'a', 'b', 'c' en 'd'

`list = ['a', 'b', 'c', 'd']`

### Opgave 2: Functies voor Lijsten

a) L.index(1)

`returned de index van de opgegeven waarde terug dus 1 want die staat op de tweede plek`

b) L.count(1)

`returned het aantal keer dat 1 voorkomt in de lijst`

c) len(L)

`returned het aantal items in de lijst`

d) max(L)

`returned de hoogste waarde in de lijst indien de lijst bestaat uit getallen. en anders een error`

```
>>> max(L)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'str' and 'int'
```

e) L.append(40)

`Voegt het getal 40 toe aan het einde van de lijst.`

f) L.insert(1, 43)

'Wijzigd de waarde op index 1 naar 43'

g) L.extend([1, 43])

`Voegt de gegeven lijst achteraan L toe.`
`[30, 1, 2, 1, 0, 'hello', 'Goodbye', 1, 43]`

h) L.remove("hello")

`Haalt de gegeven waarde uit de lijst indien die bestaat, anders geeft ie een error.`

i) L.pop()

`returned het laatste waarde in de lijst en haalt deze uit de lijst.`

j) "Goodbye" in L

`True`
`Een conditional statement die True of False teruggeeft als de gegeven waarde voorkomt in de lijst`

k) L.pop(3)

`returned de waarde op de meegegeven index en haalt hem uit de lijst.`

l) L.sort()

`sorteert de waarden in de lijst van klein naar groot indien de lijst uit sorteerbaare waardes bestaat.`

m) random.shuffle(L)

`husselt de waardes in de lijst door elkaar heen mits random is geimport anders geeft ie een error.`

### Opgave 3: List Slicing

`L = ['a', 'b', 'c', 'd', 'e']` 

a) >>> L[1:-3]

`Geeft de waardes van index 1 tot en met het einde -3`
`['b']`

b) >>> L[-4:-2]

`Geeft de waardes vanaf het einde 4 terug tot 2 terug`
`['b', 'c']`

c) >>> L[:3]

`Geeft de eerste 3 waardes`
`['a', 'b', 'c']`

d) >>> L[:2] + L[2:]

`plakt alle waardes tot 2 en alle waardes na 2 aan elkaar vast`
`['a', 'b', 'c', 'd', 'e']`

e) >>> L[:-1]

`Geeft alle waardes terug behalve de laatste`
`['a', 'b', 'c', 'd']`

f) >>> L[::-1]

`Geeft de waardes omgekeerd terug.`
`['e', 'd', 'c', 'b', 'a']`

g) >>> L[:]

`Geeft alle waardes in de lijst terug.`
`['a', 'b', 'c', 'd', 'e']`

### Opgave 4: Twee Lijsten

a) L1 + L2

`[30, 1, 2, 1, 0, 1, 21, 13]`

b) 3 * L2

`Geeft de waardes van L2 3x achterelkaar aan terug.`
`[1, 21, 13, 1, 21, 13, 1, 21, 13]`

c) L1 > L2

`Gaat de waardes van links naar rechts bij langs om te kijken of de waarde hoger in L1 is dan in L2 en returned dan True of dit waar is voor https://en.wikipedia.org/wiki/Lexicographical_order`
`True`

d) [x for x in L1]

`List alle waardes in L1?`
`[30, 1, 2, 1, 0]`

e) [x for x in L1 if x in L2]

`Returned waardes uit L1 die ook in L2 voorkomen`
`[1, 1]`

### Opgave 5: Lijsten en Strings

```
s = 'Guido van Rossum'
L = s.split(' ')

print(L)
```

### Opgave 6: Wat wordt er afgedrukt?

a)

```
L = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    L[i] = L[i -1]
    print(L)

------output------
[1, 1, 3, 4, 5, 6]
[1, 1, 1, 4, 5, 6]
[1, 1, 1, 1, 5, 6]
[1, 1, 1, 1, 1, 6]
[1, 1, 1, 1, 1, 1]
```

b) 

```
L1 = list(range(1, 10, 2))
L2 = L1
L1[0] = 'abc'
print(L1)
print(L2)

------output------
['abc', 3, 5, 7, 9]
['abc', 3, 5, 7, 9]
```

c)

```
a, b = 0, 1
while b < 10:
  print (b)
  a, b = b, a+b

-------output------
1
1
2
3
5
8
```

### Opgave 7: Palindroom

```
woord = 'lepel'
woordOmgekeerd = woord[::-1]

if woordOmgekeerd == woord:
    print(woord, "is een palindroom")
else:
    print(woord, "is GEEN palindroom")

```

### Opgave 8: Gevoelstemperatuur

```
print("Temperatuur: ")
T = input()
print("Waarde van Beaufort: ")
B = input()

if T.replace('.','',1).strip('-').isdigit() and B.replace('.','',1).strip('-').isdigit():
    temp = 13 + 0.62 * float(T) - 14 * float(B) ** 0.24 + 0.47 * float(T) * float(B) ** 0.24
    print(round(temp.real, 2), "°C")
else:
    print("een van de gegeven waardes is geen (decimaal) getal.")
```

### Opgave 9: Vind de genen

a)

```
genomeSequence = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

for i in range(0, len(genomeSequence)):
    smallSequence = genomeSequence[i:i+3]
    if(smallSequence == "ATG"):
        print(i+3)
```

b)

```
genoom = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

sequenceStarted = False
sequenceStartIndex = 0
currentGene = ""

def processGene(gene):
        if(gene != "" and len(gene) % 3 == 0):
                print(f'Gene found: {gene}')
        else:
                print('Gene not multiple of 3')

for index, char in enumerate(genoom):
        if(char == 'A' and genoom[index : index + 3] == 'ATG'):
                sequenceStartIndex = index
                sequenceStarted = True

        if(sequenceStarted == True):
                if(char == 'T' and (genoom[index : index + 3] == 'TAG'
                        or genoom[index : index + 3] == 'TAA'
                        or genoom[index : index + 3] == 'TGA')):
                        sequenceStarted = False
                        processGene(currentGene)
                        currentGene = ""
                        continue
        
                if(index > sequenceStartIndex + 2):
                        currentGene += char
```

### Opgave 10: De gemiddelde temperatuur

`python3 Opdracht10.py < station_vl.txt`

```
from sys import stdin

NUMBER_OF_DAYS = 10
NUMBER_OF_HOURS = 24

data = []

for i in range(NUMBER_OF_DAYS):
    data.append([])
    for j in range(NUMBER_OF_HOURS):
        data[i].append([])

# read input using input redirection from a file
for line in stdin:
    if line[0] == '#':
        continue
    L = line.strip().split()
    
    data[int(L[0])-1][int(L[1])-1] = int(L[2])

print("Gemiddelde temperaturen: ")

# find the average daily temperature
for i in range(NUMBER_OF_DAYS):
    avg = (sum(data[i]) / float(len(data[i]))) / 10.0
    print(round(avg, 2), "℃")

```
