import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
for _ in range(int(input())):
    n = int(input())
    arr =list(map(int,input()))
    # print(arr)
    # print("tttt")
    subsequence = []
    prev =None

    for i in range(1,n,2):
        if arr[i-1] == arr[i]:
            continue
        else:
            if prev is not None:
                if prev !=arr[i]:
                    subsequence.append(i+1)
                    prev = arr[i]
                else:
                    subsequence.append((i-1)+1)
                    prev = arr[i-1]
            else:
                subsequence.append(i+1)
                prev = arr[i]
    else:
        print(len(subsequence))
        print(*subsequence)
