"""

Given an array arr[] and a number k. The task is to delete k elements which are smaller than next element.

(i.e., we delete arr[i] if arr[i] < arr[i+1]) or become smaller than next because next element is deleted.

Constraints:

1<=arr[].length<=1000
1<=k<=100

Input:
first line contains elements of array
Secondline indicates the integer k

Output:
Print the arrray after deleting k such elements

Example:
Input:

3 100 1
3

Output:
100 1

Input:
20 10 25 30 40
2

Output:
25 30 40

Explanation : 
First we delete 10 because it follows arr[i] < arr[i+1]. 
Then we delete 20 because 25 is moved next to it and it also starts following the condition.

Input:
23 45 11 77 18
3

Output:

77 18

"""
def deleteElements(arr, n, k):
    st = [] 
    st.append(arr[0])
    top = 0
    count = 0
    for i in range(1, n): 
        while(len(st) != 0 and count < k and st[top] < arr[i]):
            st.pop() 
            count += 1
            top -= 1
  
        st.append(arr[i]) 
        top += 1
    print(*st)
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
deleteElements(arr,n,k)

