#Time Complexity: O(n*m)
#Space Complexity: O(1)
#Did it run on leetcode: Yes

def numIslands(self, grid: List[List[str]]) -> int:
        def is_valid(i, j):
            return True if 0 <= i < len_row and 0 <= j < len_col and grid[i][j] == "1" else False
                
        len_row, len_col = len(grid), len(grid[0])
        island_count = 0
        for row in range(len_row):
            for col in range(len_col):
                if is_valid(row, col):
                    island_count += 1
                    queue = deque([(row, col)])
                    while len(queue) != 0:
                        r, c = queue.popleft()
                        if grid[r][c] == "1":
                            grid[r][c] = "0"
                            for r_move, c_move in ((-1,0),(1,0),(0,1),(0,-1)):
                                if is_valid(r + r_move, c + c_move):
                                    queue.append((r + r_move, c + c_move))

        return island_count