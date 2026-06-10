class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        ROWS, COLS = len(grid), len(grid[0])
        fresh, time = 0, 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1 

        while q and fresh > 0:
            for i in range(len(q)):
                r , c = q.popleft()
                for dr, dc in directions:
                    curR, curC = dr + r, dc + c
                    if (curR in range(ROWS) and 
                        curC in range(COLS) and 
                        grid[curR][curC] == 1):
                        grid[curR][curC] = 2
                        fresh -= 1
                        q.append((curR, curC))
            time += 1

        return time if fresh == 0 else -1

        