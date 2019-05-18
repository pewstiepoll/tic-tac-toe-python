from helpers import clear

'''
    Abstract class:
        Abstracts logic for all printers
'''

class Printer():
    @staticmethod
    def print_board(board):
        raise TypeError("Called method on abstract class")
    
    @staticmethod
    def print():
        raise TypeError("Called method on abstract class")

    @staticmethod
    def input():
        raise TypeError("Called method on abstract class")

'''
    Printer that use console as a main io
'''
class ConsolePrinter(Printer):

    @staticmethod
    @clear
    def print_board(board):
        list = board.get_as_list()

        print("-------------")
        print(f"| {list[0]} | {list[1]} | {list[2]} |")
        print("-------------")
        print(f"| {list[3]} | {list[4]} | {list[5]} |")
        print("-------------")
        print(f"| {list[6]} | {list[7]} | {list[8]} |")
        print("-------------")

    @staticmethod
    @clear
    def print(content):
        print(content)

    @staticmethod
    @clear
    def input(prompt):
        return input(prompt)