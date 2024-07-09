def add(number_one, number_two):
    return number_one + number_two


def divide(number_one, number_two):
    if number_two == 0:
        raise ValueError
    return number_one / number_two


def add_string(char_1, char_2):
    return char_1 + " " + char_2
