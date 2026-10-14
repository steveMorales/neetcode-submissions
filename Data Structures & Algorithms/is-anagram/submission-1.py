class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       if len(s) != len(t):
            return False

       freqMap_S = {}
       freqMap_T = {}

       for char in s:
            freqMap_S[char] = freqMap_S.get(char,0) + 1

       for char in t:
            freqMap_T[char] = freqMap_T.get(char,0) + 1

       return freqMap_S == freqMap_T