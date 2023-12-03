from aocd import get_data

class Solution:
    def __init__(self):
        #gets input from year 2023 and day 4
        self.data = get_data(year=2023, day=3).splitlines()
        self.nothingToSeeHereCounter = 0

    #def for part1
    def part1(self):
        self.nothingToSeeHereCounter + 1


    #def for part2
    def part2(self):
        self.nothingToSeeHereCounter + 1



if __name__ == '__main__':
    #create instance of Solution class
    solution = Solution()

    print(solution.nothingToSeeHereCounter)