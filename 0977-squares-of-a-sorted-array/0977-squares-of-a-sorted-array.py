class Solution(object):
    def sortedSquares(self, nums):
        arr = []
        arr2 = []
        for i in nums:
            if i < 0:
                arr.append(i * i)
            else:
                arr2.append(i * i)

        arr.reverse()

        n = 0
        m = 0
        result = []
        
        while n < len(arr) and m < len(arr2):
            if arr[n] < arr2[m]:
                result.append(arr[n])
                n += 1
            else:
                result.append(arr2[m])
                m += 1

        while n < len(arr):
            result.append(arr[n])
            n += 1
        while m < len(arr2):
            result.append(arr2[m])
            m += 1
        return result
                