EXAMPLE_FILE_NAME = "example.txt"
INPUT_FILE_NAME = "input.txt"


# Putting all nodes into a map
def read_map(lines, location_map):
    for i in range(2, len(lines)):
        line = lines[i].strip()
        # Lines look like 'NAME = (LEFT, RIGHT)'
        [location, directions] = line.split("=")
        left, right = directions[2:len(directions) - 1].split(",")

        location_map[location.strip()] = (left.strip(), right.strip())


# Returns the number of steps needed to reach "ZZZ" from "AAA"
def traverse_map(instructions, location_map):
    c = 0
    current_location = "AAA"

    while current_location != "ZZZ":
        direction = instructions[
            c % (len(instructions) - 1)]  # We use 'c % (len(instructions) - 1)' to always stay within the array

        # Based on the direction variable we move to the first element if it's equal to 'L', and vice versa for 'R'
        if direction == 'L':
            current_location = location_map[current_location][0]
        else:
            current_location = location_map[current_location][1]
        c += 1
    return c


def main():
    with open(INPUT_FILE_NAME, 'r') as file:
        lines = file.readlines()

        instructions = lines[0]
        location_map = {}  # Format: 'NAME_OF_LOCATION':('LEFT_OPTION','RIGHT_OPTION')
        read_map(lines, location_map)
        count = traverse_map(instructions, location_map)
        print(count)


if __name__ == "__main__":
    main()
