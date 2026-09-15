class Solution(object):
    def moveZeroes(self, nums):
        value = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[value] = nums[value], nums[i]
                value += 1

        