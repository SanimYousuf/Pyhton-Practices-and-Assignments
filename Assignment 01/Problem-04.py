n = int(input())

arr = list(map(int, input().split()))

count = 0
while all(i%2==0 for i in arr):
    
    arr = [i//2 for i in arr]
    count += 1

print(count)