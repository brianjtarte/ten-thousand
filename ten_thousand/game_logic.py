import random


# Define GameLogic class with roll_dice static method.
class GameLogic:
    ''' Game Logic: Contains the main methods for the game of calculating the score, rolling the dice, and banking. '''

    def __init__(self):
        pass

    @staticmethod
    def roll_dice(num_dice):
        die_value = random.randint(1, 6)
        print(die_value)


if __name__ == '__main__':
    GameLogic.roll_dice(1)
