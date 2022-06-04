import random


# Define GameLogic class with roll_dice static method.
class GameLogic:
    ''' Game Logic: Contains the main methods for the game of calculating the score, rolling the dice, and banking. '''

    def __init__(self):
        pass

    @staticmethod
    def roll_dice(num_dice):
        # list = []
        # for num in range(1,num_dice +1):
        #     die_value = random.randint(1, 6)
        #     list.append(die_value)
        # return list
        return tuple(random.randint(1,6) for die in range(0,num_dice))


if __name__ == '__main__':
    # GameLogic.roll_dice(2)
    print(GameLogic.roll_dice(2))
