class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        visited = set()
        island = 0

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                poppedr, poppedc = q.popleft()
                directions = [[0,1],[1,0],[0,-1],[-1,0]]
                for dr,dc in directions:
                    nextrow = poppedr + dr
                    nextcol = poppedc + dc

                    if (nextrow in range(row) and 
                        nextcol in range(col) and 
                        (nextrow,nextcol) not in visited and 
                        grid[nextrow][nextcol] == '1'):
                        q.append((nextrow,nextcol))
                        visited.add((nextrow,nextcol))
                    
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    island += 1
        return island
        