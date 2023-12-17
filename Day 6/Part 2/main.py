EXAMPLE_FILE_NAME = "example.txt"
INPUT_FILE_NAME = "input.txt"


# We know that there exists the range of numbers from which we can get the right result
# We get that range by finding the numbers before and after that range
def check_race(time: int, distance: int) -> int:
    l, r = 0, time  # l is the number before the start of the range, r is the number after the end of the range

    while (time - l) * l <= distance:  # We increment l until we get the number which gets the right distance
        l += 1

    while (time - r) * r <= distance:  # We increment r until we get the number which gets the right distance
        r -= 1

    return r - l + 1


def main():
    with open(INPUT_FILE_NAME, 'r') as file:
        lines = file.readlines()

        # Both lines are in the same format, so we get the numbers ('Text: n n n n ...')
        time = int(''.join(lines[0].split(":")[1].strip().split(" ")))  # We know the first line is for times
        distance = int(''.join(lines[1].split(":")[1].strip().split(" ")))  # We know that the second line is for times

        print(check_race(time, distance))


if __name__ == "__main__":
    main()
