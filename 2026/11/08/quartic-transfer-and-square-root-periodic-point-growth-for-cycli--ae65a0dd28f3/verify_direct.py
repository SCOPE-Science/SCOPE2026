#!/usr/bin/env python3
"""Exhaustively enumerate edge gaps in [-3,3] on cyclic rings.
Bound 3 is proved in RESULT.md for all initially recurrent states.
"""
from itertools import product

def update(x):
    n=len(x)
    return tuple(x[i]+(x[(i-1)%n]>x[i])+(x[(i+1)%n]>x[i])
                 -(x[(i-1)%n]<x[i])-(x[(i+1)%n]<x[i])
                 for i in range(n))

def count(n):
    count=0
    for gaps in product(range(-3,4),repeat=n-1):
        final=-sum(gaps)
        if not -3<=final<=3:continue
        x=[0]
        for d in gaps:x.append(x[-1]-d)
        x=tuple(x)
        if update(update(x))==x:count+=1
    return count

def main():
    expected={3:19,4:47,5:171,6:517,7:1793,8:5927}
    for n,goal in expected.items():
        got=count(n)
        assert got==goal,(n,got,goal)
        print(f'C_{n}={got}: direct iteration OK')
    print('DIRECT_OK')
if __name__=='__main__':main()
