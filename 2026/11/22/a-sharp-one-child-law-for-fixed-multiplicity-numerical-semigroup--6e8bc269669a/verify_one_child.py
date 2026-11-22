#!/usr/bin/env python3
"""Exact, independent checks of fixed-multiplicity child counts."""
from itertools import combinations
from math import comb

def comps(g,d):
    for cuts in combinations(range(1,g),d-1):
        p=(0,)+cuts+(g,)
        yield tuple(p[i+1]-p[i] for i in range(d))

def valid(x):
    m=len(x)+1
    for i in range(1,m):
        for j in range(i,m):
            r=(i+j)%m
            if r and x[i-1]+x[j-1]+(i+j)//m < x[r-1]:
                return False
    return True

def children_kunz(x):
    m=len(x)+1
    w=[0]+[m*x[i-1]+i for i in range(1,m)]
    F=max(w)-m
    primes=[m]
    for r in range(1,m):
        u=w[r]
        primitive=True
        for i in range(1,m):
            j=(r-i)%m
            if j and w[i]+w[j]==u:
                primitive=False
                break
        if primitive:primes.append(u)
    return sum(u>F for u in primes)

def children_direct(x):
    m=len(x)+1
    w=[0]+[m*x[i-1]+i for i in range(1,m)]
    F=max(w)-m
    def member(u):return u>=w[u % m]
    count=0
    for u in range(1,F+m+1):
        if not member(u):continue
        if all(not (member(a) and member(u-a)) for a in range(1,u//2+1)):
            if u>F:count+=1
    return count

if __name__=='__main__':
    tested=0
    for m in range(2,7):
        for g in range(m-1,17):
            for x in comps(g,m-1):
                if valid(x):
                    a=children_kunz(x)
                    b=children_direct(x)
                    assert a==b,(m,g,x,a,b)
                    tested+=1
    print('INDEPENDENT_CHILDREN_OK',tested)
    for m in range(3,8):
        for g in (12,18,24,32):
            if g<m-1:continue
            ct=[0]*(m+1)
            for x in comps(g,m-1):
                if valid(x):ct[children_kunz(x)]+=1
            total=sum(ct)
            bad=total-ct[1]
            assert bad>0
            print('PROFILE',m,g,total,bad,round(g*bad/total,4),ct)
    print('VERIFY_OK')
