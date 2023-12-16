EXAMPLE_FILE_NAME = "example.txt"
INPUT_FILE_NAME = "input.txt"


def read_map(lines, row: int, values):
    modified_index = set() # Keep track of the indexes we have modified within the map
    while row < len(lines) and lines[row] != '\n':
        line = lines[row].strip()
        [destination_start, source_start, source_range] = line.split(" ")
        destination_start, source_start, source_range = int(destination_start), int(source_start), int(source_range)

        # Loop through all of the values
        for i in range(len(values)):
            if i in modified_index:
                continue
            val = values[i]
            if source_start <= val < source_start + source_range: # If the value is in the correct range
                values[i] += destination_start - source_start # To get the new value we subtract the value of the source start from the destination start and add it to the value
                modified_index.add(i)
        row += 1
    return row  # We return the row index so that we can continue from the end of the map


def main():
    with open(INPUT_FILE_NAME, 'r') as file:
        lines = file.readlines()

        # Get values from first line, they are the starting values
        values = []
        for num in lines[0].split(":")[1].strip().split(" "):
            values.append(int(num))

        # Reading the maps
        row = 2
        while row < len(lines):
            if lines[row] == '\n':  # If the row is empty skip
                row += 1
                continue
            row = read_map(lines, row + 1,
                           values)  # row+1 is the start of the map, because the value of row is the name of the map
        print(min(values))


if __name__ == "__main__":
    main()
