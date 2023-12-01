import re
def extract_numbers_from_string(s):
    return [int(i) for i in s if i.isdigit()]


file = open("inputDay1", "r")
summe = int(0)
zahl = str()

for line in file:
    numbers = extract_numbers_from_string(line)
    print(numbers)
    for i in numbers:
        zahl += str(i)
        print(zahl)
    summe += int(zahl)

print(summe)