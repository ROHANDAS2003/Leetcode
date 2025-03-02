class Solution(object):
    def mergeArrays(self, nums1, nums2):
        l1,l2 = len(nums1),len(nums2)
        d = {}
        for i in range(l1):
            if not(nums1[i][0] in d):
                d[nums1[i][0]] = nums1[i][1]
        for i in range(l2):
            if not(nums2[i][0] in d):
                d[nums2[i][0]] = nums2[i][1]
            else:
                d[nums2[i][0]] += nums2[i][1]
        
        result = []
        for i in sorted(d.keys()):
            el = [i,d[i]]
            result.append(el)
            
        return result
        
sol = Solution()
print("\nCase 1: [[1,2],[2,3],[4,5]] and [[1,4],[3,2],[4,1]]")
print("Sol: ",sol.mergeArrays([[1,2],[2,3],[4,5]],[[1,4],[3,2],[4,1]]))
print("\nCase 1: [[2,4],[3,6],[5,5]] and [[1,3],[4,3]]")
print("Sol: ",sol.mergeArrays([[2,4],[3,6],[5,5]],[[1,3],[4,3]]))