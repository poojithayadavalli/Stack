"""

Ganesh is learning about stack datastructure and he wants to solve the following task:

Given an array of N integers. The task is to count the number of subarrays (of size at least one) that are non-increasing.

Input:

Firstline indicates number of elements in array N
nextline contains the elements of array

Output:

Print the count of non increasing subarrays

Example:

Input:
3
1 4 3

Output:
4

Explanation:
The possible subarrays are {1}, {4}, {3}, {4, 3}.

Input:
4
4 3 2 1

Output:
10

"""
def countNonIncreasing(arr, n):
    cnt = 0
    len1 = 1
    for i in range(n-1):
        if (arr[i + 1] <= arr[i]):
            len1 += 1
        else:
            cnt += (((len1 + 1) * len1) // 2)
            len1 = 1 
    if (len1 > 1):
        cnt += (((len1 + 1) * len1) // 2)
    elif len1==1:
        cnt+=1
    return cnt
n=int(input())
arr=list(map(int,input().split()))
print(countNonIncreasing(arr,n))
