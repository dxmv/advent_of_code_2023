EXAMPLE_FILE_NAME = "example.txt"
INPUT_FILE_NAME = "input.txt"


def check_race(time: int, distance: int) -> int:
    c = 0  # The number of ways to win
    for charge in range(0, time):  # Going through all the combinations of holding down the button
        if charge * (
                time - charge) > distance:  # Charge is equal to speed, time-charge is equal to the seconds remaining, when we multiply them we get the distance
            c += 1  # If this is true than increment count
    return c


def main():
    with open(INPUT_FILE_NAME, 'r') as file:
        lines = file.readlines()

        # Both lines are in the same format, so we get the numbers ('Text: n n n n ...')
        times = [line for line in lines[0].split(":")[1].strip().split(" ") if
                 line != '']  # We know the first line is for times
        distances = [line for line in lines[1].split(":")[1].strip().split(" ") if
                     line != '']  # We know that the second line is for distances

        res = 1  # Result
        for i in range(len(times)):  # Going through all the time and distance pairs
            res *= check_race(int(times[i]), int(distances[i]))
        print(res)


if __name__ == "__main__":
    main()
