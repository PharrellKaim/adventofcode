from aocd import get_data
from functools import reduce

class Solution:
    def __init__(self):
        self.data = get_data(year=2023, day=2).splitlines() #gets the aocd input from sessionId via package

    def splitData(self):
        dataDict = {}
        for line in self.data:
            gameId = line.split(': ') #splits the game id
            numberId = gameId[0].split(' ')[1] #extracts the number frome de GameId Game100 -> 100
            dataDict[numberId] = []
            for game in gameId[1].split('; '):
                gameDict = {}
                for cubes in game.split(', '):
                    cubeValue = cubes.split(' ')
                    gameDict[cubeValue[1]] = cubeValue[0]
                dataDict[numberId].append(gameDict)
        return dataDict

    def part1(self, getData):
        valueOfPossibleGames = 0
        searchedBag = {'red': 12, 'green': 13, 'blue': 14} #the bag we are searching for
        for game in getData.keys():
            possible = True
            for pulls in getData[game]:
                for color in pulls.keys():
                    if int(pulls[color]) > int(searchedBag[color]): #bag impossible
                        possible = False
                        print('Game: ' + game + ' is not possible')
                        break
            if possible:
                valueOfPossibleGames += int(game)
                print('Game: ' + game + ' is possible')
        return valueOfPossibleGames

    def part2(self, getData):
        totalValue = 0
        for game in getData.keys():
            highestValue = {'red': '0', 'green': '0', 'blue': '0'}
            for pulls in getData[game]:
                for color in pulls.keys():
                    if int(highestValue[color]) < int(pulls[color]):
                        highestValue[color] = pulls[color]
            product = reduce(lambda x, y: x * y, [int(highestValue[color]) for color in
                                                  highestValue.keys()])  # Use the reduce function to multiply the values of all colors in the highest_value dict
            print(f"Game {game} has a minimum power of {product}")
            totalValue += product

        return totalValue


if __name__ == '__main__':
    solution = Solution()
    answer1 = solution.part1(solution.splitData())
    answer2 = solution.part2(solution.splitData())

    print("Answers:")
    print(f"The answer of part one = {answer1}")
    print(f"The answer of part two = {answer2}")