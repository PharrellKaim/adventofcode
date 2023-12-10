import re

with open('inputDay6', 'r') as f:
    input_data = f.read().replace(' ', '')

race_duration = int(re.findall(r'\d+', input_data)[0])
record_distance = int(re.findall(r'\d+', input_data)[1])


# brute-force solution...
def part1(race_duration: int, record_distance: int) -> int:
    wins = 0
    for hold_duration in range(1, race_duration):
        speed = hold_duration
        distance = (race_duration - hold_duration) * speed
        if distance > record_distance:
            wins += 1
    return wins


part1Solution = part1(race_duration, record_distance)
part2Solution = part2(race_duration, record_distance)
print("Part 1: ")
print(part1Solution)
print("Part 2: ")
print(part2Solution)