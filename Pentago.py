# Author: Kyle Adkerson
# GitHub Username: kadkerson
# Date: 08/13/2024
# Description: DESCRIPTION
#

class Player:
    """Represents a Pentago player with a name and color (white or black)"""
    def __init__(self, name, color):
        self._name = name
        self._color = color

    def get_name(self):
        """Returns the name of the player"""
        return self._name

    def get_color(self):
        """Returns the color of the player"""
        return self._color


class Pentago:
    def __init__(self):
        self._board = self._board = [
            ['□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□']
        ]
        self._players = []
        self._turn_tracker = 0  # turn 0 is white/player 1, turn 1 is black/player 2
        self._game_state = 'UNFINISHED'
        self._rows = {'A': 0,
                      'B': 1,
                      'C': 2,
                      'D': 3,
                      'E': 4,
                      'F': 5}
        self._columns = {'0': 0,  # rows and columns represented as dictionaries for placing marbles
                         '1': 1,
                         '2': 2,
                         '3': 3,
                         '4': 4,
                         '5': 5}

    def create_player(self, player):
        self._players.append(player)

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

        current_turn = self._players[self._turn_tracker]
        if current_turn.get_color() != color:
            return "not this player's turn"

        row = self._rows[position[0]]
        col = self._columns[position[1]]

        if self._board[row][col] != '□':
            return "position is not empty"

        if color == 'white':
            self._board[row][col] = '●'  # Symbol for Player 1/White
        else:
            self._board[row][col] = '○'  # Symbol for Player 2/Black

        if self.check_win('white'):
            self._game_state = "WHITE_WON"
            return True  # end game if win is before rotation so board accurately reflects win
        elif self.check_win('black'):
            self._game_state = "BLACK_WON"
            return True  # end game if win is before rotation so board accurately reflects win


        if self.check_win('white'):  # recheck wins after rotation
            self._game_state = "WHITE_WON"
        elif self.check_win('black'):
            self._game_state = "BLACK_WON"
        elif self.is_board_full():  # check if draw occurred
            self._game_state = 'DRAW'

        if self._turn_tracker == 0:  # switch turns
            self._turn_tracker = 1
        else:
            self._turn_tracker = 0
        return True

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
        for row_index in range(3):  # loop to pop out sub-board as is
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

        for row_index in range(3):  # put sub-board back into game
            for col_index in range(3):
                self._board[start_row + row_index][start_col + col_index] = rotation[row_index][col_index]

    def check_win(self, color):
        """
        Checks if a player has placed 5 of their marbles in a row.
        """
        if color == 'white':
            marble = '●'
        else:
            marble = '○'

        row_indices = list(self._rows.values())
        col_indices = list(self._columns.values())

        for row in row_indices:  # horizon win check
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
    p1 = Player('alice', 'white')
    p2 = Player('jake', 'black')
    game = Pentago()
    game.create_player(p1)
    game.create_player(p2)
    print(game.make_move('white', 'A0', 4, 'A'))
    print(game.make_move('black', 'B0', 4, 'C'))
    print(game.make_move('white', 'A1', 4, 'A'))
    print(game.make_move('black', 'B1', 4, 'C'))
    print(game.make_move('white', 'A2', 4, 'A'))
    print(game.make_move('black', 'B2', 4, 'C'))
    print(game.make_move('white', 'A3', 4, 'A'))
    print(game.make_move('black', 'B3', 1, 'C'))
    print(game.make_move('white', 'A4', 4, 'A'))
    print(game.make_move('black', 'B5', 2, 'C'))
    print(game.make_move('white', 'D2', 1, 'A'))
    print(game.make_move('black', 'D5', 2, 'A'))
    game.print_board()
    print(game.get_game_state())


if __name__ == "__main__":
    main()