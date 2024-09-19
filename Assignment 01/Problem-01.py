def balancedSplit(str):
    c = ans = 0
    result = []
    temp = ""

    for char in str:

        temp += char

        if char == 'L':
            c += 1

        else:
            c -= 1

        if c == 0:
            ans += 1
            result.append(temp)
            temp = ""

    print(ans)
    for balanced_str in result:
        print(balanced_str)

str = input()

balancedSplit(str)
    