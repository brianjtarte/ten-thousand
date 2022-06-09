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
        self.roller = roller or GameLogic.roll_dice
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        play_game = input("> ")
        if play_game == "n":
            print("OK. Maybe another time")
        elif play_game == "y":
            self.start_round(self.round, self.roller)

    def start_round(self, round, roller):
        round += 1
        dice = 6
        print(f'Starting round {round}')
        while True:
            print(f'Rolling {dice} dice...')
            """
                First test is passing, attempting to print the dice rolled
            """
            print(roller(GameLogic.roll_dice(dice)))
        #     print("*** 4 4 5 2 3 1 ***")
        #     print("Enter dice to keep, or (q)uit:")
        #     quit_game = input("> ")
        #     if quit_game == "q":
        #         print("Thanks for playing. You earned 0 points")
        #         return
        #     elif quit_game != "q":
        #         print("Starting round 1")
        #         print("Rolling 6 dice...")
        #         print("*** 4 2 6 4 6 5 ***")
        #         print("Enter dice to keep, or (q)uit:")
        #         keep_dice = input("> ")
        #         if keep_dice != "q":
        #             print("You have 50 unbanked points and 5 dice remaining")
        #             print("(r)oll again, (b)ank your points or (q)uit:")
        #             bank_or_roll = input("> ")
        #         if bank_or_roll == "b":
        #             print("You banked 50 points in round 1")
        #             print("Total score is 50 points")
        #             print("Starting round 2")
        #             print("Rolling 6 dice...")
        #             print("*** 6 4 5 2 3 1 ***")
        #             print("Enter dice to keep, or (q)uit:")
        #             quit_round = input("> ")
        #             if quit_round == "q":
        #                 print("Thanks for playing. You earned 50 points")


#
# if __name__ == '__main__':
#     game = Game()
#
