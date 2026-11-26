#!/usr/bin/env python3
"""Exact finite-state checks for the three-color excitable dynamics on triangle bouquets.
Run with Python 3; requires only the standard library.
"""
from collections import Counter
from itertools import combinations_with_replacement, product
from math import comb


def wing_step(h, pair):
    a, b = pair
    def f(x, neighbor):
        return (x+1) % 3 if x else int(h == 1 or neighbor == 1)
    return f(a, b), f(b, a)


def all_step(x):
    h=x[0]
    h_next=((h+1)%3) if h else int(1 in x[1:])
    out=[h_next]
    for j in range(1,len(x),2):
        out.extend(wing_step(h, (x[j],x[j+1])))
    return tuple(out)


def rainbow(h,pair):
    return len({h, *pair})==3


def direct_reductions():
    n=0
    types=list(combinations_with_replacement(range(3),2))
    for h in range(3):
        allowed=[p for p in types if not rainbow(h,p)]
        assert len(allowed)==5
        for bits in range(1,1<<5):
            support=frozenset(allowed[j] for j in range(5) if bits & (1<<j))
            hh=h; ss=support
            for t in range(4):
                h_next=(hh+1)%3 if hh else int(any(1 in p for p in ss))
                ss=frozenset(tuple(sorted(wing_step(hh,p))) for p in ss)
                hh=h_next
            assert (hh,ss)==(0,frozenset({(0,0)})),(h,support,hh,ss)
            n+=1
    print('NO_RAINBOW_SUPPORT_CASES', n)
    assert n==93
    m=0
    for h in range(3):
        for pair in product(range(3),repeat=2):
            p=pair
            for t in range(4):p=wing_step((h+t)%3,p)
            p4=p
            for t in range(4,7):p=wing_step((h+t)%3,p)
            assert p==p4,(h,pair,p,p4)
            hh=(h+4)%3
            canonical={1:{(0,0),(0,2),(2,0)},2:{(1,1),(1,0),(0,1)},0:{(2,2),(2,1),(1,2)}}[hh]
            assert p4 in canonical,(h,pair,p4)
            assert rainbow(h,pair)==rainbow(hh,p4)
            m+=1
    print('PERIODIC_HUB_WING_CASES',m)
    assert m==27


def exhaustive(r):
    n=2*r+1
    pows=[3**j for j in range(n)]
    N=3**n
    fixed=0
    three_cycles=set()
    basins=Counter()
    maxdepth=0
    for k in range(N):
        x=tuple((k//p)%3 for p in pows)
        y=x
        states=[y]
        for t in range(7):
            y=all_step(y)
            states.append(y)
        assert states[4]==states[7],(r,k,'not F^4=F^7')
        if states[4][0]==0 and all(c==0 for c in states[4]):
            orbit='zero'
        else:
            z=states[4]
            while z[0]!=1:
                z=all_step(z)
            assert all(z[j:j+2] in [(0,0),(0,2),(2,0)] for j in range(1,n,2))
            orbit=tuple(z)
            three_cycles.add(orbit)
        preperiod=next(t for t in range(5) if states[t]==states[t+3]) if orbit!='zero' else next(t for t in range(5) if states[t]==(0,)*n)
        maxdepth=max(maxdepth,preperiod)
        basins[orbit]+=1
        if x==all_step(x):fixed+=1
    assert fixed==1
    assert len(three_cycles)==3**r-1,(r,len(three_cycles))
    assert basins['zero']==3*7**r,(r,basins['zero'])
    for orbit in three_cycles:
        k=sum(orbit[j:j+2]!=(0,0) for j in range(1,n,2))
        assert basins[orbit]==3*7**(r-k),(r,orbit,basins[orbit])
    for k in range(1,r+1):
        assert sum(1 for orb in three_cycles if sum(orb[j:j+2]!=(0,0) for j in range(1,n,2))==k)==comb(r,k)*2**k
    assert maxdepth==(3 if r==1 else 4),(r,maxdepth)
    print(f'FULL_STATE_r={r}_states={N}_cycles={len(three_cycles)}_extinction_basin={basins["zero"]}_max_preperiod={maxdepth}_PASS')

if __name__=='__main__':
    direct_reductions()
    for r in range(1,6):exhaustive(r)
    print('VERIFY_OK')
