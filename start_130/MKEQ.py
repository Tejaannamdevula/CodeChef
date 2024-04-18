for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    minimum = min(arr)
    if arr[0] != minimum or arr[-1] != minimum:
        print("NO")
    else:
        print("YES")