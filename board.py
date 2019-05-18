class Board():
    def __init__(self):
        self.board = [" "] * 9

    def get_as_list(self):
        return self.board

    def put(self, symbol, position):
        self.board[position - 1] = symbol

    def has_empty_cells(self):
        return len([c for c in self.board if c == " "]) > 0

    def is_empty_cell(self, id):
        return self.board[id] == " "