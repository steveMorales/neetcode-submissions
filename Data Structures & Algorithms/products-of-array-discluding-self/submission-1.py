class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        #pre
        pre = 1
        for i in range(len(nums)):
            output[i] = pre
            pre *= nums[i]
        #post
        post = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= post
            post *= nums[i]
        
        return output


# 1,2,4,6
# 1,1,2,8
# 48,24,6,1