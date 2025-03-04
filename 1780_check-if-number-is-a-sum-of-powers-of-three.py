class Solution(object):
    def checkPowersOfThree(self, n):
        while n!=0:
            rem = n%3
            if rem == 2:
                return False
            else:
                n = n//3
        return True
    
sol = Solution()
print("\ncase 1: 12")
print(sol.checkPowersOfThree(12))
print("\ncase 2: 91")
print(sol.checkPowersOfThree(91))
print("\ncase 3: 21")
print(sol.checkPowersOfThree(21))