class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1


        while left < right:
            #target is less than largest number
            if numbers[left] + numbers[right] > target:
                right -= 1
            #target is more than largest number
            if numbers[left] + numbers[right] < target:
                left += 1
            #found answer
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]
