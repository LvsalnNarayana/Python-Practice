class Recursion:
    def recursion_basic(self, counter):
        if counter == 10:
            return
        print(counter)
        counter += 1
        self.recursion_basic(counter)

    def forwardCounterBacktrack(self, i):
        if i < 1:
            return
        self.forwardCounterBacktrack(i - 1)
        print(i)

    def reverseCounterBacktrack(self, i, n=0):
        if i < 1:
            return
        self.reverseCounterBacktrack(i - 1, n)
        print(n + i)

    def parameterRecursionSum(self, i, sum=0):
        if i < 1:
            print(sum)
            return
        self.parameterRecursionSum(i - 1, sum + i)

    def functionRecursionSum(self, i) -> int:
        if i < 1:
            return i
        return i + self.functionRecursionSum(i - 1)

    def factorial(self, i) -> int:
        if i < 1:
            return 1
        return i * self.factorial(i - 1)

    def reverseArray(self, array, index=0):
        if index >= len(array) // 2:
            return
        last_index = len(array) - index - 1
        array[index], array[last_index] = array[last_index], array[index]
        self.reverseArray(array, index + 1)
        return array

    def checkPalindrome(self, string="", index=0):
        if index >= len(string) // 2:
            return True
        if string[index] != string[len(string) - index - 1]:
            return False
        return self.checkPalindrome(string, index + 1)

    def fibonacciNumber(self, index=0):
        if index <= 1:
            return index
        return self.fibonacciNumber(index - 1) + self.fibonacciNumber(index - 2)

    def printSubsequences(self, array, index=0, current_subsequence=[]):
        if index == len(array):
            print("____Current Subsequence____")
            print(current_subsequence)
            return
        current_subsequence.append(array[index])
        self.printSubsequences(
            array,
            index=index + 1,
            current_subsequence=current_subsequence,
        )

        current_subsequence.pop()
        self.printSubsequences(
            array,
            index=index + 1,
            current_subsequence=current_subsequence,
        )

    def isPalindrome(self, s: str, index=0) -> bool:
        alphaString = "".join(c.lower() for c in s if c.isalpha())
        if index >= len(alphaString) // 2:
            return True
        if alphaString[index] != alphaString[len(alphaString) - index - 1]:
            print(f"index : {alphaString[index]}")
            print(f"index -  : {alphaString[len(alphaString) - index - 1]}")
            return False
        return self.isPalindrome(s, index + 1)


rec = Recursion()
# print("______//Recursion Basic//______")
# rec.recursion_basic(0)
# print("______//Forward Counter Backtrack//______")
# rec.forwardCounterBacktrack(30)
# print("______//Reverse Counter Backtrack//______")
# rec.reverseCounterBacktrack(30)
# print("______//Parameter Recursion Sum//______")
# rec.parameterRecursionSum(30, sum=0)
# print("______//Function Recursion Sum//______")
# print(rec.functionRecursionSum(20))
# print("______//Factorial//______")
# print(rec.factorial(5))
# print("______//Reverse Array//______")
# array = [1, 2, 3, 2, 1]
# rec.reverseArray(array)
# print(array)
# print("______//Check Palindrome//______")
# result = rec.checkPalindrome("racecar")
# print(result)
# print("______//Fibonacci Number//______")
# print(rec.fibonacciNumber(10))
# print("______//Print All Subsequences//______")
# main_sequence = [3, 2, 1]
# rec.printSubsequences(main_sequence)
print(rec.isPalindrome("A man, a plan, a canal: Panama"))
