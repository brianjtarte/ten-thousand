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
        roller = roller or GameLogic.roll_dice
        # print(roller, "Line 22")
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        play_game = input("> ")
        if play_game == "n":
            # self.quit_game(play_game, self.banker.balance, self.round)
            self.quit_game(play_game)
        elif play_game == "y":
            self.start_game(roller)

    @staticmethod
    def quit_game(quit_type, points=0):
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
        list1 = ' '.join(str(dice) for dice in roller(num_dice))
        print(f'*** {list1} ***')
        print("Enter dice to keep, or (q)uit:")
        saved_dice = input("> ")
        self.user_choice(saved_dice, num_dice)


    def user_choice(self, saved_dice, num_dice):
        if saved_dice == "q":
            self.quit_game(saved_dice, self.banker.balance)
        elif saved_dice == "b":
            self.end_round()
        elif saved_dice == "r":
            pass

        else:
            saved_dice_list = tuple(map(int,saved_dice))
            # saved_dice_list = [int(i) for i in saved_dice]
            dice_saved = len(saved_dice_list)
#            print("dice saved: ", dice_saved, " saved: ", saved_dice_list)
#            roll_dice = str(roller(num_dice))
#            self.shelf_round(num_dice - dice_saved, roller)
            self.shelf_round(GameLogic.calculate_score(saved_dice_list),
                             dice_saved, num_dice)

    def shelf_round(self, points, dice_saved, num_dice):
        print(f"You have {points} unbanked points and "
              f"{num_dice - dice_saved} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        #saved_dice refers to user_response
        saved_dice = input("> ")
        self.user_choice(saved_dice,self.roller(num_dice),num_dice)


    def bank_points(self, points):
        self.banker.bank()
        print(f"You banked {points} points in round {self.round}")
        print(f"Total score is {self.banker.balance} points")


    def end_round(self):
        self.banker.bank()
        print(f"You banked {self.banker.balance} points in round {self.round}")


if __name__ == '__main__':
    game = Game()
    game.play()

