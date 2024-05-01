import math


class Solution:
    def getDivisors(self, x: int) -> list:
        divisor_list = []
        for i in range(1, x + 1):
            if x % i == 0:
                divisor_list.append(i)
        return divisor_list

    def getDivisors2(self, x: int) -> list:
        divisor_list = []
        print(int(math.sqrt(x)))
        for i in range(1, int(math.sqrt(x)) + 1):
            if x % i == 0:
                divisor_list.append(i)
                if i != x // i:
                    divisor_list.append(x // i)
        divisor_list.sort()
        return divisor_list


sol = Solution()
print(sol.getDivisors2(345677282))
