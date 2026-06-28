class Solution(object):
    def isAnagram(self, sum, target):
        if len(sum) != len(target):
            return False

        for ch in sum:
            if sum.count(ch) != target.count(ch):
                return False

        return True
        