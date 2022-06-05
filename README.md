# Lab-06 Ten-Thousand

## Authors: Marni, Anthony H., Brendon, Brian

### Links & Resources:


### Feature Tasks/Requirements:
1. Focus on scoring,dice rolling, banking of points (Game logic)
2. Define appropriate classes
   1. GameLogic
      1. Methods:
         1. roll_dice (static)
         - [x] 1. Input of an int between 1-6 (number of dice)
         - [x] 2. Output is tuple with random values between 1-6 (value of dice)
         2. calculate_score (static)
            - [x] 1. Input is a tuple of integers that represent a dice roll
            - [x] 2. Output is an integer representing the roll's score according to the rules
   2. Banker
      1. Methods/Functions: 
         1. shelf (instance)
            - [x] 1. Temporarily store  unbanked points
         2. bank (instance)
            - [x] 1. Should add any points on the shelf to total and reset shelf to 0
            - [x] 2. Output should be the amount of points added to total from shelf
         3. clear_shelf (instance)
            - [x] 1. Should remove all unbanked points
### Initialize/Run Application:

### Tests
 - Running tests: 
   - pytest tests/test_calculate_score.py
   - pytest tests/test_banker.py
   - pytest tests/test_roll_dice.py
 
 - Tests of note: N/A
 - Tests not completed/skipped: N/A
