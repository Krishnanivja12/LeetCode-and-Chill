class Solution(object):
    def sortedSquares(self, nums):
        array = []
        for i in nums:
            array.append(i * i)
        array.sort()
        return array
    


                