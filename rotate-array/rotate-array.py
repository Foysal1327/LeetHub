class Solution:
    def reverse(self, nums, i, j):
        left_i = i
        right_i = j
        while(left_i < right_i):
            temp = nums[left_i]
            nums[left_i] = nums[right_i]
            nums[right_i] = temp
            
            left_i += 1
            right_i -= 1
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if(k < 0):
            k += len(nums)
            
        self.reverse(nums, 0, len(nums)-k-1);
        self.reverse(nums, len(nums)-k, len(nums)-1)
        self.reverse(nums, 0, len(nums)-1)
        

        