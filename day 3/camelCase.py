import math
import os
import random
import re
import sys
def camelcase(s):
    # Write your code here
    word_count=1
    
    for char in s:
        if char.isupper():
            word_count+=1
    
    return word_count        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()