EXAMPLE_FILE_NAME = "example.txt"
INPUT_FILE_NAME = "input.txt"


def game_points(line: str):  # Line is in format 'Game ID: n n n n | n n n n'
    line.strip()
    [first_half, numbers] = line.split(':')[1].strip().split(
        '|')  # First we get the 'n n n n | n n n n' part, and then 'n n n n'

    first_half.strip()
    numbers.strip()

    # Converting the winning numbers to a set, so the search is faster
    winning_numbers = set()
    [winning_numbers.add(item.strip()) for item in first_half.split(' ') if item != '']

    points = 0
    for n in numbers.split(' '):
        if n == ' ':
            continue
        if n in winning_numbers:  # Check if the number matches to a winning number
            points = 1 if points == 0 else points * 2  # If this is the first match points==0
    return points


def main():
    with open(INPUT_FILE_NAME, 'r') as file:
        sum = 0
        for line in file:
            sum += game_points(line)
        print(sum)


if __name__ == "__main__":
    main()
