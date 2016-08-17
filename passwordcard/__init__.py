"""Password Card implementation in python.

Original project https://www.passwordcard.org/
Original project code https://www.passwordcard.org/algorithm.html

"""


__license__ = 'GPLv3'
__copyright__ = 'Copyright © 2015 haxwithaxe'
__authors__ = (('haxwithaxe', 'spam@haxwithaxe.net'),)
__credits__ = ['pepsoft.org']


import random
import string


WIDTH = 29
HEIGHT = 9
BODY_HEIGHT = HEIGHT - 1

HEADER_CHARS = list('■□▲△○●★☂☀☁☹☺♠♣♥♦♫€¥£$!?¡¿⊙◐◩�')
DIGITS = string.digits
DIGITS_AND_LETTERS = string.digits+string.ascii_letters
DIGITS_LETTERS_AND_SYMBOLS = "@#$%&*<>?€+{}[]()/\\"


class PasswordCard:
    """Create a new PasswordCard with a specific number and specific options.
     
     Arguments:
        serial_number (int): The serial number or seed of the card. Defaults to a random value.
        digit_area (bool): Whether to include an area containing only digits. Defaults to False.
        include_symbols (bool): Whether to include symbols. Defaults to True.

    """

    def __init__(self, number = None, digitArea=False, includeSymbols=True, eol=None):
        random.seed()
        self.number = number or random.randint(0, 1e9)
        random.seed(self.number)
        self.digitArea = digitArea
        self.includeSymbols = includeSymbols
        self._grid = []
        self.eol = eol or '\n'

    @property
    def grid(self):
        """The contents of the card as a two dimensional array of characters."""
        if not self._grid:
            self.generate_grid()
        return self._grid

    def __str__(self):
        """The contents of the card as a string containing multiple lines, using the specified EOL sequence. Each line except the header will have a line number (starting with 1) appended.

         Returns:
             str: The contents of the card in string format.

        """
        return self.eol.join(' '.join(x) for x in [hex(self.number)]+self.grid)
            
    def generate_grid(self):
        '''
        if self.digitArea:
            halfHeight = HEIGHT / 2
            for y  in range(len(self._grid[:halfHeight])):
                for x in range(WIDTH):
                    self._grid[y][x] = self.oscilate_column(x)
            for y in range(len(self._grid[halfHeight:])):
                    self._grid[y] = [random.choice(DIGITS) for _ in range(WIDTH)]
        else:
        '''
        for y in range(HEIGHT):
            self._grid.append([self.oscilate_column(x) for x in range(WIDTH)])
        header = HEADER_CHARS.copy()
        random.shuffle(header)
        self._grid = [header] + self._grid

    def oscilate_column(self, column):
        if self.includeSymbols and column % 2 == 0:
            return random.choice(DIGITS_LETTERS_AND_SYMBOLS)
        else:
            return random.choice(DIGITS_AND_LETTERS)


if __name__ == '__main__':
    print(PasswordCard(100))
