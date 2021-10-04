#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def combination(n,r):
    return int(math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))

def sherlockAndAnagrams(s):
    # Write your code here
    di={}
    count=0
    for i in range(0,len(s)):
        for j in range(i,len(s)):
            st = sorted(s[i:(j+1)])
            st = "".join(st)
            if (di.get(st)==None):
                di[st]=1    
            else:
               di[st]=di.get(st)+1
    for irr in di.values():
        if irr > 1:
            count+=combination(irr,2)
            
    return count
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
