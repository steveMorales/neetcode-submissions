class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1

        while left < right:
            #if numbers at those spots are target
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]
            #if numbers at those spots are less than target
            if numbers[left] + numbers[right] < target:
                left += 1
            #if numbers at those spots are more than target
            if numbers[left] + numbers[right] > target:
                right -= 1

            