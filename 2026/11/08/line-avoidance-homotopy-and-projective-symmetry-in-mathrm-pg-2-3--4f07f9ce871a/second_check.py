#!/usr/bin/env python3
"""Second finite-field model and reverse-pivot Morse check for PG(2,3)."""
from functools import cache
from collections import Counter
from itertools import combinations
P=[(1,a,b) for a in range(3) for b in range(3)]
P += [(0,1,b) for b in range(3)]+[(0,0,1)]
assert len(P)==13

def normalize(q):
    z=next(x for x in q if x%3)
    inv=1 if z%3==1 else 2
    return tuple((inv*x)%3 for x in q)

def cross(a,b):
    return normalize((a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]))
L={cross(a,b) for a,b in combinations(P,2)}
assert len(L)==13
BLOCK={sum(1<<i for i,p in enumerate(P) if sum(x*y for x,y in zip(l,p))%3==0) for l in L}
assert len(BLOCK)==13
F=set()
def expand(m,i):
    F.add(m)
    for j in range(i,13):
        b=m|(1<<j)
        if all((b&line)!=line for line in BLOCK):expand(b,j+1)
expand(0,0)
assert len(F)==4330
remaining=set(F);pairs=[]
for j in reversed(range(13)):
    bit=1<<j
    for m in sorted(remaining):
        if m in remaining and not m&bit and (m|bit) in remaining:
            remaining.remove(m)
            remaining.remove(m|bit)
            pairs.append((m,m|bit))
assert len(pairs)==2145
assert Counter(x.bit_count()-1 for x in remaining)=={5:1,6:39}
lower_to_upper=dict(pairs)
upper_to_lower={b:a for a,b in pairs}

def boundary(m):
    s=1
    for j in range(13):
        if m & (1<<j):
            yield m^(1<<j),s
            s=-s
crit5=next(m for m in remaining if m.bit_count()==6)
critical6=[m for m in remaining if m.bit_count()==7]
@cache
def shrink(face):
    if face==crit5:return 1
    if face in upper_to_lower:return 0
    up=lower_to_upper[face]
    coeff=dict(boundary(up))[face]
    return -coeff*sum(s*shrink(other) for other,s in boundary(up) if other!=face)
coeff=[sum(s*shrink(lo) for lo,s in boundary(c6)) for c6 in critical6]
assert coeff==[0]*39
print('line_model_from_pairwise_cross_products=13')
print('reverse_pivot_pair_count=2145')
print('reverse_pivot_critical_dimensions=5:1 6:39')
print('reverse_pivot_integer_boundary=all_zero')
print('SECOND_CHECK_PASS')
