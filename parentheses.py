#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
class stack:
    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return self.items==[]
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return
        return self.items.pop()
  
    
def isBalanced(s):
    # Write your code here
    st=stack()
    for ch in s:
        if ch in '({[':
            st.push(ch)
        if ch in ')}]':
            if st.is_empty():
                return "NO"
            else:
                char=st.pop()
                if not match_parentheses(char, ch):
                    return "NO"
                
    if st.is_empty():
        return "YES"
    else:
        return "NO"
    
def match_parentheses(leftPar, rightPar):
    if leftPar=='[' and rightPar==']':
        return True
    if leftPar=='{' and rightPar=='}':
        return True
    if leftPar=='(' and rightPar==')':
        return True
    return False


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
