from os import system

'''
    Decorator.
        Clears console before executing a passed function
'''
def clear(fn):
    def wrapper(*args, **kwargs):
        system("clear")
        return fn(*args, **kwargs)

    return wrapper