class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        res = float("infinity")

        while l <= r:
            m = (l+r) // 2
            res = min(res,nums[m])
            # #not shifted
            # if nums[l] < nums[r] and nums[l] < nums[m]:
            #     r = m
            # #shifted and lowest is in first half
            # elif nums[l] > nums[r] and nums[l] > nums[m]:
            #     r = m
            # #shifted and lowest in second half
            # # elif nums[l] > nums[r] and nums[l] < nums[m]:
            # #     l = m
            if nums[l] > nums[r] and nums[l] < nums[m]:
                l = m + 1
            elif nums[l] > nums[r] and nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return res
            
            