class Solution:
    def isArmstrong(self, x: int) -> bool:
        testSum = 0
        for i in str(x):
            testSum += int(i) ** 3
        return True if testSum == x else False


sol = Solution()
print(sol.isArmstrong(153))
