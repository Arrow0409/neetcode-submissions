class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        for i in range(len(nums)):
            for j in range(i):
                if(i!=j):
                    if nums[i]+nums[j]==target:
                        result.append(j)
                        result.append(i)
                        break
        return result

        