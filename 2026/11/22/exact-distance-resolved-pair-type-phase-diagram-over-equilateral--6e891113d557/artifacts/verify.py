#!/usr/bin/env python3
"""Independent finite-diagram enumeration for distance-resolved ordered pair types."""
from itertools import product

def unary_valid(p, old_distance):
    return all(abs(p[i]-p[j]) <= old_distance <= p[i]+p[j]
               for i in range(len(p)) for j in range(i+1, len(p)))

def pair_valid(p,q,s):
    return all(abs(a-b) <= s <= a+b for a,b in zip(p,q))

def formula(n,delta):
    if delta == 1:
        return (2*4**n+2*3**n-4*2**n+1,
                4*4**n-4*2**n+1,
                3*4**n+3**n-4*2**n+1)
    if delta == 2: return (7**n, 9**n, 8**n)
    return (4**n+3*n*4**(n-1)+(n*(n-1)*4**(n-2) if n>=2 else 0),
            (2**n+n*2**(n-1))**2,
            4**n+4*n*4**(n-1)+n*(n-1)*4**(n-1))

def unary_formula(n,delta):
    return {1:2**(n+1)-1,2:3**n,3:2**n+n*2**(n-1)}[delta]

def main():
    diagrams=0
    for n in range(1,6):
        words=list(product((1,2,3),repeat=n))
        for delta in (1,2,3):
            types=[p for p in words if unary_valid(p,delta)]
            assert len(types)==unary_formula(n,delta), (n,delta,len(types))
            got=[]
            for s in (1,2,3):
                ct=sum(pair_valid(p,q,s) for p in types for q in types)
                diagrams+=len(types)**2
                got.append(ct)
            assert tuple(got)==formula(n,delta),(n,delta,got,formula(n,delta))
            if delta==1: assert got[0]+got[1]==2*got[2]
            print('n',n,'delta',delta,'unary',len(types),'ordered_pairs_by_distance',*got)
    print('DIAGRAM_CHECKS',diagrams)
    print('VERIFY_OK')
if __name__=='__main__': main()
