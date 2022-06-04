# Lab-06 Ten-Thousand

## Authors: Marni, Anthony, Brendon, Brian

### Links & Resources:


### Feature Tasks/Requirements:
1. Focus on scoring,dice rolling, banking of points (Game logic)
2. Define appropriate classes
   1. GameLogic
      1. Methods:
         1. roll_dice (static)
            1. Input of an int between 1-6 (number of dice)
            2. Output is tuple with random values between 1-6 (value of dice)
         2. calculate_score (static)
            1. Input is a tuple of integers that represent a dice roll
            2. Output is an integer representing the roll's score according to the rules
   2. Banker
      1. Methods/Functions: 
         1. shelf (instance)
            1. Temporarily store  unbanked points
         2. bank (instance)
            1. Should add any points on the shelf to total and reset shelf to 0
            2. Output should be the amount of points added to total from shelf
         3. clear_shelf (instance)
            1. Should remove all unbanked points
### Initialize/Run Application:

### Tests
 - Running tests:
 - Tests of note:
 - Tests not completed/skipped:
