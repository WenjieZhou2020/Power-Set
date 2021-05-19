#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 23:31:07 2021

@author: wenjiezhou
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 19:45:22 2021

@author: wenjiezhou
"""
#This mini project generates the powerset for two different ways.#
#The below function generates member of powerset of the input items one by one#

######## Approach 1
#key in name.__next__() at interactive mode console pannal to generate another member#
def PowerSet(items):
    """"This function generates the power set of input items"""
    for i in range(2**len(items)):
        combo = []
        for j in range(len(items)):# There is 2**N possible combinations, where N = len(items) 
            if ( i >> j ) % 2 == 1:
                combo.append(items[j])#test bit jthe of integer i 
        yield combo

foo = PowerSet(['Apple', 'Banana', 'Carrot'])
foo.__next__()
        

######## Approach 2
#The below function generates all powerset of the input items#
from itertools import chain, combinations

def powerset(iterable):
    """This function generates all possible powerset on the input items""" 
    """By directly call the itertools library"""
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    #if you want to avoide 0 length list, just change the range to (1,len(s)+1)
    # return chain.from_iterable(combinations(s, r) for r in range(1,len(s)+1))

powersetItems = list(powerset(['Apple', 'Banana', 'Carrot']))
print(powersetItems)









