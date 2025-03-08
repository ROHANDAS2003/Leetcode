class Solution(object):
    def minimumRecolors(self, blocks, k):
        if blocks.count("B"*k) == k:
            return 0
        
        allsubS = []
        for i in range((len(blocks)-k)+1):
            subS = ""
            for j in range(i,i+k):
                subS = subS + blocks[j]
            allsubS.append(subS)
        
        minRecolor = 1000
        for subS in allsubS:
            recolor = subS.count("W")
            if recolor<minRecolor:
                minRecolor = recolor
                
        return minRecolor
    
sol = Solution()
print("\nCase 1: 'WBBWWBBWBW' and 7")
print(sol.minimumRecolors("WBBWWBBWBW",7))
print("\nCase 2: 'WBBWWBB' and 2")
print(sol.minimumRecolors("WBBWWBB",2))