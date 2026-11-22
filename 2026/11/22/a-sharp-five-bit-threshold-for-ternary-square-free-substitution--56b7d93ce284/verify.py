#!/usr/bin/env python3
"""Exact finite verification of square-free ternary one-substitution code certificates."""
import itertools
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

BASE=Path(__file__).resolve().parent
C=json.loads((BASE/'CERTIFICATE.json').read_text(encoding='utf-8'))
ALPHABET='012'
TRANSFORMS=list(itertools.permutations(ALPHABET))

def squarefree(w):
    for half in range(1,len(w)//2+1):
        for start in range(len(w)-2*half+1):
            if w[start:start+half]==w[start+half:start+2*half]:
                return False
    return True

def words(n):
    return [''.join(t) for t in itertools.product(ALPHABET,repeat=n)
            if squarefree(''.join(t))]

def orbit(w):
    return {''.join(p[int(c)] for c in v)
            for p in TRANSFORMS for v in (w,w[::-1])}

def ball(w):
    z={w}
    for i,c in enumerate(w):
        for a in ALPHABET:
            if a!=c:
                z.add(w[:i]+a+w[i+1:])
    assert len(z)==1+2*len(w)
    return z

def dist(x,y):
    return sum(a!=b for a,b in zip(x,y))

assert [len(words(i)) for i in range(1,10)]==[3,6,12,18,30,42,60,78,108]
for n in (6,7):
    W=set(words(n)); pairs=C['perfect_matchings'][str(n)]
    assert len(pairs)==len(W)//2
    used=set()
    for a,b in pairs:
        assert a!=b and a in W and b in W and a not in used and b not in used
        assert 1<=dist(a,b)<=2
        used.update([a,b])
    assert used==W

# Every dual certificate is a nonnegative output-weight function invariant
# under symbol relabeling and reversal, with exact rational weights.
for n,total in ((8,Fraction(63,2)),(9,Fraction(48))):
    y={}
    for rep,num,den in C['dual'][str(n)]:
        assert len(rep)==n and den>0 and num>=0
        weight=Fraction(num,den)
        for v in orbit(rep):
            assert v not in y, (n,rep,v)
            y[v]=weight
    objective=sum(y.values(),Fraction(0))
    assert objective==total,(n,objective)
    W=words(n)
    for x in W:
        # Exact dual covering, independently re-created substitution outputs.
        covered=sum((y.get(v,Fraction(0)) for v in ball(x)),Fraction(0))
        assert covered>=1,(n,x,covered)
        assert covered==1,(n,x,covered)
    print(f'DUAL_{n}_OK source={len(W)} support={len(y)} value={total}')

code=set().union(*(orbit(x) for x in C['code_orbit_representatives_9']))
assert len(code)==48, len(code)
assert all(squarefree(w) for w in code)
assert all(dist(x,y)>=3 for i,x in enumerate(sorted(code)) for y in sorted(code)[:i])
assert len(set().union(*(ball(w) for w in code)))==48*(1+2*9)
print('CODE_9_OK size=48 min_distance>=3')
# n<=5: at most 30 square-free sources. n=6,7: certified perfect
# matchings of confusable pairs bound sizes by 21 and 30. n=8: 63/2
# rational upper bound gives capacity <=31. n=9: capacity exactly 48.
print('THRESHOLD_OK minimum_length_for_32_messages=9')
print('VERIFY_OK')
