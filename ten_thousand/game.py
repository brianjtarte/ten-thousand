from lib2to3.pgen2.token import GREATER, LESS
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
        self.roller = GameLogic.roll_dice
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        play_game = input("> ")
        if play_game == "n":
            self.quit_game(play_game,self.banker.bank, self.round)
        elif play_game == "y":
            self.start_game()

    
    def quit_game(self,quit_type, points, round ):
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
        self.round = self.round +1
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
        string = '*** 4 4 5 2 3 1 ***'
        print(string)
        print("Enter dice to keep, or (q)uit:")
        


        # for dice in self.roller(num_dice):
        #     string = + string + ' ' + str(dice)
        


        



        

    # def play(self, roller=None):
    #     self.roller = roller or GameLogic.roll_dice
    #     print("Welcome to Ten Thousand")
    #     print("(y)es to play or (n)o to decline")
    #     play_game = input("> ")
    #     if play_game == "n":
    #         print("OK. Maybe another time")
        # elif play_game == "y":
        #     self.start_round(self.round, self.roller)

    # def start_round(self, round, roller):
    #     round += 1
    #     dice = 6
    #     print(f'Starting round {round}')
    #     while True:
    #         print(f'Rolling {dice} dice...')
            
    #         print(roller(GameLogic.roll_dice(dice)))
    #         return


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


if __name__ == '__main__':
    game = Game()
    game.start_round()
