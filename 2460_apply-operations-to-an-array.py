class Solution(object):
    def applyOperations(self, nums):
        l = len(nums)
        for i in range(l-1):
            if nums[i] == nums[i+1]:
                nums[i] *=2
                nums[i+1] = 0

        non_zero_nums = [num for num in nums if num != 0]
        zero_count = l-len(non_zero_nums)
        
        return non_zero_nums + [0] * zero_count

sol = Solution()
print("\nCase 1: [1,2,2,1,1,0]")
print("Sol: ",sol.applyOperations([1,2,2,1,1,0]))
print("\nCase 1: [0,1]")
print("Sol: ",sol.applyOperations([0,1]))