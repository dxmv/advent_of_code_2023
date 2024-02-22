EXAMPLE_FILE_NAME = "example.txt"
INPUT_FILE_NAME = "input.txt"


# returns True if the whole array consists of 0, False otherwise
def all_zeroes(arr) -> bool:
    for n in arr:
        if n != 0:
            return False
    return True


# returns the matrix of differences
def generate_result(arr):
    res_arr = [arr]
    index = 0  # index for traversing the res_arr
    while not all_zeroes(res_arr[index]):
        res_arr.append([])
        for i in range(1, len(res_arr[index])):
            res_arr[index + 1].append(
                res_arr[index][i] - res_arr[index][i - 1])  # add the elements at i and i-1 'above'
        index += 1  # now the new row becomes the previous row
    return res_arr


def get_next(arr):
    res_arr = generate_result(arr)
    res_arr[len(res_arr) - 1].append(0)  # add 0 to the last row
    for i in range(len(res_arr) - 2, -1, -1):  # traverse from the second to last row to the first
        res_arr[i].append(res_arr[i][len(res_arr[i]) - 1] + res_arr[i + 1][
            len(res_arr[i + 1]) - 1])  # add the last element in the row 'below' and the last element of the current row
    return res_arr[0][len(res_arr[0]) - 1]  # last element of the first row


def main():
    with open(INPUT_FILE_NAME, 'r') as file:
        lines = file.readlines()
        res = 0
        for line in lines:
            # convert line to numbers array
            num_array = [int(x) for x in line.strip().split(" ")]
            # get the next number
            res += get_next(num_array)
        print(res)


if __name__ == "__main__":
    main()
