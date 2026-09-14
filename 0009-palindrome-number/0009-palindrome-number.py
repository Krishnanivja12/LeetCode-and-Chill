class Solution(object):
    def isPalindrome(self, Element):
        if Element < 0:
            return False

        reverse = str(Element)
        return reverse == reverse[::-1]
