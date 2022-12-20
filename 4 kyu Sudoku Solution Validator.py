def valid_solution(board):
    for i in range(len(board)):
        hadd = 0
        vadd = 0
        for j in range(len(board)):
            vadd += board[j][i]
            hadd += board[i][j]
            if board[i][j] < 1 or board[i][j] > 9:
                return False
        if vadd != 45 or hadd != 45:
            return False
    for i in range(3):
        for j in range(3):
            gadd = 0
            for k in range(3):
                for l in range(3):
                    gadd += board[i*3+k][j*3+l]
                    if board[i][j] < 1 or board[i][j] > 9:
                        return False
            if gadd != 45:
                return False
    return True 
    pass
