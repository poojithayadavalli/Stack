"""
Given an array of size n.The task is tofind the difference between highest occurrence and least occurrence of any number in an array

Constraints:
1<=n<=1000

Input:
First line contains integer n
Second line contains elements of array
Output:
print the difference between highest frequency and least frequency.

Examples:

Input  : 
11
7 8 4 5 4 1 1 7 7 2 5
Output : 2
Lowest occurring element (5) occurs once.
Highest occurring element (1 or 7) occurs 3 times

Input  :
6
1 1 1 3 3 3
Output : 0
Input:
4
1 2 2 4
Output:
1

Input:
5
3 3 3 3 1
Output:
3
Input:
3
1 2 3
Output:
0
"""
def findDiff(arr, n):
    arr.sort()
    max_count = 0
    min_count = n 
    for i in range(n):
        count=arr.count(arr[i])
        max_count = max(max_count, count) 
        min_count = min(min_count, count)
    return max_count - min_count
n = int(input())
arr=list(map(int,input().split()))
print (findDiff(arr, n)) 

