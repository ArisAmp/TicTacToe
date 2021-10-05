import random

#Parent Class
class Player():
    def __init__(self, symbol) -> None:
        self.symbol = symbol
    
    def get_move(self, game): #every player can get their next move given a game
        pass

#Child class Computer
class ComputerPlayer(Player):
    def __init__(self, symbol) -> None:
        super().__init__(symbol)
    
    def get_move(self, game):
        print("\n" + self.symbol + "\'s turn. Input move (1-9): ")
        move = random.choice(game.available_moves())
        return move

#Child class Human
class HumanPlayer(Player):
    def __init__(self, symbol) -> None:
        super().__init__(symbol)
    
    def get_move(self, game):
        valid = False
        
        while not valid:
            move = input("\n" + self.symbol + "\'s turn. Input move (1-9): ")
            try:
                if move not in game.available_moves():
                    raise ValueError
                valid = True
            except:
                print("Invalid move. Try again.")
        return move
            