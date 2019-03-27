#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys
# global result
# result=0
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # c = []
    # result = 0
    # for a in ar:
    #     b=ar.pop(a)
    #     if b in ar and b not in c:
    #         c.append(b)
    # result=len(c)    
    c = Counter(ar)
    result = 0
    for i in c: 
        j = c[i]//2
        result +=j
    
    # for i in ar

    return result
if __name__ == '__main__':
    

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(str(result) + '\n')

    
