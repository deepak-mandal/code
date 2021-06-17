# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 19:36:30 2021

@author: dkmii
"""



if __name__=="__main__":
    n=int(input("n : "))
    m=int(input("m : "))
    
    sum_div_n=0
    sum_not_div_n = 0
    for i in range(1, m+1):
        if i%n!=0:
            sum_not_div_n+=i
        else:
            sum_div_n+=i
            
    print(abs(sum_not_div_n-sum_div_n))
    
            
        

