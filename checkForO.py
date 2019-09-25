def check_o(board):
    if(board[9]==board[8]==board[7]=='O' or
       board[4]==board[5]==board[6]=='O' or
       board[1]==board[2]==board[3]=='O' or 
       board[9]==board[4]==board[1]=='O' or
       board[8]==board[5]==board[2]=='O' or
       board[7]==board[6]==board[3]=='O' or
       board[9]==board[5]==board[3]=='O' or
       board[7]==board[5]==board[1]=='O' ):
        return True
    else:
        return False