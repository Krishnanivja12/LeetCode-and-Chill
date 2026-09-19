class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()

        arr1 = strs[0] 
        arr2 = strs[-1]
        ans = ""

        for i in range(min(len(arr1), len(arr2))):
            if arr1[i] != arr2[i]:
                break
            ans += arr1[i]
        return ans




