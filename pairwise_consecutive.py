"""
Given a stack of integers, write a function  that checks whether numbers in the stack are pairwise consecutive or not. 

The pairs can be increasing or decreasing, and if the stack has an odd number of elements, the element at the top is left out of a pair. 

The function should retain the original stack content.

Input:
Firstline contains size of stack
secondline contains elements of stack

Output:
print whether it contains pairwise consecutive elements or no

Example:

Input : 
6
4 6 6 7 4 3

Output :
No

Explanation:
(4, 6) are not consecutive.

Input : 
9
4 5 -2 -3 11 10 5 6 20

Output : 
Yes

Explanation:
Each of the pairs (4, 5), (-2, -3), (11, 10) and
(5, 6) consists of consecutive numbers.


"""

def pairWiseConsecutive(aux):
    result =  True
    while (len(aux) > 1):
        x = aux.pop(0)  
        y = aux.pop(0)  
        if (abs(x - y) != 1):  
            result = False
            break
  
    return "yes" if result else "no"
n=int(input())
s=list(map(int,input().split()))
print(pairWiseConsecutive(s))

