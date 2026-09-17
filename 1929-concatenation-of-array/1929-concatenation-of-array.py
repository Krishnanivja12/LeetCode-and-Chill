class Solution(object):
    def getConcatenation(self, nums):
        nums2 = nums[:]
        for i in nums2:
            nums.append(i)
        return nums
        