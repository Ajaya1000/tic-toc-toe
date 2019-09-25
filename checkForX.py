def check_x(board):
    if(board[9]==board[8]==board[7]=='X' or
       board[4]==board[5]==board[6]=='X' or
       board[1]==board[2]==board[3]=='X' or 
       board[9]==board[4]==board[1]=='X' or
       board[8]==board[5]==board[2]=='X' or
       board[7]==board[6]==board[3]=='X' or
       board[9]==board[5]==board[3]=='X' or
       board[7]==board[5]==board[1]=='X' ):
            return True
    else:
        return False