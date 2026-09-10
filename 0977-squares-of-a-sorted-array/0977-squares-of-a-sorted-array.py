class Solution(object):
    def sortedSquares(self, nums):
        arr1 = []
        arr2 = []
        final_arr = []
        n = 0
        m = 0
        
        for i in nums:
            if i < 0:
                arr1.append(i * i)
            else:
                arr2.append(i * i)
                
        arr1.reverse()
        
        while n < len(arr1) and m < len(arr2):
            if arr1[n] <= arr2[m]:
                final_arr.append(arr1[n])
                n += 1
            else:
                final_arr.append(arr2[m])
                m += 1
                
        while n < len(arr1):
            final_arr.append(arr1[n])
            n += 1
            
        while m < len(arr2):
            final_arr.append(arr2[m])
            m += 1
            
        return final_arr