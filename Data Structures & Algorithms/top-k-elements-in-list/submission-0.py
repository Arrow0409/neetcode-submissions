from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_map = defaultdict(list)
        for num in nums:
            frequent_map[num].append(num)

        final = sorted(frequent_map.keys(), key=lambda x: len(frequent_map[x]), reverse=True)
        return final[:k]
        