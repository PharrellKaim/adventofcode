from aocd import get_data

class Solution:
    def __init__(self):
        #gets input from year 2023 and day 3
        self.data = get_data(year=2023, day=3).splitlines()
        self.outputPart1 = 0
        self. outputPart2 = 0

    #check def for the Part one solution
    def horizontalCheck(self, line, numRange):
        if numRange[0] > 0:
            if line[numRange[0]-1] != '.':
                return True
        if numRange[1] < len(line):
            if line[numRange[1]] != '.':
                return True
        for char in line[numRange[0]:numRange[1]]:
            if (not char.isdigit() and char != '.'):
                return True
        return False

    #part 1
    def part1(self):
        find = []
        for idxLine, line in enumerate(self.data):
            idxNum = 0
            while idxNum < len(line):
                num = line[idxNum]
                currentNumber = ''
                if num.isdigit():
                    pointer = idxNum + 1
                    currentNumber += num
                    while pointer < len(line) and line[pointer].isdigit():
                        currentNumber += line[pointer]
                        pointer += 1
                    if currentNumber:
                        numRange = [idxNum, idxNum + len(currentNumber)]
                        valid = []
                        left_right = self.horizontalCheck(line, numRange)
                        valid.append(left_right)
                        if idxLine > 0:
                            checkUp = self.horizontalCheck(self.data[idxLine - 1], numRange)
                            valid.append(checkUp)
                        if idxLine < len(self.data) - 1:
                            checkDown = self.horizontalCheck(self.data[idxLine + 1], numRange)
                            valid.append(checkDown)
                        if True in valid:
                            find.append(int(currentNumber))
                            self.outputPart1 += int(currentNumber)
                    idxNum += len(currentNumber)
                else:
                    idxNum += 1

        return self.outputPart1

    def check(self,line, idx):
        output = []
        left_pointer = idx - 1
        right_pointer = idx + 1

        if not line[idx].isdigit():
            curr_num = ''
            while left_pointer >= 0 and line[left_pointer].isdigit():
                curr_num = line[left_pointer] + curr_num
                left_pointer -= 1
            if curr_num:
                output.append(int(curr_num))

            curr_num = ''
            while right_pointer < len(line) and line[right_pointer].isdigit():
                curr_num += line[right_pointer]
                right_pointer += 1
            if curr_num:
                output.append(int(curr_num))
        else:
            curr_num = line[idx]
            while left_pointer >= 0 and line[left_pointer].isdigit():
                curr_num = line[left_pointer] + curr_num
                left_pointer -= 1
            while right_pointer < len(line) and line[right_pointer].isdigit():
                curr_num += line[right_pointer]
                right_pointer += 1
            if curr_num:
                output.append(int(curr_num))

        return output

    #part 2
    def part2(self):
        for idxLine, line in enumerate(self.data):
            for idxSymbool, symbol in enumerate(line):
                numList = []
                if symbol == '*':
                    numList += self.check(line, idxSymbool)
                    if idxLine > 0:
                        numList += self.check(self.data[idxLine - 1], idxSymbool)
                    if idxLine < len(self.data) - 1:
                        numList += self.check(self.data[idxLine + 1], idxSymbool)

                if len(numList) == 2:
                    self.outputPart2 += (numList[0] * numList[1])

        return self.outputPart2




if __name__ == '__main__':
    #creating an instance of the solution class
    solution = Solution()
    answer1 = solution.part1()
    answer2 = solution.part2()
    print("Answers:")
    print("Part 1: ")
    print(answer1)
    print("Part 2: ")
    print(answer2)