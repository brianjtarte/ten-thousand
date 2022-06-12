from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker
import sys

class Game:
    """handles all the game logic, starts a round, rolls dice, ends a round, banks score, calculates shelf points
    """

    def __init__(self, max_rounds=10, dice=6):
        self.banker = Banker()
        self.max_rounds = max_rounds
        self.round = 0
        self.dice_qty = dice

    def play(self, roller=None):
        """method to start the game

        Args:
            roller (method/function, optional): the function or game logic that handles the dice rolling feature. Defaults to None.
            amt
        """
        roller = roller or GameLogic.roll_dice
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        play_game = input("> ")
        if play_game == "n":
            self.quit_game(play_game)
        elif play_game == "y":
            self.start_game(roller)
    @staticmethod
    def quit_game(quit_type, points=0):
        """Quit the game method
        """
        if quit_type == 'n':
            print("OK. Maybe another time")
        elif quit_type =='q':
            print(f"Thanks for playing. You earned {points} points")
            sys.exit()
        # else:
        #     print(f"Thanks for playing. You earned {points} points")

    def start_game(self, roller):
        """start the game with the current starting round and dice
        """
        # num_dice = 6
        self.round = self.round + 1
        print(f'Starting round {self.round}')
        self.start_round(self.dice_qty, roller)

    def start_round(self, num_dice, roller):
        """start a round 

        Args:
            num_dice (int): number of dice
            roller (function/method): the logic to roll the dice from an imported method
            amt
        """

        print(f'Rolling {num_dice} dice...')
        # dice_roll = ' '.join(str(dice) for dice in roller(num_dice))
        roll = roller(num_dice)
        dice_roll = ''
        for num in roll:
            dice_roll += str(num) + ' '
        print(f'*** {dice_roll}***')
        print("Enter dice to keep, or (q)uit:")

        keep_or_quit = input("> ")

        if keep_or_quit == "q":
            self.quit_game(keep_or_quit,self.banker.balance)
        elif keep_or_quit == "b":
            self.end_round(roller)
            # dont need this
        elif keep_or_quit == "r":
            pass



        else:
            saved_dice_list = [int(i) for i in keep_or_quit]
            dice_saved = len(saved_dice_list)

            score = GameLogic.calculate_score(saved_dice_list)
            self.shelf_round(score, dice_saved,num_dice,roller)
            

    def shelf_round(self,points,dice_saved,num_dice,roller):
        self.banker.shelf(points)
        print(f"You have {points} unbanked points and {num_dice-dice_saved} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        roll_bank_quit = input("> ")
        if roll_bank_quit == "b":
            self.end_round(roller)


    def end_round(self,roller):
        self.banker.bank()
        print(f"You banked {self.banker.balance} points in round {self.round}")
        print(f"Total score is {self.banker.balance} points")
        self.start_game(roller)

if __name__ == '__main__':
    game = Game()
    game.play()

