"""
Given algebraic string of characters, ‘+’, ‘-‘ operators and parentheses. The task is to simplify the algebraic string by removing parentheses

and changing necessary operators.Output the simplified string without parentheses.

Constraints:

The string must contain only "+" ,"-", "("and ")"

Input:
The input contains the algebraic string

Output:
Print the simplified string

Example:

Input :
a-(b+c)

Output :
a-b-c

Input : 
a-(b-c-(d+e))-f

Output :
a-b+c+d+e-f

"""
def simplify(Str):
    Len = len(Str) 
    res = []
    index = 0
    i = 0
    s = [] 
    s.append(0)
    while (i < Len):  
        if (Str[i] == '+'):
            if (s[-1] == 1):  
                res.append('-')
            if (s[-1] == 0): 
                res.append('+')
            index += 1
  
        elif (Str[i] == '-'): 
            if (s[-1] == 1):  
                res.append('+')
            elif (s[-1] == 0):  
                res.append('-')
            index += 1
        elif (Str[i] == '(' and i > 0): 
            if (Str[i - 1] == '-'):
                x = 0 if (s[-1] == 1) else 1
                s.append(x)  
            elif (Str[i - 1] == '+'):  
                s.append(s[-1])
        elif (Str[i] == ')'):  
            s.pop()  
        else: 
            res.append(Str[i]) 
            index += 1
        i += 1
    return "".join(res)
Str=input()
print(simplify(Str))
