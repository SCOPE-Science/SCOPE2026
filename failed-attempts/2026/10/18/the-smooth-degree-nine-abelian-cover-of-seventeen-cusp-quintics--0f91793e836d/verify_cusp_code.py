#!/usr/bin/env python3
"""Exact combinatorial checks for the 17-cusp quintic ternary code."""
from itertools import product
from collections import Counter

def wt(v): return sum(bool(x) for x in v)
def plus(v,w,s=1): return tuple((x+s*y)%3 for x,y in zip(v,w))

def check():
    assert 12+4+2 == 18 > 17 # ternary Griesmer bound for [17,3,12]
    good=[]
    # Up to coordinate scalings, two 12-support vectors with 7 overlap
    for signs in product((1,2),repeat=7):
        a = (1,)*12+(0,)*5
        b = signs+(0,)*5+(1,)*5
        assert wt(a)==wt(b)==12
        weights=tuple(sorted((wt(plus(a,b)), wt(plus(a,b,-1)))))
        if set(weights).issubset({12,15,18}):
            good.append((signs.count(1),weights))
    assert len(good)==42
    assert Counter(good)=={(2,(12,15)):21,(5,(12,15)):21}
    # Standard 2+5+5+5 partition: two triple points, pair-only blocks
    a=(1,)*2+(1,)*5+(1,)*5+(0,)*5
    b=(1,)*2+(2,)*5+(0,)*5+(1,)*5
    spectrum=Counter(wt(plus((0,)*17,plus(tuple((c*x)%3 for x in a),tuple((d*y)%3 for y in b)))) for c in range(3) for d in range(3))
    assert spectrum == {0:1,12:6,15:2},spectrum
    supportsets={frozenset(i for i,x in enumerate(plus(tuple((0,)*17),plus(tuple((c*x)%3 for x in a),tuple((d*y)%3 for y in b)))) if x) for c in range(3) for d in range(3)}
    assert len(supportsets)==5
    twelves=[s for s in supportsets if len(s)==12]
    assert len(twelves)==3
    assert len(set.intersection(*map(set,twelves)))==2
    assert {len(u&v) for i,u in enumerate(twelves) for v in twelves[i+1:]}=={7}
    assert sorted(len(s) for s in supportsets)==[0,12,12,12,15]
    # Orthogonality verifies 3-divisibility geometry (weight divisible by three).
    assert sum(x*y for x,y in zip(a,b))%3==0
    print('CUSPIDAL_17_CODE_AND_TOPOLOGY_COMBINATORICS_OK')
    print('vector_weights:',dict(sorted(spectrum.items())))
    print('intersection_profile: 2+5+5+5; all three pairwise intersections seven')
if __name__=='__main__':check()
