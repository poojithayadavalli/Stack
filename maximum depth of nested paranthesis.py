"""
We are given a string having parenthesis like below
     “( ((X)) (((Y))) )”
We need to find the maximum depth of balanced parenthesis, like 4 in above example. Since ‘Y’ is surrounded by 4 balanced parenthesis.
If parenthesis are unbalanced then return -1.

Input':
First line contains the input string

Output:
Print the maximum depth of balanced parenthesis
Examples :

Input : 
( a(b) (c) (d(e(f)g)h) I (j(k)l)m)
Output : 4

Input :
( p((q)) ((s)t) )
Output : 3

Input : 
""
Output : 0

Input : 
b) (c) ()
Output : -1 

Input :
(b) (c) ()
Output : 1 

"""
def maxDepth(S): 
    current_max = 0
    max = 0
    n = len(S)
    for i in range(n): 
        if S[i] == '(': 
            current_max += 1
  
            if current_max > max: 
                max = current_max 
        elif S[i] == ')': 
            if current_max > 0: 
                current_max -= 1
            else: 
                return -1 
    if current_max != 0: 
        return -1
  
    return max
s = input()
print (maxDepth(s))
