#!/usr/bin/env python3
"""Exact finite checks for a two-coordinate knowing-whether event transformer."""
from itertools import combinations
from math import comb
from collections import Counter

def op(m, n, event):
    out = 0
    for i in range(m):
        row = sum(1 << (i*n+j) for j in range(n))
        if (event & row) in (0, row):
            out |= row
    for j in range(n):
        col = sum(1 << (i*n+j) for i in range(m))
        if (event & col) in (0, col):
            out |= col
    return out

def positions(m, n, event):
    rows = tuple(i for i in range(m) if len({(event >> (i*n+j)) & 1 for j in range(n)}) == 1)
    cols = tuple(j for j in range(n) if len({(event >> (i*n+j)) & 1 for i in range(m)}) == 1)
    return rows,cols

def cross(m, n, rows, cols):
    return sum(1 << (i*n+j) for i in range(m) for j in range(n) if i in rows or j in cols)

def H(a,b):
    return sum((-1)**(i+j)*comb(a,i)*comb(b,j)*2**((a-i)*(b-j)) for i in range(a+1) for j in range(b+1))

def brute_H(a,b):
    return sum(all(any((e>>(i*b+j))&1 for j in range(b)) for i in range(a))
            and all(any((e>>(i*b+j))&1 for i in range(a)) for j in range(b))
            for e in range(1 << (a*b)))

def run():
    total = 0
    for m,n in [(1,5),(2,2),(2,3),(3,3),(3,4),(4,3),(2,5),(5,2)]:
        full=(1 << (m*n))-1
        fibers=Counter()
        for e in range(full+1):
            x=op(m,n,e); y=op(m,n,x); z=op(m,n,y)
            assert y==z, (m,n,e,'stabilization')
            rows,cols=positions(m,n,e)
            assert x==cross(m,n,rows,cols)
            if 0<len(rows)<m and 0<len(cols)<n:
                assert y==x
            else:
                assert y==full
            fibers[y]+=1
            total+=1
        if min(m,n)<2:
            assert fibers==Counter({full:2**(m*n)})
            continue
        expected={full:2**(m*n)}
        for r in range(1,m):
            for rr in combinations(range(m),r):
                for c in range(1,n):
                    for cc in combinations(range(n),c):
                        x=cross(m,n,rr,cc)
                        assert x not in expected
                        count=2*H(m-r,n-c)
                        expected[x]=count
                        expected[full]-=count
        assert dict(fibers)==expected, (m,n,'fiber mismatch')
        assert sum(expected.values())==2**(m*n)
        assert len(expected)==1+(2**m-2)*(2**n-2)
        for a in range(1,m):
            for b in range(1,n):
                assert H(a,b)==brute_H(a,b)
    # Cross-check the two-A_ij intersections for n<=4 by exact masks.
    for n in (2,3,4):
        all_masks=1<<(n*n)
        def ispair(event,i,j):
            row=[(event >> (i*n+k))&1 for k in range(n)]
            col=[(event >> (k*n+j))&1 for k in range(n)]
            return len(set(row))==len(set(col))==1
        pairs=list((i,j) for i in range(n) for j in range(n))
        for (i,j),(k,l) in combinations(pairs,2):
            count=sum(ispair(e,i,j) and ispair(e,k,l) for e in range(all_masks))
            exponent=3-3*n if (i==k or j==l) else 5-4*n
            assert count==2**(n*n+exponent), (n,i,j,k,l,count,exponent)
    print('VERIFY_OK', 'event_checks',total)

if __name__=='__main__':
    run()
