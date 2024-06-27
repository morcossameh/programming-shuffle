# Problem: https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        
        def bfs(x, y):
            queue = deque([(x, y)])
            visit.add((x, y))

            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dx, dy in directions:
                    x, y = row + dx, col + dy
                    if (x in range(rows) and
                        y in range(cols) and
                        grid[x][y] == "1" and
                        (x, y) not in visit):
                        queue.append((x, y))
                        visit.add((x, y))

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1" and (x, y) not in visit:
                    islands += 1
                    bfs(x, y)
        
        return islands
