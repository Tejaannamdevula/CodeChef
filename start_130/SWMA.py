def reverse(num:int):
    ''''
    make it as a string and use reverse function and return int(num) 

    '''

    #since  number is twodigt reversse = (num%10)*10 + (num//100)

    return (num%10)*10 +(num//100)

for _ in range(int(input())):
    alice,bob = map(int,input().split())
    if alice > bob or alice > reverse(bob) or reverse(alice) > bob or reverse(alice) > reverse(bob) :
        print("YES")
    else:
        print("NO")
    