# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:40:25 2019

@author: Administrator
"""
class Solution:

    def findSolution(self, z: int):

        res,functionid = [],1        
        for x in range(1, 1001):            
            left, right = 1, 1000                        
            while left <= right:                
                mid = (left + right) // 2                
                t = f(x, mid,functionid)                
                if t == z:                    
                    res.append([x, mid])                    
                    break                
                elif t > z:                    
                    right = mid - 1                
                elif t < z:                    
                    left = mid + 1                            
        return res


def f(x:int,y:int,functionid:int):
    if functionid == 1:
        return x+y
    if functionid==2:
        return x*y
    else:
        return x*x+y

if __name__ == "__main__":
    print(Solution().findSolution(5))
        
        
