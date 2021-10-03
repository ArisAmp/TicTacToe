theBoard = {'1': ' ', '2': ' ', '3': ' ',\
            '4' :' ', '5': ' ', '6': ' ',\
            '7': ' ', '8':' ', '9':' '}

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print("-+-+-")
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print("-+-+-")
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def checkWinner(player):
    if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': #Check if the winning line across the top(7-8-9) is filled by the same player
        printBoard(theBoard)
        print("\nGame Over\n")
        print("***** player " + player + " won *****")
        
    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':#Check if the winning line across the middle(5-6-7) is filled by the same player
        printBoard(theBoard)
        print("\nGame Over\n")
        print("***** player " + player + " won *****")
        
    elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':#Check if the winning line across the bottom(1-2-3) is filled by the same player
        printBoard(theBoard)
        print("\nGame Over\n")
        print("***** player " + player + " won *****")
        
    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':#Check if the winning diagonal line (1-5-9) is filled by the same player
        printBoard(theBoard)
        print("\nGame Over\n")
        print("***** player " + player + " won *****")
        
    elif theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':#Check if the winning diagonal line (3-5-7) is filled by the same player
        printBoard(theBoard)
        print("\nGame Over\n")
        print("***** player " + player + " won *****")
        
    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':#Check if the winning line down left side (1-4-7) is filled by the same player
        printBoard(theBoard)
        print("\nGame Over\n")
        print("***** player " + player + " won *****")
        
    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':#Check if the winning line down middle (1-4-7) is filled by the same player
        printBoard(theBoard)
        print("\nGame Over\n")
        print("***** player " + player + " won *****")
        
    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':#Check if the winning line down right side(3-6-9) is filled by the same player
        printBoard(theBoard)
        print("\nGame Over\n")
        print("***** player " + player + " won *****")
        
def cleanBoard():
    for k in range(1,10):
            theBoard[str(k)] = ' '


def game():
    player='X'
    count = 0

    for _ in range(10):
        printBoard(theBoard)
        print("It's " + player + " turn. Choose a place to move: ")

        move = input()

        if theBoard[move] == ' ': #Put the player symbol to an empty place if there is one and change round.
            theBoard[move] = player
            count += 1
        else:
            print("Invalid move. Position occupied. Choose again.")
            continue
        
        if count >= 5: #Check for winner after 5 rounds have been played
            checkWinner(player)
            break

        if count == 9: #After 9 rounds with no winners the game is tie
            print("It's a Tie Game.")
            

        if player == "X":
            player = "O"
        else:
            player= "X"
    
    print("Do you want a rematch?(y/n)")
    ans = input()

    if ans =="y" or ans == "Y":
        cleanBoard()
        game()

if __name__ == "__main__":
    game()