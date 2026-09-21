class Solution(object):
    def isPalindrome(self, head):
        value = []
        current = head
        while current:
            value.append(current.val)
            current = current.next
        return value == value[::-1]

        