import random
from collections import Counter

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
        roll = tuple(random.randint(1,6) for die in range(0,num_dice))
        
        return roll



    @staticmethod 
    def calculate_score(roll):
        score = 0
        count = Counter(roll).most_common()
        print(count)

        num = len(count)

        for num in range(0,len(count)):
            print (count[num][0], count[num][1])

            if count[num][0] == 1:
                score += 50 * count[num][1]

        # if roll[0] == 1 and roll[1] <=2:
        #     score = score + 100 * roll[1]

        # elif roll[0] == 1 and roll[1] >=3:
        #     score = score + 1000 * roll[1]

        # elif roll[0] == 5:
        #     score = score + 50

        return count, score
        # score = 0
        # if roll is None:
        #     roll = [0]


        
        

if __name__ == '__main__':
    # GameLogic.roll_dice(2)
    # print(GameLogic.roll_dice(2))
    print(GameLogic.calculate_score(GameLogic.roll_dice(5)))