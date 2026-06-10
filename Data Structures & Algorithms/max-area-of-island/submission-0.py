class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r,c):
            q = collections.deque()
            grid[r][c] = 0
            q.append((r,c))
            res = 1

            while q:
                poppedr,poppedc = q.popleft()
                for dr, dc in directions:
                    nr, nc = poppedr + dr, poppedc + dc
                    if (nr in range(rows) and 
                        nc in range(cols) and 
                        grid[nr][nc] == 1):
                        q.append((nr,nc))
                        grid[nr][nc] = 0
                        res += 1
            return res 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = bfs(r,c)
                    maxArea = max(maxArea, area)
        return maxArea 

        