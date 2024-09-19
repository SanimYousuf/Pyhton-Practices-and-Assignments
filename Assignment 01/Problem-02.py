def goodSequence(N,a):
    from collections import Counter

    freq = Counter(a)
    removals = 0

    for x, count in freq.items():
        if count < x:
            removals += count
        else:
            removals += (count - x)

    return removals

N = int(input().strip())
a = list(map(int,input().strip().split()))

result = goodSequence(N,a)
print(result)