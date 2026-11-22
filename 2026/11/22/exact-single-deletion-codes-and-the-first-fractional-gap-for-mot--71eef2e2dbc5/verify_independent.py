#!/usr/bin/env python3
"""Independent binary-mask recursion for Motzkin deletion-code capacities."""
from itertools import product
from functools import lru_cache

CLAIMED=[(1,1),(2,1),(2,3),(4,8),(6,75),(14,28),(25,142560)]

def admissible(w):
    z=0
    for s in w:
        if s=='U':z+=1
        if s=='D':z-=1
        if z<0:return False
    return z==0

def maximum_and_count(group):
    k=len(group)
    cuts=[set() for _ in group]
    for j,w in enumerate(group):
        for i in range(len(w)):
            cuts[j].add(w[:i]+w[i+1:])
    neighbors=[0]*k
    for i in range(k):
        for j in range(k):
            if i!=j and cuts[i].intersection(cuts[j]):neighbors[i]|=1<<j
    @lru_cache(None)
    def solve(mask):
        if not mask:return (0,1)
        remaining=mask;target=-1;degree=-1
        while remaining:
            bit=remaining & -remaining
            j=bit.bit_length()-1
            remaining^=bit
            d=(neighbors[j]&mask).bit_count()
            if d>degree:target,degree=j,d
        without=mask & ~(1<<target)
        a,count_a=solve(without)
        b,count_b=solve(without & ~neighbors[target]);b+=1
        if a>b:return a,count_a
        if b>a:return b,count_b
        return a,count_a+count_b
    return solve((1<<k)-1)

def main():
    for n in range(1,8):
        L=[''.join(z) for z in product('FUD',repeat=n) if admissible(z)]
        tmax=n//2
        result=0
        count=1
        for t in range(tmax+1):
            group=[w for w in L if w.count('U')==t]
            maximum,ways=maximum_and_count(group)
            result+=maximum
            count*=ways
        assert (result,count)==CLAIMED[n-1],(n,result,count)
    print('ALTERNATE_OK')

if __name__=='__main__':main()
