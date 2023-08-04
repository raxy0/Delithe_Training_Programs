#Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        rev_num=0
        temp = x

        while temp!=0:
            dig=temp%10
            rev_num=rev_num*10 + dig
            temp //= 10

        return rev_num == x        