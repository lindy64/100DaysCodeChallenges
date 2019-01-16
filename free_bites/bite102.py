VALID_COLORS = ['blue', 'yellow', 'red']

def print_colors():
    """Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
    while True:
        color = input("enter the colour:  ").lower()
        if color == "quit":
            print('bye')
            break
        if color in VALID_COLORS:
            print(color)
        else:
            print("Not a valid color")


from unittest.mock import patch


@patch("builtins.input", side_effect=['blue', 'Yellow', 'white',
                                      'red', 'Orange', 'quit'])
def test_print_colors(input_mock, capfd):
    not_valid = 'Not a valid color'
    expected = '\n'.join(['blue', 'yellow', not_valid, 'red',
                          not_valid, 'bye'])

    print_colors()

    output = capfd.readouterr()[0].strip()
    assert output == expected
