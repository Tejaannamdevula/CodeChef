for _ in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))

    if n ==1 :
        print(0)
    else:
        count = 0
        for i in range(1,n):
            if s[i] == s[i-1]:
                count +=1

        print(count)