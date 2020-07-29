"""

Rekha is learning about stack datastructure and she found a problem statement as given below:

Given a binary string containing only 0's and 1's  with an Question mark ?.Ex: 11?01

The task is to find all the combinations possible with the given binary string replacing the ? with 0 or 1.

Constraints:
The binary string should contain only 0's 1's and ?'s

Input:

Input indicates the binary string


Output:
print all the possible combinations of binary strings

Example:

Input:
01?11?0

Output:
0111110
0111100
0101110
0101100

Input:
11?01

Output:
11101
11001

"""
from collections import deque

def printAllCombinations(pattern):
    stack = deque()
    stack.append(pattern)
    while stack:
        curr = stack.pop()
        index = curr.find('?')
        if index != -1:
            for ch in "01":
                curr = curr[:index] + ch + curr[index + 1:]
                stack.append(curr)
        else:
            print(curr)

str1=input()
printAllCombinations(str1)
