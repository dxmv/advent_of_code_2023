FILE_NAME = "input_part2.txt"


def part1():
    def get_number_line(line: str) -> int:
        line = line.strip()
        l, r = 0, len(line) - 1
        # Use the two pointer approach to get the most left, and most right number
        while True:
            if line[l].isdigit() and line[r].isdigit():
                break
            if not line[l].isdigit():
                l += 1
            if not line[r].isdigit():
                r -= 1
        return int(line[l]) * 10 + int(line[r])  # Construct the number

    sum = 0
    # Open a file in read mode
    with open(FILE_NAME, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            sum += get_number_line(line)
    print(sum)


def part2():
    def get_numbers_from_line(line: str):
        def get_number(line: str, start=0, end=len(line), step=1):
            result = -1
            for i in range(start, end, step):
                # If we encounter a digit first we return it
                if line[i].isdigit():
                    result = int(line[i])
                    break
                # If we don't encounter a digit we check if it forms the string that corresponds to a key in the numbers map
                else:
                    found = False
                    for n in lenghts:
                        sub = line[i:i + n]  # Substring
                        if sub in numbers:
                            result = numbers[sub]
                            found = True
                            break
                    if found:
                        break
            return result

        numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
        lenghts = [3, 4, 5]  # Lengths of number strings above
        line = line.strip()
        # Find the leftmost and rightmost number representation
        left_number = get_number(line)
        right_number = get_number(line, start=len(line) - 1, end=-1, step=-1)
        return left_number * 10 + right_number  # Construct the number

    sum = 0
    # Open a file in read mode
    with open(FILE_NAME, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            sum += get_numbers_from_line(line)
    print(sum)


if __name__ == "__main__":
    part2()
