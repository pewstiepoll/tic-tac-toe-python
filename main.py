from console_printer import Printer
from game import Game

'''
Simple Tic-Tac-Toe console game implementation
'''
if __name__ == "__main__":
    # Create a new game instance and specify the Printer to be used
    game = Game(Printer)

    # Start the game
    game.run()