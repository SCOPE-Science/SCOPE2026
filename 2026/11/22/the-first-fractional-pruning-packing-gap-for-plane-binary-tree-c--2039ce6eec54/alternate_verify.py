#!/usr/bin/env python3
"""Independent bottom-up tree decomposition and exact certificate checks."""
import json
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

LEAF='.'
@lru_cache(None)
def shapes(n):
    if n==0:return (LEAF,)
    return tuple('('+a+','+b+')' for left in range(n)
                 for a in shapes(left) for b in shapes(n-left-1))

def split_top(t):
    if t==LEAF:return None
    assert t[0]=='(' and t[-1]==')'
    depth=0
    for i,c in enumerate(t):
        if c=='(':depth+=1
        elif c==')':depth-=1
        elif c==',' and depth==1:
            return t[1:i],t[i+1:-1]
    raise ValueError(t)

@lru_cache(None)
def deleted(t):
    child=split_top(t)
    if child is None:return frozenset()
    a,b=child
    out=set()
    if a==LEAF:out.add(b)
    else:out.update('('+v+','+b+')' for v in deleted(a))
    if b==LEAF:out.add(a)
    else:out.update('('+a+','+v+')' for v in deleted(b))
    return frozenset(out)

def run():
    d=json.loads(Path(__file__).with_name('certificates.json').read_text())['lengths']
    for n in range(1,7):
        c=d[str(n)]
        t=shapes(n);o=shapes(n-1)
        assert t==tuple(c['source_words'])
        assert o==tuple(c['output_words'])
        incidence=c['deletion_incidence']
        assert all({o[j] for j in inc}==deleted(word) for word,inc in zip(t,incidence))
        weights={j:F(v) for j,v in c['fractional_dual']}
        lower={j:F(v) for j,v in c['fractional_primal']}
        assert all(sum(weights.get(i,0) for i in inc)>=1 for inc in incidence)
        assert all(sum(lower.get(j,0) for j,inc in enumerate(incidence) if i in inc)<=1 for i in range(len(o)))
        assert sum(weights.values())==sum(lower.values())
        assert sum(weights.values())==F(c['fractional_optimum'])
        C=c['codeword_indices']
        assert len(set(C))==len(C)
        assert not any(set(incidence[x])&set(incidence[y]) for ix,x in enumerate(C) for y in C[ix+1:])
        assert len(C)==c['integer_optimum']==sum(weights.values()).numerator//sum(weights.values()).denominator
    print('ALTERNATE_OK')
if __name__=='__main__':run()
