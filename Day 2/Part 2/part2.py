EXAMPLE_FILE_NAME = "example.txt"
INPUT_FILE_NAME = "input.txt"

# We find the highest value for red, green and blue in each game and multiply them
def game_power(line: str) -> int:
    s = line.split(":")[1]
    s = s.strip() # s is going to be in format: 'set1; set2;... setN;'
    max_map={"blue":-1,"green":-1,"red":-1}
    for game_set in s.split(";"):  # every set is going to look like 'number color, number color...'
        for combination in [item.strip() for item in game_set.split(',')]:
            [number, color] = combination.split(' ')
            if int(number) > max_map[color]:
                max_map[color]=int(number)
    return max_map["blue"]*max_map["green"]*max_map["red"]


def main():
    s = 0
    with open(INPUT_FILE_NAME, 'r') as file:
        for line in file:
            s += game_power(line)
    print(s)


if __name__ == "__main__":
    main()
