# Lab-07 Ten-Thousand II

## Authors: Marni, Anthony H., Brendon, Brian

### Links & Resources:
[Farkle example](http://www.playonlinedicegames.com/farkle)
[Python| Converting all strings in list to integers](https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/)


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
            - [x] 1. should simulate rolling between 1 and 6 dice
            - [] 2. Should allow user to set aside dice each roll
         2. calculate_score (static)
            - [] 1. Application Should allow banking of current score or allow rolling again
            - [] 2. Application Should keep track of total score
         3. Misc Features:
            - [] 1. Application should keep track of current round
            - [] 2. Have automated Tests to ensure proper operation

### Feature Tasks: Ten Thousand 3
1. Focus Added Features 
   1. Implement features from Lab I and Lab II
     - [x] 1. should handle setting aside scoring dice and continue turn 
              with remaining dice
     - [] 2. should handle when cheating occurs or checks for typos
   2. Should allow user to:
      - [] 1. continue rolling with 6 new dice when all dice 
         have scored with HOT DICE
   3. Should handle ZILCH
     - [] 1. No points for round and round is over


### Initialize/Run Application:

6/9/2022
- Not Applicable, no full game implementation, only dice rolling. 

### Tests
 - Running tests: 
   - pytest test/version_1 (this test all version one tests from the first part of the lab)
   - pytest test/version_2 (this tests all verion two tests from the second part of the lab)
 
 - Tests of note: N/A
 - Tests not completed/skipped: We only have the first two tests passing at the moment, and are struggling to bank points, which is causing the subsequent tests to fail.

### Other Notes:
1. Technical difficulties again prevented equal driving among all team 
   members. (06/11/22)
2. Long periods trying to troubleshoot with TAs and Instructor that brought 
   us back to where we were on 6/9/22. (6/11/22)
3. Managed to get a bit further along on Lab II, but still not able to pass 
   the "bank_one_roll_then_quit" test. (06/11/22)