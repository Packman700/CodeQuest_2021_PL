from typing import Union
from string import ascii_uppercase

def return_playfair_table(key: str) -> list:
    # CREATE LIST 1 DIMENSION FOR PLAYFAIR ENCRYPTING
    key_list = list(dict.fromkeys(key))
    alphabet_list = list(ascii_uppercase)
    filter_alphabet_list = [letter for letter in alphabet_list if letter not in key_list]
    key_list = [*key_list, *filter_alphabet_list]
    key_list.remove('J')

    # CONVERT LIST TO 2D
    ROW_SIZE = 5
    COLUMN_SIZE = 5
    index_tuples = [(index // ROW_SIZE, index % COLUMN_SIZE) for index in range(ROW_SIZE * COLUMN_SIZE)]

    playfair_table = []
    for letter, (row, column) in zip(key_list, index_tuples):
        if column == 0:
            playfair_table.append([])
        playfair_table[row].append(letter)

    return playfair_table

def return_tuple_pairs(message: str) -> tuple:
    return tuple(zip(list(message[::2]), list(message[1::2])))

def find_letter_position(playfair_table: list, letter: str) -> Union[tuple, None]:
    for row_index, row in enumerate(playfair_table):
        if letter in row:
            column_index = row.index(letter)
            return row_index, column_index
    return None

def decode_pair(playfair_table: list, pair: tuple) -> str:
    char_1, char_2 = pair[0], pair[1]
    row_1, column_1 = find_letter_position(playfair_table, char_1)
    row_2, column_2 = find_letter_position(playfair_table, char_2)

    if row_1 == row_2:
        encrypted_char_1 = playfair_table[row_1][column_1 - 1]
        encrypted_char_2 = playfair_table[row_1][column_2 - 1]
    elif column_1 == column_2:
        encrypted_char_1 = playfair_table[row_1 - 1][column_1]
        encrypted_char_2 = playfair_table[row_2 - 1][column_1]
    else:
        encrypted_char_1 = playfair_table[row_1][column_2]
        encrypted_char_2 = playfair_table[row_2][column_1]
    return f"{encrypted_char_1}{encrypted_char_2}"

def main():
    for _ in range(int(input())):
        amount_to_use, key = input().split(' ')
        amount_to_use = int(amount_to_use)
        playfair_table = return_playfair_table(key)
        for _ in range(amount_to_use):
            encrypted_message = input()
            pairs = return_tuple_pairs(encrypted_message)
            decoded_message = ""
            for pair in pairs:
                decoded_message += decode_pair(playfair_table, pair)
            print(decoded_message.lower())

if __name__ == '__main__':
    main()
