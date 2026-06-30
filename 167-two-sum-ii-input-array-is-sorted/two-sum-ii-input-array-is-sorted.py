class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
     numbers.sort()
     left,right=0,len(numbers)-1
     while left<right:
        if numbers[left]+numbers[right]==target:
            a=[left+1,right+1]
            return a
        elif numbers[left]+numbers[right] < target:
            left+=1
        else:
            right-=1           