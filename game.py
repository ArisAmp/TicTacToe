from player import HumanPlayer, ComputerPlayer
import time

class TicTacToe():
    def __init__(self) -> None:
        self.board = {'1': ' ', '2': ' ', '3': ' ',\
                    '4' :' ', '5': ' ', '6': ' ',\
                    '7': ' ', '8':' ', '9':' '}
    
    #Printing pattern for the board.
    def print_board(self):
        print(self.board['7'] + '|' + self.board['8'] + '|' + self.board['9'])
        print("-+-+-")
        print(self.board['4'] + '|' + self.board['5'] + '|' + self.board['6'])
        print("-+-+-")
        print(self.board['1'] + '|' + self.board['2'] + '|' + self.board['3'])

    #Return a list with all available moves --> empty places in the board.
    def available_moves(self):
        return [k for k in self.board if self.board[k] ==' ']

    def check_winner(self, player):
        if self.board['7'] == self.board['8'] == self.board['9'] != ' ': #Check if the winning line across the top(7-8-9) is filled by the same player
            self.print_board()
            print("\nGame Over\n")
            print("***** player " + player.symbol + " won *****")
            return True

        elif self.board['4'] == self.board['5'] == self.board['6'] != ' ':#Check if the winning line across the middle(5-6-7) is filled by the same player
            self.print_board()
            print("\nGame Over\n")
            print("***** player " + player.symbol + " won *****")
            return True

        elif self.board['1'] == self.board['2'] == self.board['3'] != ' ':#Check if the winning line across the bottom(1-2-3) is filled by the same player
            self.print_board()
            print("\nGame Over\n")
            print("***** player " + player.symbol + " won *****")
            return True

        elif self.board['1'] == self.board['5'] == self.board['9'] != ' ':#Check if the winning diagonal line (1-5-9) is filled by the same player
            self.print_board()
            print("\nGame Over\n")
            print("***** player " + player.symbol + " won *****")
            return True

        elif self.board['3'] == self.board['5'] == self.board['7'] != ' ':#Check if the winning diagonal line (3-5-7) is filled by the same player
            self.print_board()
            print("\nGame Over\n")
            print("***** player " + player.symbol + " won *****")
            return True

        elif self.board['1'] == self.board['4'] == self.board['7'] != ' ':#Check if the winning line down left side (1-4-7) is filled by the same player
            self.print_board()
            print("\nGame Over\n")
            print("***** player " + player.symbol + " won *****")
            return True

        elif self.board['2'] == self.board['5'] == self.board['8'] != ' ':#Check if the winning line down middle (1-4-7) is filled by the same player
            self.print_board()
            print("\nGame Over\n")
            print("***** player " + player.symbol + " won *****")
            return True
            
        elif self.board['3'] == self.board['6'] == self.board['9'] != ' ':#Check if the winning line down right side(3-6-9) is filled by the same player
            self.print_board()
            print("\nGame Over\n")
            print("***** player " + player.symbol + " won *****")
            return True
    
    #True if there are empty places in the board.
    def empty_squares(self):
        for k in self.board:
            if self.board[k] == ' ':
                return True

#Main function to play the game.
def play(game, x_player, o_player):

    symbol = "X"
    count = 0
    while game.empty_squares():
        
        #Print the board every round
        game.print_board()

        if symbol == "X":
            move = x_player.get_move(game)
        else:
            move = o_player.get_move(game)

        game.board[move] = symbol
        count +=1
        
        #Check for winner after 5 rounds have been played
        if count >= 5 and symbol == "X": 
            if game.check_winner(x_player):
                break
        elif count >= 5 and symbol == "O":
            if game.check_winner(o_player):
                break
            
        #Change player after each play
        symbol = "O" if symbol == "X" else "X"
        
        print(' ')
        time.sleep(0.6)
        
        #After 9 rounds with no winners the game is tie
        if count == 9: 
            print("It's a Tie Game.")
        
        




if __name__ == "__main__":
    game = TicTacToe()
    p1 = ComputerPlayer("X")
    p2 = ComputerPlayer("O")

    play(game, p1, p2)
            