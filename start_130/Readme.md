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

#### not done during live

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

    there will be no case for not having a subsequence. cant write in words

#### Solution:

in GDST.py

### Question 6

#### not done during live

[Updating A](https://www.codechef.com/problems/UPDA)

#### Explanation:

    alice want to maximize the total.alice uses absolute value i.e takes makes sum+ve even if the sum is -ve.

    bob wants to minimize the total and he uses on sum.


    first case if all elements are +ve in array both alice and bob has same answer.
    bob cannot minimize the sum .

    second case :- if there are -ve numbers
        selecting string :- 1<=L<R<=M
        so minimum sub string length is two .
        so the process of alice and bob continues till two

    alice finds the substring with minimum sum and makes it postive and inserts the positive sum in array to maximize.

    in bob turn bob finds the substring with minimum sum adds and inserts the
    -ve value in the array to minimize.

    but here is trick when bob turn he does the sum of entire array and ends the game because
        1. if all +ve there  bob cannot minimize
        2. if there are -ve
            to minimize bob want to include all -ve numbers in sum .and also bob dont give a chanve to alice
                Ex :- -1 -2 -3 -4  5 6 7 8
                bobs turn  -10 5 6 7 8
                if he gave alice a chance alice can increase total sum by
                    making (-10 +5 ) as 5 and 5 5 6 7 8 then answer is 5+5+6+7+8 = 31.

                to avoid this risk bob adds entire arrayso he surely gets the value of all -ve numbers. (-1 -2 -3 -4 +5+ 6+7+8) = 16 and minimizes.
    so alice has only one chance to increase sum because bob ends the game as soon as he gets chance.

    alice:- finds the sub string with minimum total sum and make it positive.

    we need to apply kadanes algorithm here (its used to find sub string with maximum sum ) but here we need to reverse the logic to find minimum.
    kadanes algo finds in minimum time .  but Kadanes will give length = 1 subarray also.so we need to implement kadanes algorithm with atleast 2 length subarray .

    for this we use sliding window + kadanes algo links below.

---

    Now we get minimum sum subarray values
    now if we make this positive  and caluculate rest of summ and add this

    insted of that we can directly get sum = sum+ 2*(abs(min(0,minimum_subarray_sum)))

    0 is included if minimum subarray sum is +ve then we will be adding twice so for that case we are making it 0 by adding min(0,minimum_subarray_sum)

#### learn dp for this

[resources for kadanes](https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d)

[resource for kadanes+ slidingwindow](https://www.youtube.com/watch?v=OodoQ95se20)

#### Solution:

in UPDA.py

### Question 5

#### not done during live

[Costly Swapping](https://www.codechef.com/problems/COSS)

#### Explanation:

#### Solution:

in COSS.py
