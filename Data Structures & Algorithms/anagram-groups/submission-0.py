from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_out = defaultdict(list)
        
        for s in strs:
            sort="".join(sorted(s))
            anagram_out[sort].append(s)
        
        return list(anagram_out.values())



        