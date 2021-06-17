# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 08:07:49 2021

@author: dkmii
"""

if __name__=="__main__":
    n=int(input("n: "))
    m=int(input("m: "))
    
    outRes=[]
    for x in range(n+1, m, 1):
        x=str(x)
        res=[]
        for i in range(len(x)):
            if x[i] == x[-(i+1)]:
                res.append(0)
                #outRes.append(x)
            else:
                res.append(1)
        if max(res)==0:
            outRes.append(x)
            
    for out in outRes:
        print(out, end=" ")
        
        