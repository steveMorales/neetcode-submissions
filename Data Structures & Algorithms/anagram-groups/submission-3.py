class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        #going to group them based on their common word (anagram) so the key is that. would have to sort them to find that
        for word in strs:
            sorted_word = "".join(sorted(word))
            res[sorted_word].append("".join(word))
        return list(res.values())
