# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 08:31:46 2021

@author: dkmii
"""

if __name__=="__main__":
    n=int(input())
    sum=0
    for i in range(1, 11):
        print(i*n, end=" ")
        sum+=i*n
    print()
    print(sum)
        