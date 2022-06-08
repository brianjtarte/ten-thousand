# Lab-06 Ten-Thousand

## Authors: Marni, Anthony H., Brendon, Brian

### Links & Resources:
[Farkle example](http://www.playonlinedicegames.com/farkle)



### Feature Tasks: Ten Thousand 1
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

### Feature Tasks: Ten Thousand 2
1. Focus Game simulation
   1. GameLogic
      1. Methods:
         1. roll_dice (static)
            - [] 1. should simulate rolling between 1 and 6 dice
            - [] 2. Should allow user to set aside dice each roll
         2. calculate_score (static)
            - [] 1. Application Should allow banking of current score or allow rolling again
            - [] 2. Application Should keep track of total score
         3. Misc Features:
            - [] 1. Application should keep track of current round
            - [] 2. Have automated Tests to ensure proper operation


### Initialize/Run Application:

6/7/2022
- Not Applicable, no full game implementation, only dice rolling. 

### Tests
 - Running tests: 
   - pytest tests/test_calculate_score.py
   - pytest tests/test_banker.py
   - pytest tests/test_roll_dice.py
 
 - Tests of note: N/A
 - Tests not completed/skipped: N/A
