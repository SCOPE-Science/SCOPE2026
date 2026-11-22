#!/usr/bin/env python3
"""Verify two infinite-formula conjectures against exhaustive small Kunz vectors."""
from itertools import product

def kunz_ok(x):
    m = len(x) + 1
    y = (0,) + tuple(x)
    return all(y[i] + y[j] + (i+j)//m >= y[(i+j)%m]
               for i in range(1,m) for j in range(1,m))

def candidates(m,r):
    F = 3*m+r
    choices = [((4,) if i==r else tuple(range(1,(F+m-i)//m+1)))
               for i in range(1,m)]
    for x in product(*choices):
        if kunz_ok(x):
            yield x

def predicted(m,r):
    x = [0]*m
    x[r]=4
    if r==2: x[1]=2
    remaining = list(range(r+1,m))
    pairs=[]
    while remaining:
        i=remaining.pop(0)
        j=m+r-i
        if i==j:
            x[i]=2
        else:
            remaining.remove(j)
            pairs.append((i,j))
    for bits in product((0,1),repeat=len(pairs)):
        y=x[:]
        for (i,j),bit in zip(pairs,bits):
            y[i],y[j] = ((1,2) if bit==0 else (2,1))
        yield tuple(y[1:])

def independently_check_membership(m,r,x):
    F=3*m+r
    bound=F+2*m+2
    S={0}
    S.update(n for n in range(1,bound+1) if n%m==0)
    for i,xi in enumerate(x,1):
        S.update(range(m*xi+i,bound+1,m))
    assert min(S-{0})==m
    assert max(set(range(bound+1))-S)==F
    assert len(set(range(F+1))-S)==sum(x)
    for a in S:
        for b in S:
            if a+b<=bound:
                assert a+b in S

case_count=0
for r in (1,2):
    for m in range(max(2,r+1),12):
        all_good=list(candidates(m,r))
        least=min(map(sum,all_good))
        minimizers={x for x in all_good if sum(x)==least}
        expected=set(predicted(m,r))
        assert minimizers==expected,(m,r,least,len(minimizers),len(expected))
        assert len(expected)==2**((m-r-1)//2)
        assert least==(3*m+r+2)//2
        for x in expected:
            independently_check_membership(m,r,x)
        case_count+=1
assert case_count==19
print('TWO_LINE_KUNZ_VERIFY_OK',case_count)
