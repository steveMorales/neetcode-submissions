class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # result dictionary -> defaultdict does not return a KeyError 
        # instead with List in the parentheses it will return an empty list for every key
        res = defaultdict(list)
        #iterate through the words in the strings
        for s in strs:
            #create a count array for all the letters in the english alphabet
            count = [0] * 26
            #iterate through the chars in each word
            for c in s:
                #increment the count to the corresponding index
                count[ord(c) - ord('a')] += 1
            #convert the count array as a tuple so it can be used as they key for the dict
            #tuple=ordered, immutable collection of elements that can be of diff data types
            res[tuple(count)].append(s)
        #return the values of the hashmap in list form
        return list(res.values())

            


