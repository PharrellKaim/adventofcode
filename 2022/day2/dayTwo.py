list = []
count = int(0)

with open('./day2/testSource.txt', 'r') as file:
        lines = file.readlines()
        list.append(lines)   

print(list)

def matching(list, count):
    for lines in list:
        if str == 'A Y\n' or str == 'A Y':
            count + 8
        elif str == 'A X\n' or str == 'A X':
            count + 4
        elif str == 'A Z\n' or str == 'A Z':
            count + 3
        elif str == 'B X\n' or str == 'B X':
            count + 2
        elif str == 'B Y\n' or str == 'B Y':
            count + 5
        elif str == 'B Z\n' or str == 'B Z':
            count + 9
        elif str == 'C X\n' or str == 'C X':
            count + 7
        elif str == 'C Y\n' or str == 'C Y':
            count + 2
        elif str == 'C Z\n' or str == 'C Z':
            count + 6
    return count

matching(list, count)
print(count)