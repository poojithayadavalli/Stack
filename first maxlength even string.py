"""
Given a string of words separated by spaces. The task is to find the first maximum length even word from the string.

Eg: “You are given an array of n numbers” The answer would be “an” and not “of” because “an” comes before “of”.

If no such word found print -1

Examples:

Input:
this is a test string
Output:  string
Even length words are this, is, test, string. Even
maximum length word is string.

Input: 
guvigeeks is a platform for geeks
Output:  platform
Only even length word is platform.

Input:
helo world
Output:
helo
Input:
hello world
Output:
-1

"""
def findMaxLenEven(str): 
    n = len(str) 
    i = 0
    currlen = 0
    maxlen = 0
    st = -1
  
    while (i < n):
        if (str[i] == ' '): 
            if (currlen % 2 == 0): 
                if (maxlen < currlen): 
                    maxlen = currlen 
                    st = i - currlen 
            currlen = 0  
        else :
            currlen += 1
  
        i += 1
    if (currlen % 2 == 0): 
        if (maxlen < currlen): 
            maxlen = currlen 
            st = i - currlen  
    if (st == -1):
        return "-1"
      
    return str[st: st + maxlen] 
str = input()
print(findMaxLenEven(str))
