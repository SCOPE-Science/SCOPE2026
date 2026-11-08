#!/usr/bin/env python3
"""Exact independent checks of residue-profile length classification in M(1,10).

Run: python3 verify.py (Python standard library only).
The mathematical proof is unrestricted; these checks are finite corroboration.
"""
from functools import lru_cache
from math import isqrt

ATOMS = ((4,0,0),(0,4,0),(1,1,0),(0,0,2),(2,0,1),(0,2,1))
PATTERNS = ((2,2,2),(2,4,1),(4,2,1),(4,4,0))

def predicts(a,b,c):
    return any(a>=u and b>=v and c>=w for u,v,w in PATTERNS)

@lru_cache(None)
def vector_lengths(v):
    if v == (0,0,0):
        return frozenset((0,))
    out = set()
    for u in ATOMS:
        if all(v[i]>=u[i] for i in range(3)):
            for k in vector_lengths(tuple(v[i]-u[i] for i in range(3))):
                out.add(k+1)
    return frozenset(out)

checked = 0
for a in range(25):
    for b in range(25-a):
        for c in range(25-a-b):
            if (a-b+2*c)%4:
                continue
            found = len(vector_lengths((a,b,c)))>1
            assert found == predicts(a,b,c), ((a,b,c),found,predicts(a,b,c))
            checked += 1
assert vector_lengths((4,2,1)) == frozenset((2,3))

LIMIT=200000
lengths={1:frozenset((0,))}
first=[]
count=0
for n in range(11,LIMIT+1,10):
    poss=set()
    for d in range(11,isqrt(n)+1,10):
        if n%d==0:
            q=n//d
            if q%10==1:
                for u in lengths[d]:
                    for v in lengths[q]:
                        poss.add(u+v)
    lengths[n] = frozenset(poss) if poss else frozenset((1,))
    if len(lengths[n])>1:
        first.append(n)
        count+=1
assert first[0]==75411 and lengths[75411]==frozenset((2,3)),first[:5]
assert (81*931,21*21*171)==(75411,75411)
assert all(lengths[x]==frozenset((1,)) for x in (21,81,171,931))
minimums = [3**a*7**b*19**c for a,b,c in PATTERNS]
assert min(minimums)==75411 and sorted(minimums)==[75411,159201,194481,410571]
print('VERIFY_OK')
print('exact_residue_profiles_total_weight_le_24=',checked)
print('monoid_elements_examined=',len(lengths)-1)
print('first_disparate_length_elements=',first[:5])
print('first_element_lengths=',sorted(lengths[75411]))
print('independent_witness=81*931=21*21*171=75411')
print('threshold_minimal_values=',sorted(minimums))
