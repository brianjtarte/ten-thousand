from ten_thousand.game_logic import GameLogic
from ten_thousand.game_logic import Banker


class Game:
    """hadles all the game logic, starts a round, rolls dice, ends a round, banks score, calculates shelf points
    """

    def __init__(self, max_rounds=10):
        self.banker = Banker()
        self.max_rounds = max_rounds
        self.round = 0

    def play(self, roller=None):
        """method to start the game

        Args:
            roller (method/function, optional): the function or game logic that handles the dice rolling feature. Defaults to None.
        """
        num_dice = 6
        self.roller = roller or GameLogic.roll_dice
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        play_game = input("> ")
        if play_game == "n":
            self.quit_game(play_game, self.banker.balance, self.round)
        elif play_game == "y":
            self.start_game()

    def quit_game(self, quit_type, points, dice):
        """Quit the game method
        """
        if quit_type == 'n':
            print("OK. Maybe another time")
        else:
            print(f"Thanks for playing. You earned {points} points")

    def start_game(self):
        """start the game with the current starting round and dice
        """
        num_dice = 6
        self.round = self.round + 1
        print(f'Starting round {self.round}')
        self.start_round(num_dice)

    def start_round(self, num_dice):
        """start a round 

        Args:
            num_dice (int): number of dice
            roller (function/method): the logic to roll the dice from an imported method
        """
        # initialize an empty string
        print(f'Rolling {num_dice} dice...')
        # change the tring to the concatenation string with the for loop
        # string = '*** 4 4 5 2 3 1 ***'
        list = ' '.join(str(dice) for dice in self.roller(num_dice))
        print(f"*** {list} ***")
        print("Enter dice to keep, or (q)uit:")
        roll_dice = input("> ")
        if roll_dice == "q":
            self.quit_game(roll_dice, self.banker.balance, self.round)
        else:
            self.end_round()



    def end_round(self):
        self.banker.shelf(50)
        print(f"You banked {self.banker.shelved} points in round {self.round}")


if __name__ == '__main__':
    game = Game()
    game.start_round()
