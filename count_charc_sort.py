#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    
    d = dict() 
    for char in s :
        d[char] = d.get(char,0) + 1
        
    sorted_items = sorted( d.items() , key =lambda  item :(-item [1], item[0])   )
    
    for char, freq in sorted_items[:3] :
        print (char, freq)
        
    
                
            
