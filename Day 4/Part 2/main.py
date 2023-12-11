EXAMPLE_FILE_NAME = "example.txt"
INPUT_FILE_NAME = "input.txt"


def game_points(line: str, cards, index: int):  # Line is in format 'Game ID: n n n n | n n n n'
    line.strip()
    [first_half, numbers] = line.split(':')[1].strip().split(
        '|')  # First we get the 'n n n n | n n n n' part, and then 'n n n n'

    first_half.strip()
    numbers.strip()

    # Converting the winning numbers to a set, so the search is faster
    winning_numbers = set()
    [winning_numbers.add(item.strip()) for item in first_half.split(' ') if item != '']

    # Calculating the number of matches
    points = 0
    for n in numbers.split(' '):
        if n == ' ':
            continue
        if n in winning_numbers:  # Check if the number matches to a winning number
            points += 1

    if points == 0:  # If there are no matches that means that we get no copies
        return
    # If there are matches we add the copies to all cards that have the index '<=index+points'
    for i in range(index + 1, index + points + 1):
        cards[i] += cards[index] # We add the copies evenly, so (points*cards[index])/points


def main():
    with open(INPUT_FILE_NAME, 'r') as file:
        lines = file.readlines()
        cards = []  # Represents how many copies of each card you have used
        cards = [1] * len(lines)  # For each card we know we have at least the original
        for i in range(len(lines)):
            game_points(lines[i], cards, i)
        # The sum of cards array
        s = 0
        for c in cards:
            s += c
        print(s)


if __name__ == "__main__":
    main()
