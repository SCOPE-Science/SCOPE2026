#!/usr/bin/env python3
"""Exact optimal PZF starters in proper double stars of orders at most nine.

No nonstandard dependencies. Includes independent full labeled-state comparisons.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb
ONE = Fraction(1)
ZERO = Fraction(0)

@lru_cache(None)
def binom_row(m,p):
    assert 0 <= p <= 1
    return tuple(Fraction(comb(m,r))*p**r*(1-p)**(m-r)
                 for r in range(m+1))

def quotient_times(a,b):
    """Returns exact (hub-a, hub-b, leaf-a, leaf-b) expectations."""
    assert 2 <= a <= b
    @lru_cache(None)
    def both(i,j):
        if (i,j)==(a,b): return ZERO
        P=binom_row(a-i,Fraction(i+2,a+1)) if i<a else (ONE,)
        Q=binom_row(b-j,Fraction(j+2,b+1)) if j<b else (ONE,)
        numerator=ONE
        for r,s in product(range(len(P)),range(len(Q))):
            if r+s:
                numerator += P[r]*Q[s]*both(i+r,j+s)
        loop=P[0]*Q[0]
        assert loop < ONE
        return numerator/(ONE-loop)
    @lru_cache(None)
    def only_a(i):
        p=Fraction(i+1,a+1)
        P=binom_row(a-i,p)
        numerator=ONE
        for r in range(a-i+1):
            numerator+=P[r]*p*both(i+r,0)
            if r:
                numerator+=P[r]*(ONE-p)*only_a(i+r)
        loop=P[0]*(ONE-p)
        assert loop < ONE
        return numerator/(ONE-loop)
    @lru_cache(None)
    def only_b(j):
        p=Fraction(j+1,b+1)
        P=binom_row(b-j,p)
        numerator=ONE
        for r in range(b-j+1):
            numerator+=P[r]*p*both(0,j+r)
            if r:
                numerator+=P[r]*(ONE-p)*only_b(j+r)
        loop=P[0]*(ONE-p)
        assert loop < ONE
        return numerator/(ONE-loop)
    return (only_a(0),only_b(0),ONE+only_a(1),ONE+only_b(1))

def labeled_times(a,b):
    """Separate vertex-labeled Markov model; no quotient recurrence used."""
    n=a+b+2
    neighbors= [[1]+list(range(2,2+a)), [0]+list(range(2+a,n))]
    neighbors += [[0] for _ in range(a)]
    neighbors += [[1] for _ in range(b)]
    full=(1<<n)-1
    @lru_cache(None)
    def E(mask):
        if mask==full:return ZERO
        whites=[v for v in range(n) if not (mask>>v)&1]
        remain=[]
        for v in whites:
            q=ONE
            for u in neighbors[v]:
                if (mask>>u)&1:
                    p=Fraction(1+sum((mask>>w)&1 for w in neighbors[u]),len(neighbors[u]))
                    q*=ONE-p
            remain.append(q)
        loop=ONE
        for q in remain:loop*=q
        assert loop<ONE
        num=ONE
        for choice in range(1,1<<len(whites)):
            prob=ONE
            nextmask=mask
            for j,v in enumerate(whites):
                if (choice>>j)&1:
                    nextmask|=1<<v
                    prob*=ONE-remain[j]
                else:
                    prob*=remain[j]
            if prob:
                num+=prob*E(nextmask)
        return num/(ONE-loop)
    return E(1),E(2),E(1<<2),E(1<<(2+a))

def check():
    graph_types=[]
    for n in range(6,10):
        for a in range(2,(n-2)//2+1):
            b=n-a-2
            vals=quotient_times(a,b)
            winner=min(range(4),key=lambda j:vals[j])
            assert vals.count(vals[winner])==(2 if a==b else 1)
            assert winner==(0 if a==b else (3 if (a,b)==(2,5) else 1)), (a,b,winner)
            if a==b:
                assert vals[0]==vals[1] and vals[2]==vals[3] and vals[0]<vals[2]
            else:
                assert len(set(vals))==4
                assert vals[1]<vals[0] and vals[3]<vals[2]
                if (a,b)==(2,5):
                    assert vals[3]<vals[1]
                    assert vals[1]-vals[3]==Fraction(10821394247161847,236576000775098985)
                    assert Fraction(45,1000)<vals[1]-vals[3]<Fraction(46,1000)
                else:
                    assert vals[1]<vals[3]
            graph_types.append((a,b))
            print(f'D({a},{b}): winner',('both hubs','larger hub','smaller leaf','larger leaf')[winner],
                  'times', ', '.join(f'{float(v):.9f}' for v in vals))
    assert graph_types==[(2,2),(2,3),(2,4),(3,3),(2,5),(3,4)]
    for a,b in [(2,2),(2,3),(2,4),(2,5),(3,4)]:
        assert quotient_times(a,b)==labeled_times(a,b), (a,b)
        print('independent fully labeled exact state verification passed',a,b)
    print('PASS: six exact graph types, every source orbit, five independent labeled graph checks')

if __name__=='__main__':check()
