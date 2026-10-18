class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        l = 0
        charSet = set()
        longestSub = 1

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            longestSub = max(longestSub,r-l+1)
            
        return longestSub




