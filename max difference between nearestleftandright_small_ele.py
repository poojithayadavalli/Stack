"""

Given an array of integers, the task is to find the maximum absolute difference between the nearest left and the right smaller element of every element in the array.

Note: If there is no smaller element on right side or left side of any element then we take zero as the smaller element. 

For example for the leftmost element, the nearest smaller element on the left side is considered as 0. 

Similarly, for rightmost elements, the smaller element on the right side is considered as 0

Input:
First line contains size of array n 
Secondline indicates the integers in array

Output:
print the maximum absolute difference between nearest left and right smaller element

Examples:

Input :
3
2 1 8

Output : 1

Explanation:
Left smaller  LS[] {0, 0, 1}
Right smaller RS[] {1, 0, 0}
Maximum Diff of abs(LS[i] - RS[i]) = 1 

Input  :
7
2 4 8 7 7 9 3

Output : 
4

Explanation:
Left smaller   LS[] = {0, 2, 4, 4, 4, 7, 2}
Right smaller  RS[] = {0, 3, 7, 3, 3, 3, 0}
Maximum Diff of abs(LS[i] - RS[i]) = 7 - 3 = 4 

Input :
7
5 1 9 2 5 1 7

Output : 1

"""

def leftsmaller(arr, n, SE):
    sta = [] 
    for i in range(n):
        while(sta != [] and sta[len(sta)-1] >= arr[i]): 
            sta.pop() 
        if(sta != []): 
            SE[i]=sta[len(sta)-1]
        else: 
            SE[i]=0 
        sta.append(arr[i]) 

def findMaxDiff(arr, n): 
    ls=[0]*n
    rs=[0]*n
    leftsmaller(arr, n, ls)
    leftsmaller(arr[::-1], n, rs)
    res = -1
    for i in range(n): 
        res = max(res, abs(ls[i] - rs[n-1-i])) 
    return res
n=int(input())
arr=list(map(int,input().split()))
print(findMaxDiff(arr,n))
