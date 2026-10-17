class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxContainer = 0
        l,r = 0,len(heights)-1

        while l<r:
            currentArea = (r-l) * (min(heights[r],heights[l]))
            maxContainer = max(maxContainer,currentArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxContainer