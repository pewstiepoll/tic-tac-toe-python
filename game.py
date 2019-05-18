from board import Board
from player import Player

class Game():
    symbols = ["X", "O"]

    def __init__(self, printer):
        self.printer = printer
        self.players = []
        self.current_player = None
        self.board = Board()

    def get_next_turn(self):
        turn = ""

        while turn not in range(1, 10):
            try:
                turn = int(input(f"{self.current_player.name}'s turn. Enter number [1-9]: "))
                if self.board.get_as_list()[turn - 1] != " ":
                    turn = ""
            except:
                continue

        return turn

    def get_symbol(self, prompt):
        result = ""

        while result.upper() not in Game.symbols:
            result = self.printer.input(prompt).upper()

        return result

    '''
        Based on a given symbol returns the opposite one
    '''
    def get_opposite_symbol(self, symbol):
        if symbol in Game.symbols:
            return "X" if symbol == "O" else "O"

    '''
        Switches current user to the opposite one
    '''
    def switch_current_player(self):
        # if first player is selected
        if self.current_player.id == 0:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    '''
        Checks every row, col and diagonal to detect whether there's a winner
    '''
    def has_winner(self):
        board_list = self.board.get_as_list()
        # check each row
        if (board_list[0] == board_list[1] == board_list[2] == self.current_player.symbol 
            or 
            board_list[3] == board_list[4] == board_list[5] == self.current_player.symbol
            or
            board_list[6] == board_list[7] == board_list[8] == self.current_player.symbol
            ):
            return True

        # check each column
        if (board_list[0] == board_list[3] == board_list[6] == self.current_player.symbol 
            or 
            board_list[1] == board_list[4] == board_list[7] == self.current_player.symbol
            or board_list[2] == board_list[5] == board_list[8] == self.current_player.symbol
            ):
            return True

        # check each diagonal
        if (board_list[0] == board_list[4] == board_list[8] == self.current_player.symbol 
            or 
            board_list[2] == board_list[4] == board_list[6] == self.current_player.symbol
            ):
            return True

        return False

    '''
        Main function:
            1. Creates two players.
            2. Inits the board.
            3. Starts the game
    '''
    def run(self):
        # Get first player name
        name = self.printer.input("Player1 enter your name: ")
        # Get first player symbol
        symbol = self.get_symbol(f"{name} enter your symbol [X/O]: ")
        # Create a player object for the first
        self.players.append(Player(0, name, symbol))
        # Get second player name
        name = self.printer.input("Player2 enter your name: ")
        # Assign the only symbol left to the second player
        symbol = self.get_opposite_symbol(symbol)
        # Create a player object for the second player
        self.players.append(Player(1, name, symbol))

        # Get player with Game.symbols[0] symbol to start
        self.current_player = next((player for player in self.players if player.symbol == Game.symbols[0]))

        # while board is not full
        while self.board.has_empty_cells():
            # draw the board
            self.printer.print_board(self.board)
            # wait for current player to press button 1-9 and put current turn on the board
            self.board.put(self.current_player.symbol, self.get_next_turn())
            # redraw the board
            self.printer.print_board(self.board)
            # check if there's a win
            if self.has_winner():
                print(f"{self.current_player.name} has won!")
                break
            # switch players
            self.switch_current_player()

        # if there was no winner
        if not self.has_winner():
            print("It's a tie!")
