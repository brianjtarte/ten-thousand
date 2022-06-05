import random
from collections import Counter

# Define GameLogic class with roll_dice static method.
class GameLogic:
    ''' Game Logic: Contains the main methods for the game of calculating the score, rolling the dice, and banking. '''

    def __init__(self):
        pass

    @staticmethod
    def roll_dice(num_dice):
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
            #  ones
            if count[num][0] == 1 and count[num][1] <= 2:
                score += 100 * count[num][1]
                print(score)

            if count[num][0] == 1 and count[num][1] > 2:
                score += 1000 * (count[num][1] - 2)
                print(score)
            # twos
            if count[num][0] == 1 and count[num][1] >= 3:
                score += 200 * (count[num][1] - 2)
            # threes
            if count[num][0] == 1 and count[num][1] >= 3:
                score += 300 * (count[num][1] - 2)
            # fours
            if count[num][0] == 1 and count[num][1] >= 3:
                score += 400 * (count[num][1] - 2)
            # fives
            if count[num][0] == 1 and count[num][1] <= 2:
                score += 50 * (count[num][1] - 2)
                print(score)

            if count[num][0] == 1 and count[num][1] > 2:
                score += 500 * (count[num][1] - 2)
                print(score)
            # sixes
            if count[num][0] == 1 and count[num][1] >= 3:
                score += 600 * (count[num][1] - 2)
            # three pair
            # streight
            # 2 triples

        return count, score
        
if __name__ == '__main__':
    print(GameLogic.calculate_score(GameLogic.roll_dice(5)))