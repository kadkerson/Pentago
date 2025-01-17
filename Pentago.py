# Author: Kyle Adkerson
# GitHub Username: kadkerson
# Date: 08/13/2024
# Description: Program simulates the Pentago board game. It has 1 class, Pentago. It contains the methods
#              get_game_state(), is_board_full(), print_board(), make_move(), update_turn(), rotate_sub_board(), and
#              check_win(). The game can be played by first creating a Pentago object. Then, the user can use the
#              make_move() method to play. Once a valid move is made, rotate_sub_board() is called to rotate the
#              sub-board in the direction the user chose. check_win() is called before and after the rotation to see if
#              anyone won. print_board() can be used to print the current state of the board for the user.
#

class Pentago:
    """Represents the Pentago game, played by 2 players (black and white). Black has the first move."""
    def __init__(self):
        self._board = [
            ['□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□']
        ]
        self._turn_tracker = 'black'  # black starts first
        self._game_state = 'UNFINISHED'
        self._rows = {'a': 0,
                      'b': 1,
                      'c': 2,
                      'd': 3,
                      'e': 4,
                      'f': 5}
        self._columns = {'0': 0,  # rows and columns represented as dictionaries for placing marbles
                         '1': 1,
                         '2': 2,
                         '3': 3,
                         '4': 4,
                         '5': 5}

    def get_game_state(self):
        """
        Returns current game state
        """
        return self._game_state

    def is_board_full(self):
        """
        Checks for any empty spaces on the board. Returns False if there is, True if there is not.
        """
        for row in self._board:
            for cell in row:
                if cell == '□':
                    return False
        return True

    def print_board(self):
        """
        Prints the current state of the board. Adds row and column headers for formatting.
        """
        print("  0 1 2   3 4 5")
        for row_label, row_index in self._rows.items():
            if row_index == 3:
                print("  " + '-------------')
            vert_divider = ''
            for col_label in self._columns:
                col_index = self._columns[col_label]
                vert_divider += self._board[row_index][col_index] + ' '
                if col_index == 2:
                    vert_divider += '| '
            print(row_label, vert_divider)

    def make_move(self, color, position, sub_board, rotation):
        """
        Places a marble in a position, rotates a sub-board in a chosen direction, and then switches turns.
        """
        if self._game_state != 'UNFINISHED':
            return 'game is finished'

        if color != self._turn_tracker:
            return "not this player's turn"

        row = self._rows[position[0]]  # use dictionaries from innit method for marble placement
        col = self._columns[position[1]]

        if self._board[row][col] != '□':
            return "position is not empty"

        if color == 'black':
            self._board[row][col] = '○'  # symbol for Player 1/Black
        else:
            self._board[row][col] = '●'  # symbol for Player 2/White

        if self.check_win('white'):
            self._game_state = "WHITE_WON"
            return True  # end game if win is before rotation so board accurately reflects win
        elif self.check_win('black'):
            self._game_state = "BLACK_WON"
            return True  # end game if win is before rotation so board accurately reflects win

        self.rotate_sub_board(sub_board, rotation)

        if self.check_win('white'):  # recheck wins after rotation
            self._game_state = "WHITE_WON"
        elif self.check_win('black'):
            self._game_state = "BLACK_WON"
        elif self.is_board_full():  # check if draw occurred
            self._game_state = 'DRAW'

        self.update_turn()

        return True

    def update_turn(self):
        """
        Changes whose turn it is.
        """
        if self._turn_tracker == 'black':
            self._turn_tracker = 'white'
        else:
            self._turn_tracker = 'black'

    def rotate_sub_board(self, sub_board, direction):
        """
        Rotates a 3x3 sub-board by 90 degrees in a chosen direction (clockwise or
        anti-clockwise) when a move is made.
        """
        sub_board_locations = {1: (0, 0),
                               2: (0, 3),
                               3: (3, 0),
                               4: (3, 3)}

        start_row, start_col = sub_board_locations[sub_board]
        current_board = []
        for row_index in range(3):  # copies sub-board as is
            row = []
            for col_index in range(3):
                row.append(self._board[start_row + row_index][start_col + col_index])
            current_board.append(row)

        rotation = None
        if direction == 'C':
            rotation = [
                [current_board[2][0], current_board[1][0], current_board[0][0]],
                [current_board[2][1], current_board[1][1], current_board[0][1]],
                [current_board[2][2], current_board[1][2], current_board[0][2]],
            ]
        elif direction == 'A':
            rotation = [
                [current_board[0][2], current_board[1][2], current_board[2][2]],
                [current_board[0][1], current_board[1][1], current_board[2][1]],
                [current_board[0][0], current_board[1][0], current_board[2][0]],
            ]

        for row_index in range(3):  # replace old sub-board with rotated sub-board
            for col_index in range(3):
                self._board[start_row + row_index][start_col + col_index] = rotation[row_index][col_index]

    def check_win(self, color):
        """
        Checks if a player has placed 5 of their marbles in a row.
        """
        if color == 'black':
            marble = '○'
        else:
            marble = '●'

        row_indices = list(self._rows.values())
        col_indices = list(self._columns.values())

        for row in row_indices:  # horizontal win check
            for col in col_indices[:-4]:
                if (self._board[row][col] == marble
                        and self._board[row][col + 1] == marble
                        and self._board[row][col + 2] == marble
                        and self._board[row][col + 3] == marble
                        and self._board[row][col + 4] == marble):
                    return True

        for col in col_indices:  # vertical win check
            for row in row_indices[:-4]:
                if (self._board[row][col] == marble
                        and self._board[row + 1][col] == marble
                        and self._board[row + 2][col] == marble
                        and self._board[row + 3][col] == marble
                        and self._board[row + 4][col] == marble):
                    return True

        for row in row_indices[:-4]:   # down right diagonal win check
            for col in col_indices[:-4]:
                if (self._board[row][col] == marble
                        and self._board[row + 1][col + 1] == marble
                        and self._board[row + 2][col + 2] == marble
                        and self._board[row + 3][col + 3] == marble
                        and self._board[row + 4][col + 4] == marble):
                    return True

        for row in row_indices[:-4]:   # down left diagonal win check
            for col in col_indices[4:]:
                if (self._board[row][col] == marble
                        and self._board[row + 1][col - 1] == marble
                        and self._board[row + 2][col - 2] == marble
                        and self._board[row + 3][col - 3] == marble
                        and self._board[row + 4][col - 4] == marble):
                    return True
        return False


def main():

    game = Pentago()
    print(game.make_move('black', 'b0', 4, 'C'))
    print(game.make_move('white', 'a1', 4, 'A'))
    print(game.make_move('black', 'b1', 4, 'C'))
    print(game.make_move('white', 'a2', 4, 'A'))
    print(game.make_move('black', 'b2', 4, 'C'))
    print(game.make_move('white', 'a3', 4, 'A'))
    print(game.make_move('black', 'b3', 1, 'C'))
    print(game.make_move('white', 'a4', 4, 'A'))
    print(game.make_move('black', 'b5', 2, 'C'))
    print(game.make_move('white', 'd2', 1, 'A'))
    print(game.make_move('black', 'b4', 2, 'C'))

    game.print_board()
    print(game.get_game_state())


if __name__ == "__main__":
    main()
