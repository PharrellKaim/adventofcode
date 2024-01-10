list = []

file = open('./source/1test.txt', 'r')
lines = str(file.readline())

elfs = lines.split('\\n\\n')
file.close()


rank = []

for(elf) in elfs:    
    cals = elf.split('\\n')
    totalCal = int(0)
    for(cal) in cals:
    
        print(cal)
        totalCal = totalCal + str(cal)
    rank.append(totalCal)

rank.sort()
print(rank)

