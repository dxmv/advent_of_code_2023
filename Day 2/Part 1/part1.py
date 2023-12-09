EXAMPLE_FILE_NAME = "example.txt"
INPUT_FILE_NAME = "input.txt"

MAX_MAP = {"red": 12, "green": 13, "blue": 14}


# s is going to be in format: 'set1; set2;... setN;'
def possible_game(s: str) -> bool:
    s = s.strip()
    for game_set in s.split(";"):  # every set is going to look like 'number color, number color...'
        for combination in [item.strip() for item in game_set.split(',')]:
            [number, color] = combination.split(' ')
            if int(number) > MAX_MAP[color]:
                return False
    return True


def check_game(line: str) -> int:
    [first_part, second_part] = line.split(":")
    game_id = first_part.split(" ")[1]  # First part is going to look like: 'Game ID', with this we get the id
    if possible_game(second_part):
        return int(game_id)
    return 0  # If the game isn't valid we return 0 so we don't add anything to sum


def main():
    sum = 0
    with open(INPUT_FILE_NAME, 'r') as file:
        for line in file:
            sum += check_game(line)
    print(sum)


if __name__ == "__main__":
    main()
