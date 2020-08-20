"""
Given a string, The task is to find the 1st repeated word in a string.

If no repeated words in the string print "No Repetition".

Input:
First line contains the input string

Output:
Print the first repeated word

Examples:

Input :
Ravi had been saying that he had been there
Output : had

Input :
Ravi had been saying that
Output : No Repetition

Input : "he had he had"
Output : he

Input:
hello world hello
Output:
hello

Input:
hello
No Repetition
"""
x=input().split()
a=[]
y=None
for i in x:
    if i in a:
        y=i
        break
    else:
        a.append(i)
print(y if y else "No Repetition")
    
