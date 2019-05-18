from helpers import clear

'''
Helper class. Prints to console
'''
class Printer():

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