import random
import art


def main():
    while True:
        print(art.text2art('GAMES!'))
        game = getGame()
        if game == 1 :
            TicTacToe()
        elif game == 2 :
            MagicBall()
        elif game == 3 :
            RockPaperScissors()
        else:
            continue
        request = input('Do you want to carry on playing y/n? ').upper()
        if request in ['NO','N']:
            break

def getGame():
    try :        
        n = int(input('Welcome to games :), If you want to exit press CTRL + C\nSelect a game :\n- 1 for TicTactoe\n- 2 for Magic 8 Ball\n- 3 for Rock Paper Scissors\nAnswer: '))
        if n not in [1,2,3]:
            raise Exception()
    except (ValueError,Exception):
        print('please Enter a Value 1 or 2')
        
    else : 
        return n

def RockPaperScissors():
    print('Welcome to Rock Paper scissors')
    user = input("'r' for rock, 's' for scissors, 'p' for paper\n")
    computer = random.choice(['r','p','s'])


    if user == computer:
        print('You tied!')
    elif is_win(user, computer):
        print('You won!')
    else:
        print('You lost!')
    




def is_win(player, player2):
    if (player == 'r' and player2 == 's') or (player == 's' and player2 == 'p') or (player == 'p' and player2 == 'r'):
        return True

def MagicBall():
    answerNumber = random.randint(1, 9)
    if answerNumber == 1:
        print('Magic 8 Ball says : It is certain')
    elif answerNumber == 2:
        print('Magic 8 Ball says : It is decidedly so')
    elif answerNumber == 3: 
        print('Magic 8 Ball says : Yes')
    elif answerNumber == 4: 
        print('Magic 8 Ball says : Reply hazy try again')
    elif answerNumber == 5: 
        print('Magic 8 Ball says : Ask again later')
    elif answerNumber == 6: 
        print('Magic 8 Ball says : Concentrate and ask again')
    elif answerNumber == 7:
        print('Magic 8 Ball says : My reply is no')
    elif answerNumber == 8:
        print('Magic 8 Ball says : Outlook not so good')
    elif answerNumber == 9:
        print('Magic 8 Ball says : Very doubtful')





def TicTacToe():
    print('Tic Tac Toe started!')
    board = DefineBoard()
    currentPlayer, nextPlayer = 'X', 'O'
    while True:
        try:
            print(DisplayBoard(board))
            position = input(f'{currentPlayer} Role to play? ')
            if CheckSpot(board, position) == True :
                UpdateBoard(board, currentPlayer, position)
                if Winner(board, currentPlayer) == True :
                    print(DisplayBoard(board))
                    print(f"{currentPlayer} has won the game.")
                    break
                if checkFullBoard(board) == True:
                    print(DisplayBoard(board))
                    print('Game Over!')
                    break
                currentPlayer, nextPlayer = nextPlayer, currentPlayer
            else :
                continue
        except (ValueError,KeyError):
            print("Enter a Value between 1 and 9.")               

        
def DefineBoard():
    board = {1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '}
    return board
def UpdateBoard(board, player, position):
    board[int(position)] = player

def CheckSpot(board,position):
    if board[int(position)] == ' ':
        return True
    else: 
        return False
def Winner(board,player):
    if board[1] == board[2] == board[3] == player:
        return True
    elif board[4] == board[5] == board[6] == player:
        return True
    elif board[7] == board[8] == board[9] == player:
        return True
    elif board[1] == board[4] == board[7] == player:
        return True
    elif board[2] == board[5] == board[8] == player:
        return True
    elif board[3] == board[6] == board[9] == player:
        return True
    elif board[1] == board[5] == board[9] == player:
        return True
    elif board[3] == board[5] == board[7] == player:
        return True
    else : 
        return False


def checkFullBoard(board):
    for value in board.values():
        if value == ' ':
            return False
        else :
            continue
    return True
def DisplayBoard(board):
    return f'{board[1]}|{board[2]}|{board[3]}   1 2 3\n-----\n{board[4]}|{board[5]}|{board[6]}   4 5 6\n-----\n{board[7]}|{board[8]}|{board[9]}   7 8 9'




if __name__ == "__main__" :
    main()