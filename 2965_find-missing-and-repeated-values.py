class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        l = len(grid)
        n = l*l
        expected_sum = n * (n + 1) // 2
        actual_sum = 0
        seen = set()
        
        for row in grid:
            for num in row:
                actual_sum += num
                if num in seen:
                    a = num
                seen.add(num)
        
        b = expected_sum - actual_sum + a
        # count = []
        # for i in range(l):
        #     for j in range(l):
        #         if grid[i][j] in count:
        #             a = grid[i][j]
        #         else:
        #             count.append(grid[i][j])
        # j = 1
        # while j<=(l*l):
        #     if j in count:
        #         pass
        #     else:
        #         b = j
        #     j+=1
            
        return [a,b]

sol = Solution()
print("\nCase 1: [[1,3],[2,2]]")
print(sol.findMissingAndRepeatedValues([[1,3],[2,2]]))
print("\nCase 2: [[9,1,7],[8,9,2],[3,4,6]]")
print(sol.findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))