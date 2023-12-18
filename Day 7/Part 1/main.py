EXAMPLE_FILE_NAME = "example.txt"
INPUT_FILE_NAME = "input.txt"
CARD_VALUE_MAP = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2,
                  '2': 1}
COMBINATION_VALUE_MAP = {'5K': 1, '4K': 2, 'FH': 3, '3K': 4, '2P': 5, '1P': 6, 'HC': 7}


# All cards share the same label
# The length of array is going to be 1, and the only element is 5
def five_of_a_kind(card_count):
    return len(card_count) == 1


# Four cards have the same label and one card has a different label
# The length of array is going to be 2, the array looks like [1,4]
def four_of_a_kind(card_count):
    if len(card_count) != 2:
        return False
    return card_count[1] == 4


# Three cards have the same label, and the remaining two cards share a different label
# The length of array is going to be 2, the array looks like [2,3]
def full_house(card_count):
    if len(card_count) != 2:
        return False
    return card_count[1] == 3 and card_count[0] == 2


# Three cards have the same label, and the remaining two cards are each different from any other card in the hand
# The length of array is going to be 3, the array looks like [1,1,3]
def three_of_a_kind(card_count):
    if len(card_count) != 3:
        return False
    return card_count[2] == 3


# Two cards share one label, two other cards share a second label, and the remaining card has a third label
# The length of array is going to be 3, the array looks like [1,2,2]
def two_pair(card_count):
    if len(card_count) != 3:
        return False
    return card_count[2] == 2


# Two cards share one label, and the other three cards have a different label from the pair and each other
# The length of array is going to be 4, the array looks like [1,1,1,2]
def one_pair(card_count):
    if len(card_count) != 4:
        return False
    return card_count[3] == 2


# Get the combination that corresponds to the hand
# Returns the code of the combination, related to the 'COMBINATION_VALUE_MAP'
def get_combination(card_count):
    if five_of_a_kind(card_count):
        return '5K'
    if four_of_a_kind(card_count):
        return '4K'
    if full_house(card_count):
        return 'FH'
    if three_of_a_kind(card_count):
        return '3K'
    if two_pair(card_count):
        return '2P'
    if one_pair(card_count):
        return '1P'
    return 'HC'  # The type of a hand is going to be high card, all cards are distinct


def read_cards(cards: str):
    card_values = {}
    # Loop through all cards, count the number of appearances and put it in a map
    for el in cards:
        if el in card_values:
            card_values[el] += 1
        else:
            card_values[el] = 1
    card_count = sorted(card_values.values())
    return COMBINATION_VALUE_MAP[get_combination(card_count)]


# Sorts hands based on the type
# If two hands are of the same type we compare the card values
# We use selection sort, because it's the easiest to implement
def sort_hands(hands):
    # Returns True if card1 is greater than card2, returns False if card2 is greater than card1
    def compare_card_numbers(card1, card2):
        for i in range(len(card1)):
            if CARD_VALUE_MAP[card1[i]] > CARD_VALUE_MAP[card2[i]]:
                return True
            if CARD_VALUE_MAP[card1[i]] < CARD_VALUE_MAP[card2[i]]:
                return False
        return True

    # Go through every hand, i-th element will always be the weakest hand
    for i in range(len(hands)):
        # We compare the i-th element to all elements after it
        for j in range(i + 1, len(hands)):
            if hands[i][2] < hands[j][2]:  # Weaker hand type is going to have a higher value, based on 'COMBINATION_VALUE_MAP'
                hands[i], hands[j] = hands[j], hands[i]
            if hands[i][2] == hands[j][2]:
                if compare_card_numbers(hands[i][0], hands[j][0]):
                    hands[i], hands[j] = hands[j], hands[i]  # The hand with smaller card value is going to the i-th place


def main():
    with open(INPUT_FILE_NAME, 'r') as file:
        lines = file.readlines()

        hands = []
        for line in lines:
            [cards, pay] = line.strip().split(" ")  # Each row is going to be in format 'CARDS PAY'
            value = read_cards(cards)  # The value is based on the type of hand and 'COMBINATION_VALUE_MAP'
            hands.append((cards, int(pay), value))

        sort_hands(hands)

        res = 0
        # Calculating the result
        for i in range(len(hands)):
            res += hands[i][1] * (i + 1)  # Because we sorted the hands, we multiply the pay with the position in array
        print(hands)
        print(res)


if __name__ == "__main__":
    main()
