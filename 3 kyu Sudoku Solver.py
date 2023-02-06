def sudoku(puzzle):
    def find_empty_cell():
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == 0:
                    return (row, col)
        return None

    def is_valid(num, row, col):
        for i in range(9):
            if puzzle[row][i] == num or puzzle[i][col] == num:
                return False
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if puzzle[row_start + i][col_start + j] == num:
                    return False
        return True

    def solve():
        empty_cell = find_empty_cell()
        if not empty_cell:
            return True
        row, col = empty_cell
        for num in range(1, 10):
            if is_valid(num, row, col):
                puzzle[row][col] = num
                if solve():
                    return True
                puzzle[row][col] = 0
        return False

    solve()
    return puzzle



