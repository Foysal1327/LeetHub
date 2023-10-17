class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numlist = {}
        for i, item in enumerate(nums):
            diff = target - item
            if diff in numlist:
                return [numlist[diff], i]
            else:
                numlist[item] = i
        