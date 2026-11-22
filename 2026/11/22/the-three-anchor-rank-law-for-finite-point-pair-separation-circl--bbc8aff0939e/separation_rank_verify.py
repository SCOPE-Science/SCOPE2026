#!/usr/bin/env python3
"""Independent finite extension-type game and exact cyclic-gap count checks.

Pure 4-ary alternation relation; no rank formula is used in the game solver.
"""
from functools import lru_cache
from itertools import combinations
from math import comb


def alt(a, b, c, d):
    """True precisely when pair (a,c) alternates with pair (b,d)."""
    if len({a,b,c,d}) != 4:
        return False
    order = sorted((a,b,c,d))
    return (order.index(a) - order.index(c)) % 2 == 0


def fingerprint(F, x, position):
    bits=[]
    for a,b,c in combinations(F,3):
        p = position
        bits.extend((alt(p[a],p[b],p[c],p[x]),
                     alt(p[a],p[c],p[b],p[x]),
                     alt(p[b],p[a],p[c],p[x])))
    return tuple(bits)


def possible_extensions(F):
    m=len(F)
    if m<3:
        return {()}
    abstract={a:2*i for i,a in enumerate(F)}
    forms=set()
    for j in range(m):
        here=dict(abstract)
        here['*']=2*j+1
        forms.add(fingerprint(F, '*', here))
    assert len(forms)==m, (m, len(forms))
    return forms


def brute_rank(n):
    points=tuple(range(n))
    pos={i:i for i in points}
    @lru_cache(None)
    def rank(mask):
        F=tuple(i for i in points if (mask>>i)&1)
        possible=possible_extensions(F)
        actual={}
        for x in points:
            if (mask>>x)&1: continue
            typ=fingerprint(F,x,pos)
            actual[typ]=max(actual.get(typ,-1),rank(mask | (1<<x)))
        assert set(actual).issubset(possible), (n,F,actual,possible)
        if not possible.issubset(actual): return 0
        return 1+min(actual[t] for t in possible)
    output=rank(0)
    for mask in range(1<<n):
        F=[i for i in points if (mask>>i)&1]
        if len(F)>=3:
            gaps=[((F[(j+1)%len(F)]-F[j]-1)%n) for j in range(len(F))]
            expected=min((g+1).bit_length()-1 for g in gaps)
            assert rank(mask)==expected, (n,F,gaps,rank(mask),expected)
    expected = n if n<=2 else 3+(n//3).bit_length()-1
    assert output==expected, (n,output,expected)
    return output


def check_counting(n):
    for m in range(3,n+1):
        for k in range(0,5):
            count=0
            for F in combinations(range(n),m):
                gaps=[(F[(j+1)%m]-F[j]-1)%n for j in range(m)]
                if all(g>=2**k-1 for g in gaps): count+=1
            if n<m*(2**k): predicted=0
            else:
                numerator=n*comb(n-m*2**k+m-1,m-1)
                assert numerator % m==0
                predicted=numerator//m
            assert count==predicted,(n,m,k,count,predicted)


def main():
    for n in range(0,12):
        got=brute_rank(n)
        print('EXACT_GAME',n,got)
    for n in range(3,17):
        check_counting(n)
    print('ALL_CHECKS_OK', 'game_n_max=11', 'count_n_max=16')

if __name__=='__main__': main()
