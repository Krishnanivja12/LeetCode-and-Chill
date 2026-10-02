class Solution(object):
    def removeElement(self, nums, val):
        K_val = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[K_val] = nums[i]
                K_val += 1
        return K_val
        
        