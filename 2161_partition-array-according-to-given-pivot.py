class Solution(object):
    def pivotArray(self, nums, pivot):
        less = [num for num in nums if num<pivot]
        equal = [num for num in nums if num==pivot]
        greater = [num for num in nums if num>pivot]
        
        nums = less + equal + greater
        return nums
    
sol = Solution()
print("\nCase 1: [9,12,5,10,14,3,10] and pivot = 10")
print("Sol: ",sol.pivotArray([9,12,5,10,14,3,10],10))
print("\nCase 1: [-3,4,3,2] and pivot=2")
print("Sol: ",sol.pivotArray([-3,4,3,2],2))