"""
Given an integer k and a queue of N integers, we need to reverse the order of the first k elements of the queue, 

leaving the other elements in the same relative order. Only following standard operations are allowed on queue.

enqueue(x) : Add an item x to rear of queue
dequeue() : Remove an item from front of queue
size() : Returns number of elements in queue.
front() : Finds front item.

Constraints:
0<=k<=N
1<=N<=1000

Input:
First line indicates the integer N
Second line contains elements of queue
Next line contains the integer k
Output:
Print the resultant queue

Examples:

Input :
10
10 20 30 40 50 60 70 80 90 100
5
Output :
50 40 30 20 10 60 70 80 90 100

Input :
10
10 20 30 40 50 60 70 80 90 100
4
Output :
40 30 20 10 50 60 70 80 90 100

Input:
5
6 8 9 4 7
3
Output:
9 8 6 4 7 
Input:
5
1 2 3 4 5
5
Output:
5 4 3 2 1 
"""
from queue import Queue 
def reverseQueueFirstKElements(k, Queue): 
    if (Queue.empty() == True or
             k > Queue.qsize()):  
        return
    if (k <= 0):  
        return
    Stack = []
    for i in range(k): 
        Stack.append(Queue.queue[0])  
        Queue.get()
    while (len(Stack) != 0 ):  
        Queue.put(Stack[-1])  
        Stack.pop()
    for i in range(Queue.qsize() - k): 
        Queue.put(Queue.queue[0])  
        Queue.get()
def Print(Queue): 
    while (not Queue.empty()):  
        print(Queue.queue[0], end =" ")  
        Queue.get()

Queue = Queue()
n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    Queue.put(arr[i])  
  
k = int(input())
reverseQueueFirstKElements(k, Queue)  
Print(Queue)
