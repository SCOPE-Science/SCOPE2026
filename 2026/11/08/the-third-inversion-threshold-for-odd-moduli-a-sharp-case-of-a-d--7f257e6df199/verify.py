#!/usr/bin/env python3
"""Reproducible integer checks for the third distinct inversion minimum (odd moduli)."""
from functools import lru_cache
from math import gcd

@lru_cache(maxsize=None)
def inversion_reciprocity(a, b):
    assert 1 <= a < b and gcd(a, b) == 1
    if a == 1:
        return 0
    r = b % a
    n = (a-1)*(b-1)*(a+b-1)-4*b*inversion_reciprocity(r, a)
    assert n % (4*a) == 0
    return n//(4*a)

def inversion_direct(a, b):
    p = [a*j % b for j in range(1,b)]
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def main():
    direct_rows=direct_entries=rows=entries=equalities=0
    for b in range(7,1002,2):
        values = {}
        for a in range(1,b):
            if gcd(a,b)>1: continue
            v=inversion_reciprocity(a,b)
            values[a]=v;entries+=1
            if b<=103:
                assert v==inversion_direct(a,b),(a,b,v)
                direct_entries+=1
            assert v == inversion_reciprocity(pow(a,-1,b),b)
            if a not in (1,2,(b+1)//2):
                assert 6*v >= (b+1)*(b-2),(a,b,v)
                iseq=(6*v ==(b+1)*(b-2))
                expectation=(b%3==2 and a in (3,(b+1)//3))
                assert iseq == expectation,(a,b,iseq,expectation)
                if iseq:equalities+=1
        distinct=sorted(set(values.values()))
        assert len(distinct)>=3 and distinct[:2]==[0,(b*b-1)//8]
        assert 6*distinct[2]>=(b+1)*(b-2)
        assert (6*distinct[2]==(b+1)*(b-2))==(b%3==2 and b>=11)
        rows+=1
        if b<=103:direct_rows+=1
    print('VERIFY_OK odd_moduli=7..1001 rows=',rows,'unit_entries=',entries,
          'direct_rows=',direct_rows,'direct_entries=',direct_entries,
          'threshold_equalities=',equalities,'reciprocity=PASS',
          'independent_inversion_enumeration=PASS','third_distinct_bound=PASS',
          'equality_classification=PASS')

if __name__=='__main__':main()
