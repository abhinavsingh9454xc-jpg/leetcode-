class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            a=nums[i]**2
            result.append(a)
        result.sort()
        return result   