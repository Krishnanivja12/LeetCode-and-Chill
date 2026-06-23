class Solution(object):
    def sortedSquares(self, nums):
        arr = []
        for i in nums:
            arr.append(i * i)
        arr.sort()
        return arr        