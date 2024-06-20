import random


def pattern_1(input):
    print("___________________")
    print("Pattern 1")
    print("___________________")
    print(f"Input : {input}")
    print("===================")
    for i in range(0, input):
        for j in range(0, input):
            print("* ", end="")
        print()


def pattern_2(input):
    print("___________________")
    print("Pattern 2")
    print("___________________")
    print(f"Input : {input}")
    print("===================")
    for i in range(0, input):
        for j in range(0, i):
            print("* ", end="")
        print()
    pass


def pattern_3(input):
    print("___________________")
    print("Pattern 3")
    print("___________________")
    print(f"Input : {input}")
    print("===================")
    for i in range(1, input + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()


def pattern_4(input):
    print("___________________")
    print("Pattern 4")
    print("___________________")
    print(f"Input : {input}")
    print("===================")
    for i in range(1, input + 1):
        for j in range(1, i + 1):
            print((i), end="")
        print()


def pattern_5(input):
    print("___________________")
    print("Pattern 5")
    print("___________________")
    print(f"Input : {input}")
    print("===================")
    for i in range(0, input):
        for j in range(0, input - i):
            print("* ", end="")
        print()


def pattern_6(input):
    print("___________________")
    print("Pattern 6")
    print("___________________")
    print(f"Input : {input}")
    print("===================")
    for i in range(0, input + 1):
        for j in range(1, input + 1 - i):
            print(j, end="")
        print()


def pattern_7(input):
    print("___________________")
    print("Pattern 7")
    print("___________________")
    print(f"Input : {input}")
    print("===================")
    for i in range(0, input):
        for j in range(0, input - i - 1):
            print("  ", end="")
        for j in range(0, (2 * i + 1)):
            print("* ", end="")
        for j in range(0, input - i - 1):
            print("  ", end="")
        print()


def pattern_8(input):
    print("___________________")
    print("Pattern 8")
    print("___________________")
    print(f"Input : {input}")
    print("===================")
    for i in range(0, input):
        for j in range(0, i):
            print("  ", end="")
        for j in range(0, ((2 * (input - i)) - 1)):
            print("* ", end="")
        for j in range(0, i):
            print("  ", end="")
        print()


def pattern_9(input):
    print("___________________")
    print("Pattern 9")
    print("___________________")
    print(f"Input : {input}")
    print("===================")
    for i in range(0, input):
        for j in range(0, input - i - 1):
            print("  ", end="")
        for j in range(0, (2 * i + 1)):
            print("* ", end="")
        for j in range(0, input - i - 1):
            print("  ", end="")
        print()
    for i in range(0, input):
        for j in range(0, i):
            print("  ", end="")
        for j in range(0, ((2 * (input - i)) - 1)):
            print("* ", end="")
        for j in range(0, i):
            print("  ", end="")
        print()


def pattern_10(input):
    print("___________________")
    print("Pattern 10")
    print("___________________")
    print(f"Input : {input}")
    print("===================")
    for i in range(0, ((2 * input) - 1)):
        if i < input:
            for j in range(0, i + 1):
                print("* ", end="")
        else:
            for j in range(0, ((2 * input) - 1) - i):
                print("* ", end="")
        print()


def pattern_11(input):
    print("___________________")
    print("Pattern 11")
    print("___________________")
    print(f"Input : {input}")
    print("===================")
    start = 1
    for i in range(1, input + 1):
        if ((i + 1) % 2) == 0:
            start = 1
        else:
            start = 0
        for j in range(1, i + 1):
            print(start, end="")
            start = 1 - start
        print()


def pattern_12(input):
    space = 2 * (input - 1)
    for i in range(0, input):
        for j in range(0, i + 1):
            print(f"{j+1} ", end="")
        for j in range(space, 0, -1):
            print("* ", end="")
        for j in range(i + 1, 0, -1):
            print(f"{j} ", end="")
        print()
        space -= 2


def pattern_13():
    num = 1
    for i in range(0, 5):
        for j in range(0, i + 1):
            print(f"{num} ", end="")
            num += 1
        print()


def pattern_14():
    num = 65
    for i in range(0, 5):
        for j in range(0, i + 1):
            print(f"{chr(num+j)} ", end="")
        print()


def pattern_15(input):
    num = 65
    for i in range(0, input):
        for j in range(0, input - i):
            print(f"{chr(num+j)} ", end="")
        print()


def pattern_16(input):
    num = 65
    for i in range(0, input):
        for j in range(0, i + 1):
            print(f"{chr(num+i)} ", end="")
        print()


def pattern_17(input):
    for i in range(0, input):
        ch = "A"
        breakpoint = (2 * i + 1) // 2
        for j in range(1, input - i):
            print("* ", end="")
        for j in range(1, 2 * i + 2):
            print(ch, end=" ")
            if j <= breakpoint:
                ch = chr(ord(ch) + 1)
            else:
                ch = chr(ord(ch) - 1)
        for j in range(input - i, 0, -1):
            print("* ", end="")
        print()


def pattern_18(input):
    num = 65
    print("___________________")
    print("Pattern 18")
    print("___________________")
    print(f"Input : {input}")
    print("===================")
    for i in range(0, input):
        for j in range(0, i + 1):
            print(f"{chr(num+input-i+j-1)} ", end="")
        print()


def pattern_19(input):
    for i in range(0, 5):
        for j in range(0, (10 - (10 // 2) - i)):
            print("* ", end="")
        for j in range(1, (2 * i + 1)):
            print("  ", end="")
        for j in range((10 - (10 // 2) - i), 0, -1):
            print("* ", end="")
        print()
    for i in range(0, 5):
        for j in range(0, i + 1):
            print("* ", end="")
        for j in range((10 - (2 * (i + 1))), 0, -1):
            print("  ", end="")
        for j in range(i + 1, 0, -1):
            print("* ", end="")
        print()


def pattern_20(input):
    for i in range(0, 2 * input - 1):
        for j in range(0, i + 1):
            print("* ", end="")
        for j in range((10 - (2 * (i + 1))), 0, -1):
            print("  ", end="")
        for j in range(0, i + 1):
            print("* ", end="")
        print()


if __name__ == "__main__":
    for i in random.sample(range(1, 10), k=1):
        # pattern_17(i)
        # pattern_18(i)
        # pattern_19(i)
        pattern_9(4)
