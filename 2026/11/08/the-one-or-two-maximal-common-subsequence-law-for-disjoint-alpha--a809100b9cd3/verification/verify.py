#!/usr/bin/env python3
"""Standalone exhaustive check for a theorem on two conjugate word powers."""
from itertools import product

def subwords(word):
    seen={''}
    for c in word:
        seen |= {s+c for s in tuple(seen)}
    return seen

def is_subword(z, x):
    it=iter(x)
    return all(any(c==wanted for c in it) for wanted in z)

def maximal_common(X,Y):
    common = subwords(X)&subwords(Y)
    alphabet = set(X+Y)
    return {v for v in common if not any(v[:j]+c+v[j:] in common for j in range(len(v)+1) for c in alphabet)}

def predicted(A,B,r,s):
    X=(A+B)*r;Y=(B+A)*s
    if r<s: return {X}
    if r>s: return {Y}
    return {B+(A+B)*(r-1),A+(B+A)*(r-1)}

def check(A,B,r,s):
    X=(A+B)*r;Y=(B+A)*s
    actual=maximal_common(X,Y)
    expect=predicted(A,B,r,s)
    assert actual==expect, (A,B,r,s,actual,expect)
    if r==s:
        common=subwords(X)&subwords(Y)
        U,V=tuple(expect)
        assert common==subwords(U)|subwords(V), (A,B,r,s)
    return len(subwords(X)&subwords(Y))

if __name__=='__main__':
    cases=0; listed=0
    blocks=[[''.join(x) for n in range(1,4) for x in product(alph, repeat=n)] for alph in ('ab','cd')]
    for A in blocks[0]:
      for B in blocks[1]:
        for r,s in product(range(1,4),repeat=2):
          if max(r,s)*(len(A)+len(B))>13: continue
          listed+=check(A,B,r,s)
          cases+=1
    # A second fixed-length stress case with arbitrary repeated block patterns.
    for A,B in [('ababa','cdd'),('aab','cdcd'),('abb','cddc'),('aaa','cccc'),('ab','ccdd')]:
      for r,s in product(range(1,3),repeat=2):
        listed+=check(A,B,r,s);cases+=1
    print('PASS',cases,'cases;',listed,'common subsequence strings checked')
