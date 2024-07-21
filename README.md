# portfolio-project

**Remember that this project cannot be submitted late.**

Pentago is a two-player abstract strategy game played on a 6×6 board, which is divided into four 3×3 sub-boards (or quadrants). Players take turns placing a marble of their color (either black or white) onto an unoccupied space on the board and then rotating one of the sub-boards by 90 degrees, either clockwise or anti-clockwise. The rotation step is mandatory, and the player can choose to rotate any of the four sub-boards, not necessarily the one where they placed the marble.

To learn how to play the game, check out this video: How to Play Pentago.[(https://boardgamegeek.com/video/482262/pentago/how-to-play-pentago)](https://boardgamegeek.com/video/482262/pentago/how-to-play-pentago) and you could play it by yourself in this website: [(https://pentago.vercel.app/)](https://pentago.vercel.app/)

A player wins by getting five of their marbles in a vertical, horizontal, or diagonal row, either before or after the sub-board rotation. If a player achieves five-in-a-row before the rotation step, the game ends immediately, and the player doesn't need to rotate a sub-board. If both players achieve five-in-a-row after the rotation, the game is a draw. If only the opponent gets a five-in-a-row after the rotation, the opponent wins. If all 36 spaces on the entire board are occupied without forming a row of five after the rotation, the game ends in a draw.

For example, after the white player places a marble on the board, several scenarios could occur:

If the white player achieves five-in-a-row, they win immediately.

If the white player does not achieve five-in-a-row, after the rotation:

* a. If neither white nor black has a five-in-a-row, the game continues.
* b. If black achieves five-in-a-row, black wins.
* c. If white achieves five-in-a-row, white wins.
* d. If both players achieve five-in-a-row, the game is a draw.
* 
If neither white nor black has a five-in-a-row after the rotation and the board is full with 36 pieces, the game ends in a draw.

Here, we assume that black will play first. The figure "game_board" illustrates how the board will be labeled using our notation. ![board](game_board.png "game board")The four sub-boards are labeled with the integers 1, 2, 3, and 4, as shown in the figure. The six rows are labeled from 'a' to 'f' from top to bottom, and the six columns are labeled from '0' to '5' from left to right. Each space on the board can then be referred to as 'a0', 'a1', and so on.


Special rules for this variant of chess:

In Atomic Chess, whenever a piece is captured, an "explosion" occurs at the 8 squares immediately surrounding the captured piece in all the directions. This explosion kills all of the pieces in its range except for **pawns**. Different from regular chess, where only the captured piece is taken off the board, in Atomic Chess, every capture is suicidal. Even the capturing piece is affected by the explosion and must be taken off the board. As a result, a pawn can only be removed from the board when directly involved in a capture. If that is the case, both capturing and captured pawns must be removed from the board. Because every capture causes an explosion that affects not only the victim but also the capturing piece itself, **the king is not allowed to make captures**. Also, a player **cannot blow up both kings at the same time**. In other words, the move that would kill both kings in one step is not allowed. Blowing up a king has the same effect as capturing it, which will end the game.
[(https://www.chess.com/terms/atomic-chess#captures-and-explosions)](https://www.chess.com/terms/atomic-chess#captures-and-explosions)

Your ChessVar class must include the following:
* An **init method** that initializes any data members
* A method called **get_game_state** that just returns 'UNFINISHED', 'WHITE_WON', 'BLACK_WON'. 
* A method called **make_move** that takes two parameters - strings that represent the square moved from and the square moved to.  For example, make_move('b2', 'b4').  If the square being moved from does not contain a piece belonging to the player whose turn it is, or if the indicated move is not allowed, or if the game has already been won, then it should **just return False**.  Otherwise it should make the indicated move, remove any captured (explosion) pieces from the board, update the game state (unfinished to who wins) if necessary, update whose turn it is, and return True.

You need to implement a method called **print_board** that outputs the current state of the board. This will be extremely helpful for testing. You can choose any format for displaying the board, provided it is legible to others. If you're uncertain about the acceptability of your format, ask it on the discussion board.

Feel free to add whatever other classes, methods, or data members you want.  All data members of a class must be private.  Every class should have an init method that initializes all of the data members for that class.

Here's a very simple example of how the class could be used:
```
game = ChessVar()
print(game.make_move('d2', 'd4'))  # output True
print(game.make_move('g7', 'g5'))  # output True
print(game.make_move('c1', 'g5'))  # output True
game.print_board()
print(game.get_game_state())  # output UNFINISHED
```
The file must be named: ChessVar.py
