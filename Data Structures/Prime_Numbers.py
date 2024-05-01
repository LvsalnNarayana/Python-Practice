import math


class Solution:
    def checkPrime(self, x: int) -> list:
        counter = 0
        for i in range(1, int(math.sqrt(x)) + 1):
            if x % i == 0:
                counter += 1
                if i != x // i:
                    counter += 1
        return True if counter == 2 else False


sol = Solution()
print(sol.checkPrime(19))
