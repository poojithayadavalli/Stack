"""

Veena want to solve a problem as follows. Given an array of N distinct element of at least size 2.

A pair (a, b) in an array is defined as ‘a’ is the index of second highest element and ‘b’ is the index of highest element in the array. 

The task is to count all the distinct pair where a < b in all the subsequences.

Input:

Firstline indicates the size of array n
nextline consists of elements of array

Output:

print the count of such subarray that follows given condition

Example:

Input:
4
1 3 2 4

Output:
3

Explanation :

The subarray { 1 }, { 3 }, { 2 }, { 4 } does not contain any such pair
The subarray { 1, 3 }, { 2, 4 } contain (1, 2) as pair
The subarray { 3, 2 } does not contain any such pair
The subarray { 3, 2, 4 } contain (1, 3) as a pair
The subarray { 1, 3, 2 } does not contain any such pair
The subarray { 1, 3, 2, 4 } contain (2, 4) as a pair
So, there are 3 distinct pairs, which are (1, 2), (1, 3) and (2, 4).


"""
