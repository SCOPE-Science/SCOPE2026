"""Independent finite-field exact enumeration of coordinate-pairing plane intersections.
Requires Python 3 standard library only. Run: python3 verify_planes.py
"""
from itertools import product
from collections import Counter

def matchings(indices):
    if not indices:
        yield ()
        return
    a, *rest = indices
    for j, b in enumerate(rest):
        for other in matchings(rest[:j]+rest[j+1:]):
            yield ((a,b),)+other

MATCHINGS=list(matchings(list(range(6))))
assert len(MATCHINGS)==15 and len(set(MATCHINGS))==15

def canon(p, q):
    j=next(i for i,v in enumerate(p) if v%q)
    t=pow(p[j],-1,q)
    return tuple((a*t)%q for a in p)

def count_plane_incidence(q):
    counter=Counter()
    for matching in MATCHINGS:
        for abc in product(range(q),repeat=3):
            if abc==(0,0,0):
                continue
            vec=[0]*6
            for (i,j),t in zip(matching,abc):
                vec[i],vec[j]=t,(-t)%q
            counter[(canon(vec,q),matching)] = 1
    multiplicity=Counter()
    points=Counter()
    for p,m in counter:
        points[p]+=1
    multiplicity=Counter(points.values())
    predicted={1:15*(q-2)*(q-3),2:45*(q-2),3:15,6:10}
    assert multiplicity==predicted,(q,multiplicity,predicted)
    total=sum(multiplicity.values())
    assert total==15*q*q-30*q+25
    assert sum(k*v for k,v in multiplicity.items())==15*(q*q+q+1)
    print('q',q,'multiplicity',dict(sorted(multiplicity.items())),'total',total)

for q in (5,7,11,13):
    count_plane_incidence(q)
print('PASS')
