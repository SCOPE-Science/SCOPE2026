#!/usr/bin/env python3
"""Exact two-pentagon transfer certificate for the three-state icosahedral Potts model.

Convention: vertices N,S, upper and lower rings U_i,V_i (indices mod 5).
The intra-column edges are N-U_i, S-V_i, U_i-V_i; between
columns i-1 and i are U_(i-1)-U_i, V_(i-1)-V_i, and U_i-V_(i-1).
"""
from collections import defaultdict
from itertools import product

EXPECTED_MIN = (10,8,6,4,3,4,5,8,11,15,20,25,30)
EXPECTED_COUNT = (72,600,1260,360,120,360,120,480,240,160,144,24,1)

def d(a,b):
    return int(a == b)

def onsite(s, north, south):
    u,v = s
    return d(u,north)+d(v,south)+d(u,v)

def between(s,t):
    u,v = s
    un,vn = t
    return d(u,un)+d(v,vn)+d(un,v)

def compute():
    levels = defaultdict(int)
    states = list(product(range(3),repeat=2))
    for north in range(3):
      for south in range(3):
       for start in states:
        k = d(north,0)+d(south,0)+d(start[0],0)+d(start[1],0)
        b = onsite(start,north,south)
        dp = {(start,k,b):1}
        for col in range(1,5):
          ndp=defaultdict(int)
          for (previous,kk,bb),ways in dp.items():
            for current in states:
              nk=kk+d(current[0],0)+d(current[1],0)
              nb=bb+onsite(current,north,south)+between(previous,current)
              ndp[(current,nk,nb)]+=ways
          dp=ndp
        for (last,kk,bb),ways in dp.items():
          levels[(kk,bb+between(last,start))]+=ways
    return levels

def main():
    levels=compute()
    assert sum(levels.values())==3**12
    assert len(levels)>100
    mins=tuple(min(b for (k,b) in levels if k==i) for i in range(13))
    counts=tuple(levels.get((i,mins[i]),0) for i in range(13))
    assert mins==EXPECTED_MIN,(mins,EXPECTED_MIN)
    assert counts==EXPECTED_COUNT,(counts,EXPECTED_COUNT)
    # Every vertex coloring appears exactly once in this transfer representation.
    assert sum(1 for k,b in levels if levels[k,b] != 0)>0
    print('TRANSFER_EXACT_OK',sum(levels.values()),list(zip(mins,counts)))
if __name__=='__main__':main()
