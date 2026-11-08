"""Independent enumeration of point incidence by projective coordinates.
Requires Python 3 standard library only. Run: python3 verify_combinatorics.py
"""
from collections import Counter
from itertools import product
from math import factorial

def matched_multiplicity(x,q):
    c=Counter(x)
    if c[0]%2: return 0
    for a in range(1,q):
        if c[a]!=c[-a%q]: return 0
    z=c[0]
    d=1
    for j in range(z-1,0,-2): d*=j
    for a in range(1,q):
        b=-a%q
        if a<b: d*=factorial(c[a])
    return d

def points_projective(q):
    for k in range(6):
        for rest in product(range(q), repeat=5-k):
            yield (0,)*k+(1,)+rest

for q in (5,7):
    measured=Counter()
    for vec in points_projective(q):
        mu=matched_multiplicity(vec,q)
        if mu:
            assert sum(v*v*v for v in vec)%q ==0
            measured[mu]+=1
    predicted={1:15*(q-2)*(q-3),2:45*(q-2),3:15,6:10}
    assert measured==predicted,(q,measured,predicted)
    print('q',q,'independent count',dict(sorted(measured.items())))
print('PASS')
