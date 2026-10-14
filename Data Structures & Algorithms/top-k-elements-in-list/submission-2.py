class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap to store count of each integer
        #reverse bucket sort where index is count of integer
        #we know an integer can only have a count MAX of len(nums)

        freq = [[] for i in range(len(nums)+1)]
        count = {}
        res = []
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        #this makes sense because we want to append those numbers to that count
        # key : value
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        