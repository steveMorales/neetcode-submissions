class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search vs linear search
        #linear = sequential (O(n) time)

        #binary = compare target to half way of sorted, cut in half each time
        # O(log(n))

        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid-1
            else:
                l = mid+1
        return -1