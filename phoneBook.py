if __name__=="__main__":
    n=int(input())
    phoneDict={}
    for i in range(n):
        inpStr=input()
        inpArr=inpStr.split()
        phoneDict[inpArr[0]] = int(inpArr[1])
    
    #print(phoneDict)
    while True:
        try:
            x=input()
            if x in phoneDict.keys():
                print("{}={}".format(x, phoneDict.get(x)))
            else:
                print("Not found")   
        except Exception:
            break        
        
