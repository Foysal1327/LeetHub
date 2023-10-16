class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        print(nums)
        a_set = set(nums)
        temp = []
        nums.clear()
        for item in a_set:
            nums.append(item)
        nums.sort()
        length = len(nums)
        
        return length
        