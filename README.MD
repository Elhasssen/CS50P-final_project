# __GAMES__
#### Video Demo:  <https://youtu.be/nxQ5QZf21pI>

## __Definition__
 This project is an interactive shell providing the user with three games.

 Project structure :
 - project.py
 - test_project.py
 - requirements.txt
 - README.md

## __Libraries__

__RANDOM__ : This module implements pseudo-random number generators for various distributions.. [(Readmore)](https://docs.python.org/3/library/random.html)

__ART__ : ASCII art is also known as "computer text art". It involves the smart placement of typed special characters or letters to make a visual shape that is spread over multiple lines of text.[(Readmore)](https://pypi.org/project/art/)

## **Installing Libraries**
there is a a requirements.txt file that has all the libraries used.

and simply can be install by this pip command:

```pip install -r requirements.txt```

## __Usage__

```python project.py```
```
  ____     _     __  __  _____  ____   _ 
 / ___|   / \   |  \/  || ____|/ ___| | |
| |  _   / _ \  | |\/| ||  _|  \___ \ | |
| |_| | / ___ \ | |  | || |___  ___) ||_|
 \____|/_/   \_\|_|  |_||_____||____/ (_)


Welcome to games :), If you want to exit press CTRL + C
Select a game :
- 1 for TicTactoe
- 2 for Magic 8 Ball
- 3 for Rock Paper Scissors ``` 
```
After that the user can select a game 1 ,2 , or 3. and has the ability to Exit at any time using CTRL + C.
```
Tic Tac Toe started!

 | |    1 2 3
-----
 | |    4 5 6
-----
 | |    7 8 9
X Role to play? 2
 |X|    1 2 3
-----
 | |    4 5 6
-----
 | |    7 8 9
```
when he finished he will be promoted to keep playing or abort.
```
Do you want to carry on playing y/n? 
```
## __Functioning__

the project.py contains 12 functions including the main function.

### __getGame()__ __function__ :
This function simply prompt the user and allowing him to select which game he wants to play, the function also has exception handling if the user put a string or an integer that differs from the range of the proposed games.

### **Rock Paper Scissors game (2 Functions)**:
#### __is_win(arg1,arg2)__ __function__ : this function takes two arguments, player1 and player2 where the arguments have values like 'r' for rock, 's' for scissors, and 'p' for paper.
the function does test where it compares the two values and return a boolean true if the rules of the game has been applied  p > r, r > s, and s > p and if the didn't happen it will return false.
#### __RockPaperScissors()__ function :
this function take no argument instead it makes a random guess between three values (r,p,s) which is the computer guess and takes the user input and compare it using __is_win(computer,player)__ function, finaly it will print a certain message if user has won, lost or drew.
### **Magic 8 Ball game (1 Function)**:
#### **MagicBall()** function: 
This function takes no arguments, it randomize a number out of the range from 1 to 9 and outputs a certain message corressponding that random guess.
### **Tic Tac Toe game (7 functions)** :
#### **DefineBoard() function** :
This function simply returns a dictionarry containing keys from 1 to 9 with empty values which is a basic Tic Tac Toe board.
#### **DisplayBoard() function** :
This function displays the previous created board in the screen in a more board like manner.
#### **UpdateBoard(arg1,arg2,arg3) function** : 
This function takes two arguments the board, the player and the position, the position value is provided by user which the player when making a play whether it was the 'X' or 'O' player. so the board simply update a key value by 'X' or 'O'.
#### **CheckSpot(arg1,arg2) function** :
This function takes two arguments, the board and the position and checks whether the spot or the value of a key is empty by comparing it to a blank string which is ' '.
#### **checkFullBoard(board) function :**
This function simply takes the board dictionaty and iterating overiting while applying condition if that value is empty or not. This function return True or False.
#### **Winner(arg1,arg2) function :**
This function two arguments, board and the player ('X' or 'O') and start comparing between the recent player and the values of the keys horizontally and vertically and diagonaly following the Tic Tac Toe rules.
#### **TicTacToe() function**:
This function call all the previous functions seperately first of all it delcares a new board, the current player ('X') and the next player ('O'). then there is a infinite loop that breaks whenever a particular condition is provided, Exception are handled by a message when the user inputs a postition that differes from the board values which ranges from 1-9. After it the **CheckSpot()** function to tell if the value of position (key) is empty or not, after that the board will be updated using **UpdateBoard(board, currentPlayer, position)** after the current player and the board get passed to the function **Winner(board,currentPlayer)** to detect who won or not, finnaly we check if the board is full or not using **checkFullBoard** function if it is full and there is no winner the game stops and print 'game over', the value of the current play and the next player get switched.
### Author : ElHassen Boumeddiene.