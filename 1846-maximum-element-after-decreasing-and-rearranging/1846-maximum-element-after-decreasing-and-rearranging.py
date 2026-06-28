class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        
        max_value = 1
        for i in range(1, len(arr)):
            if arr[i] > max_value:
                max_value += 1
            
        return max_value
        