import sys
import math 

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

def reverse_kadane(arr):
    n = len(arr)
    global_minimum = math.inf
    local_minimum= 0
    for i in range(n):
        local_minimum = min(arr[i],local_minimum+arr[i])
        if local_minimum < global_minimum:
            global_minimum = local_minimum
    return global_minimum
def reverse_kadane_atleastKelements(arr,k):
    n = len(arr)
    # global_minimum = math.inf 
    local_minimum = {}
    local_minimum[0] = arr[0]
    for i in range(1,n):
        local_minimum[i] = min(arr[i],arr[i]+local_minimum[i-1])
        # if local_minimum <global_minimum:
        #     local_minimum = global_minimum
    # print("arrr",arr)
    # print("localMinimum",local_minimum)
    #sliding window

    global_minimum  = math.inf
    window_sum = 0
    for i in range(0,k):
        window_sum += arr[i]
    if window_sum < global_minimum:
        global_minimum = window_sum 
    # print("window sum",window_sum)
    for i in range(k,n):
        window_sum = window_sum+arr[i]-arr[i-k]
        # print("window",window_sum)
        curr_sum = min(window_sum,window_sum+local_minimum[i-k])
        # print('curr',curr_sum)
        if curr_sum < global_minimum:
            global_minimum = curr_sum
    return global_minimum 

    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    if n == 1:
        print(arr[0])
        continue
    min_subarray_sum = reverse_kadane_atleastKelements(arr,2)
    # min_subarray_sum = reverse_kadane(arr)
    # print('my_sum',min_subarray_sum)
    # print('my answer',sum(arr) + 2*(abs(min(0,min_subarray_sum))))
    print(sum(arr) + 2*(abs(min(0,min_subarray_sum))))

