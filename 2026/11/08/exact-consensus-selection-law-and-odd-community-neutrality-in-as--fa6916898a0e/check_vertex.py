#!/usr/bin/env python3
"""Independent full-labelled-state exact absorption calculation; no count-state transitions used."""
from fractions import Fraction
from functools import lru_cache
from check_exact import race
from itertools import product

def check(m,n):
    N=m+n
    neighbors=[tuple(range(m,N)) for _ in range(m)]+[tuple(range(m)) for _ in range(n)]
    @lru_cache(None)
    def absorption(bits):
        moves=[]
        for v in range(N):
            ones=sum(bits[w] for w in neighbors[v]); degree=len(neighbors[v]);new=bits[v]
            if 2*ones>degree:new=1
            elif 2*ones<degree:new=0
            if new!=bits[v]:
                y=list(bits);y[v]=new;moves.append(tuple(y))
        if not moves:
            if all(z==0 for z in bits):return Fraction(0)
            if all(z==1 for z in bits):return Fraction(1)
            return Fraction(0)
        vals=[absorption(y) for y in moves]
        return sum(vals,Fraction(0))/len(vals)
    checked=0
    for bits in product((0,1),repeat=N):
        expected=race(m,n,sum(bits[:m]),sum(bits[m:]))
        result=absorption(bits)
        assert expected==result,(m,n,bits,expected,result)
        checked+=1
    return checked

if __name__=='__main__':
    total=0;instances=0
    for m in range(1,7):
      for n in range(1,7):
        if m+n>10: continue
        total+=check(m,n);instances+=1
    print('PASS: labelled-state exact absorption matched formula in',total,'states across',instances,'graphs')
