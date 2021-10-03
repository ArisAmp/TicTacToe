theBoard = {'1': ' ', '2': ' ', '3': ' ',\
            '4' :' ', '5': ' ', '6': ' ',\
            '7': ' ', '8':' ', '9':' '}

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print("-+-+-")
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print("-+-+-")
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():
    player='X'
    count = 0

    for _ in range(10):
        printBoard(theBoard)
        print("It's " + player + " turn. Choose a place to move: ")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = player
            count += 1
        else:
            print("Invalid move. Position occupied. Choose again.")
            continue
        
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over\n")
                print("***** player " + player + " won *****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("\nGame Over\n")
                print("***** player " + player + " won *****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over\n")
                print("***** player " + player + " won *****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over\n")
                print("***** player " + player + " won *****")
                break
            elif theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("\nGame Over\n")
                print("***** player " + player + " won *****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("\nGame Over\n")
                print("***** player " + player + " won *****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print("\nGame Over\n")
                print("***** player " + player + " won *****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over\n")
                print("***** player " + player + " won *****")
                break

        if count == 9:
            print("It's a Tie Game.")
            break

        if player == "X":
            player = "O"
        else:
            player= "X"
    print("Do you want a rematch?(y/n)")
    ans = input()
    if ans =="y" or ans == "Y":
        for k in range(1,10):
            theBoard[str(k)] = ' '
        game()

if __name__ == "__main__":
    game()