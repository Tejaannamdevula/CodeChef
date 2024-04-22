# Code Chef Contest starters 130

## Contest Details

- **Date:** 17-04-2024
- **Duration:** [Contest Duration]
- **Link:** [starters130](http://www.codechef.com/START130)

## Questions

### Question 1

[Gaint Wheel](https://www.codechef.com/problems/GIANT)

#### Explanation:

        if height >=60 print yes else no

#### Solution:

in GaintWheel.py

### Question 2

[Swapping Marks digits](https://www.codechef.com/problems/SWMA)

#### Explanation:

    4 cases
        1.  alice_num  > bob_num
        2. reverse of alice_num > bob_num
        3. reverse of alice_num > reverse of bob_num
        4. alice_num is >reverse of bob_num
    if any one situation is possible then print yes else no

#### Solution:

in SWMA.py

### Question 3

[Alternating Binary String](https://www.codechef.com/problems/ALBS)

#### Explanation:

    if s = 0 or 1 no operetions is needed since to say  alternating we need atleast length 2 string

    1010 -> apply operation at index 2 ==>  1 --101--
    when applying operation next  parts also being reversed (obvious)
    so if the seqence is alternative when applying operation at any previous doent change it's alternative nature .

    when to apply operation
        two 11 or 00 come   we apply once and make them 10 and 01
        so by this for solution we can count how may time two
        consecutive places in a string has equal value so that
        many operations we need to perform

#### Solution:

in SWMA.py

### Question 4

[Make Equal](https://www.codechef.com/problems/MKEQ)

#### Explanation:

    operation:- 1<i<N Ai >= Ai-1 and Ai> Ai+1 reduce Ai by 1

    making equal the entire array:
        arr = [1,2,3,4,1,1]
        we can make equal the array by reducing each element to the
        minimum value (here 1).

        for any number we can apply the operation and reduce it to the
        minimum value
        ex:-
        2 3 4 --> 2 3 3 --> 2 2 3 ---> 2 2 2---> 1 2 2 --> 1 1 2
        ---> 1 1 1
        but given we can apply in range of 1< i < N so we cant use
        it for end values so to make entire array equal end values must be equal to the minimum values

    base case:-
        only one element all are equal.

#### Solution:

in MKEQ.py

### Question 5

[Good binary string](https://www.codechef.com/problems/GDST)

#### Explanation:

    from given condition it is evident that pi can be 00 or 11 atleast .if 0000 it can be
    divided into 00 00 i.e p1 and p2 of length 2. so every pi has a length 2

    if arr[i] == arr[i-1] no need to do anything 1 <=i < n (zero indexing)

    if not equal means arr[i-1],arr[i]  is 0 1 or 1 0

    store the index i in q queue we need to select an alternating subsequence

    so to do this 0 1 is one part and in the array in some othe place 1 0 is present
    no we selct 1 from 1st part and 0 from 2nd part and apply the operation
    therefore after applying operation it becomes 00 and 11

    we are storing the indices in a list to print them.

    when storing in the queue if 0 is prev one then the condition arr[i-1] and arr[i]
    is not equal but arr[i]  is 0 then you need to take arr[i-1] (i.e 1 ) as subsequence.

        Ex:- 101001  ---- > 2 3 5

    there will be no case for not having a subsequence. cant write in words .

#### Solution:

in GDST.py
