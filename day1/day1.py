from aocd import get_data


class Solution:
    def __init__(self):
        self.data = get_data(year=2023, day=1).splitlines()
        self.text_to_number_mapping = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6',
                                       'seven': '7', 'eight': '8', 'nine': '9'}

    def get_number(self, line, reverse=False, digits_only=True):
        text = ''
        line_to_check = line[::-1] if reverse else line

        for x in line_to_check:
            if x.isdigit():
                return x
            if not digits_only:
                text += x

                for word in self.text_to_number_mapping:
                    check = word[::-1] if reverse else word
                    if check in text:
                        return self.text_to_number_mapping[word]

    def solve(self, digits_only=True):
        numbers = []

        for line in self.data:
            first = self.get_number(line, digits_only=digits_only)
            last = self.get_number(line, True, digits_only=digits_only)
            numbers.append(int(first + last))

        return sum(numbers)


if __name__ == '__main__':
    solution = Solution()
    print(f'Part 1: {solution.solve()}')
    print(f'Part 2: {solution.solve(False)}')