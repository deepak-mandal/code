# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 19:57:57 2021

@author: dkmii
"""
def largeSmallSum(arr):
    arrLen=len(arr)
    if arrLen==0:
        return 0
    if arrLen<=3:
        return 0
    
    evenArr=[]
    oddArr=[]
    for i in range(arrLen):
        if i%2==0:
            evenArr.append(arr[i])
        else:
            oddArr.append(arr[i])
    #print(evenArr)
    #print(oddArr)
    evenArr.remove(max(evenArr))
    oddArr.remove(min(oddArr))
    #print(evenArr)
    #print(oddArr)
    return max(evenArr)+min(oddArr)

if __name__=="__main__":
    inpStr=input()
    
    arr=list(map(int, inpStr.split()))
    
    print(largeSmallSum(arr))
    