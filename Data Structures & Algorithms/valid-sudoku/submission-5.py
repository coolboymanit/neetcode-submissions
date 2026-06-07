class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = set()
        col_sets = [set() for _ in range(9)]
        square_sets = [set() for _ in range(3)]

        for i in range(9):
            row_set.clear()
            if i%3 == 0: 
                for s in square_sets:
                    s.clear()
            for j in range(9):
                box_no = j//3
                row_no = i
                col_no = j
                val = board[i][j]
                print(f"Box: {box_no}, Row: {row_no}, Col: {col_no}, Val: {val}")

                if val == '.' or not (val in row_set or val in col_sets[col_no] or val in square_sets[box_no]):
                    square_sets[box_no].add(val)
                    col_sets[col_no].add(val)
                    row_set.add(val)
                
                else:
                    return False

        return True

        