# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:59:42 2021

@author: dkmii
"""
def decimalToBinary(n):
    if (n>=1):
        decimalToBinary(n//2)
    print(n%2, end="")

 


if __name__=="__main__":
    try:
        decVal=int(input())
        decimalToBinary(decVal)
        
        
    except Exception:
        pass
