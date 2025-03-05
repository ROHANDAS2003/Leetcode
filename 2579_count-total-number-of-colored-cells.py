class Solution(object):
    def coloredCells(self, n):
        return (2*(n*n)) - (2*n) + 1
   
sol = Solution()
print("\ncase 1: 1")
print(sol.coloredCells(1))
print("\ncase 2: 2")
print(sol.coloredCells(2))
print("\ncase 3: 3")
print(sol.coloredCells(3))