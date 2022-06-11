from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class Game:
    """handles all the game logic, starts a round, rolls dice, ends a round, banks score, calculates shelf points
    """

    def __init__(self, max_rounds=10):
        self.banker = Banker()
        self.max_rounds = max_rounds
        self.round = 0

    def play(self, roller=None):
        """method to start the game

        Args:
            roller (method/function, optional): the function or game logic that handles the dice rolling feature. Defaults to None.
            amt
        """
        print(roller)
        roller = roller or GameLogic.roll_dice
        print(roller, "Line 22")
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        play_game = input("> ")
        if play_game == "n":
            self.quit_game(play_game, self.banker.balance, self.round)
        elif play_game == "y":
            self.start_game(roller)

    def quit_game(self, quit_type, points, dice):
        """Quit the game method
        """
        if quit_type == 'n':
            print("OK. Maybe another time")
        else:
            print(f"Thanks for playing. You earned {points} points")

    def start_game(self, roller):
        """start the game with the current starting round and dice
        """
        num_dice = 6
        self.round = self.round + 1
        print(f'Starting round {self.round}')
        self.start_round(num_dice, roller)

    def start_round(self, num_dice, roller):
        """start a round 

        Args:
            num_dice (int): number of dice
            roller (function/method): the logic to roll the dice from an imported method
            amt
        """
        # initialize an empty string
        print(f'Rolling {num_dice} dice...')
        # change the tring to the concatenation string with the for loop
        # string = '*** 4 4 5 2 3 1 ***'
        list1 = ' '.join(str(dice) for dice in roller(num_dice))
        # list1 = '*** 4 4 5 2 3 1 ***'
        print(f'*** {list1} ***')
        print("Enter dice to keep, or (q)uit:")
        roll_dice = input("> ")

        if not int(roll_dice):
            if roll_dice == "q":
                self.quit_game(roll_dice, self.banker.balance, self.round)
            else:
                self.end_round()
        else:

            dice_saved = len(roll_dice)
            roll_dice = str(roller(num_dice))
            self.shelf_round(num_dice - dice_saved, roller)

    def shelf_round(self, num_dice, roller):

        shelf_banker = roller(num_dice)

        self.banker.shelf(shelf_banker)

        print(f"You have {self.banker.shelved} unbanked points and {num_dice} dice remaining")

    def end_round(self):
        self.banker.bank()
        print(f"You banked {self.banker.balance} points in round {self.round}")


if __name__ == '__main__':
    game = Game()
    game.play()

