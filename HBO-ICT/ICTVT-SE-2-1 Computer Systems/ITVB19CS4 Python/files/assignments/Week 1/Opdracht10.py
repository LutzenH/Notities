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
