class Solution:
    def isPalindrome(self, x: int) -> bool:
        originalNum = str(x)
        reverseNumber = 0
        if x > 0:
            reverseNumber = str(x)[::-1]
            return True if reverseNumber == originalNum else False
        else:
            reverseNumber = str(x)[::-1]
            return True if reverseNumber == originalNum else False


sol = Solution()
print(sol.palindrome(121))
