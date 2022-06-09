from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class Game:
    """
    Need Banker, dice, scores, number of rounds in game (track rounds),
    """

    def __init__(self, max_rounds=10):
        self.banker = Banker()
        self.max_rounds = max_rounds
        self.round = 0

    def play(self, roller=None):
        self.roller = roller
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        play_game = input("> ")
        if play_game == "n":
            print("OK. Maybe another time")
        elif play_game == "y":
            print("Starting round 1")
            print("Rolling 6 dice...")
            print("*** 4 4 5 2 3 1 ***")
            print("Enter dice to keep, or (q)uit:")
            quit_game = input("> ")
            if quit_game == "q":
                print("Thanks for playing. You earned 0 points")




