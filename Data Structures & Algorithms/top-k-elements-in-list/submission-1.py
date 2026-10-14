class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Bucket sort + hashmap
        #going to use count as the index, only need it to be the length of the array + 1 because it can only be MAX that amount of occurrences

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for c, n in count.items():
            freq[n].append(c)
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
    
