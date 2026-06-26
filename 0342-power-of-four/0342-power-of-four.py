class Solution(object):
    def isPowerOfFour(self, num):
        if num <= 0:
            return False
        while 0 == num % 4:
            num = num // 4
        return num == 1
        