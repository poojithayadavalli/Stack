"""

Given an array of integers containing duplicate elements. The task is to find the sum of all highest occurring elements in the given array.

That is the sum of all such elements whose frequency is maximum in the array.

Input:
Firstline indicates size of array n
Secondline contains elements of array

Output:
print the sum of all elements with maximum frequency

Example:

Input:
7
1 2 2 2 3 3 3

Output:
6

Input:
5
1 2 3 4 4

Output:
4

"""

x=int(input())
arr=list(map(int,input().split()))
s=list(set(arr))
maxi=0
for i in s:
    y=arr.count(i)
    if maxi<y:
        maxi=y
sum1=0
for i in s:
    if arr.count(i)==maxi:
        sum1+=i
print(sum1)
