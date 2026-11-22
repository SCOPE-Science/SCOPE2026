#!/usr/bin/env python3
"""Exhaustive, direct two-step descendant test; no external dependencies."""
from itertools import product

def rc_step(word):
    return {word[:i+1]+(word[i]^1,)+word[i+1:] for i in range(len(word))}

def direct(word):
    return set().union(*(rc_step(y) for y in rc_step(word)))

def statistic(word):
    c=0; previous_run_letter=None; last=word[0]; r=1
    for a in word[1:]:
        if a==last:r+=1
        else:
            if previous_run_letter is not None and last==(previous_run_letter^1): c+=r
            previous_run_letter=last; last=a; r=1
    if previous_run_letter is not None and last==(previous_run_letter^1):c+=r
    return c

def check(q,max_n):
    total=0
    for n in range(1,max_n+1):
        for word in product(range(q),repeat=n):
            val=len(direct(word))
            target=n*(n+3)//2-statistic(word)
            assert val==target,(q,n,word,val,target)
            total+=1
    print('PASS direct',q,max_n,total)

if __name__=='__main__':
    check(2,10);check(4,7);check(6,5)
