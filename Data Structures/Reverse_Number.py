class Solution:
    def reverse(self, x: int) -> int:
        reverseNumber = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)

        while x != 0:
            lastDigit = x % 10
            x //= 10
            reverseNumber = (reverseNumber * 10) + lastDigit

        reverseNumber *= sign
        # Handle overflow, assuming 32-bit signed integer range
        if reverseNumber < -(2**31) or reverseNumber > 2**31 - 1:
            return 0
        return reverseNumber


sol = Solution()
print(sol.reverse(1234))
