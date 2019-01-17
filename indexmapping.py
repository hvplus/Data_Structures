

import numpy as np

def search(no):
    if no < 0 and hasht[abs(no)][0]==1:
        print("Negative Element Present")
        
    elif no >= 0 and hasht[abs(no)][1]==1:
        print("Positive Element Present")
        
    else: print("Element not present")

ele = [1,2,-3,3,4,5,-6,-2,-4,-8,6]
hasht = np.zeros((9,2))
for i in range(0,len(ele)):
    if ele[i]<0:
        hasht[abs(ele[i])][0]=1
        
    elif ele[i]>0:
        hasht[abs(ele[i])][1]=1
        

        
    
        
    
        
    