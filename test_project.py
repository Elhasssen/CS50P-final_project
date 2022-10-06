from project import getGame, RockPaperScissors, is_win,MagicBall,TicTacToe,DefineBoard, UpdateBoard, CheckSpot, checkFullBoard, Winner, DisplayBoard


def test_getGame():
    assert getGame() == None


def test_is_win():
    assert is_win('r', 's') == True
    assert is_win('s', 'p') == True
    assert is_win('p', 'r') == True
    assert is_win('r','r') == None
    assert is_win('p', 's') == None

def test_MagicBall(capfd):
    MagicBall()
    out, err = capfd.readouterr()
    assert out == 'Magic 8 Ball says : It is certain' or 'Magic 8 Ball says : It is decidedly so' or 'Magic 8 Ball says : Yes' or 'Magic 8 Ball says : Reply hazy try again' or 'Magic 8 Ball says : Ask again later' or 'Magic 8 Ball says : Concentrate and ask again' or 'Magic 8 Ball says : My reply is no' or 'Magic 8 Ball says : Outlook not so good' or 'Magic 8 Ball says : Very doubtful'

def test_DefineBoard():
    assert DefineBoard() == {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}



def test_DisplayBoard():
    board = DefineBoard()
    assert DisplayBoard(board) == f"{board[1]}|{board[2]}|{board[3]}   1 2 3\n-----\n{board[4]}|{board[5]}|{board[6]}   4 5 6\n-----\n{board[7]}|{board[8]}|{board[9]}   7 8 9"



def test_UpdateBoard():
    board = DefineBoard()
    player = 'X'
    position = 2
    UpdateBoard(board, player, position)
    assert board == {1: ' ', 2: 'X', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}


def test_CheckSpot():
    board = DefineBoard()
    player = 'X'
    position = 2
    UpdateBoard(board, player, position)
    assert CheckSpot(board, 2) == False
    assert CheckSpot(board, 4) == True


def test_Winner():
    board = {1: 'X', 2: 'X', 3: 'X', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    assert Winner(board, 'X') == True
    board = {1: 'X', 2: 'X', 3: 'O', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    assert Winner(board, 'X') == False
    board = {1: 'X', 2: 'X', 3: 'O', 4: 'X', 5: 'O', 6: 'X', 7: 'O', 8: ' ', 9: ' '}
    assert Winner(board, 'O') == True
    board = {1: 'X', 2: 'X', 3: 'X', 4: '', 5: ' ', 6: 'X', 7: ' ', 8: ' ', 9: 'X'}
    assert Winner(board, 'X') == True

def test_checkFullBoard():
    board = {1: 'X', 2: 'X', 3: 'X', 4: '', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    assert checkFullBoard(board) == False
    board = {1: 'X', 2: 'X', 3: 'X', 4: 'O', 5: 'X', 6: 'O', 7: 'X', 8: 'O', 9: 'X'}
    assert checkFullBoard(board) == True



    