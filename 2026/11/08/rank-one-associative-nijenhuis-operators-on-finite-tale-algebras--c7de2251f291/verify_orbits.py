#!/usr/bin/env python3
"""Independent canonical-parameter orbit census for rank-one Nijenhuis maps.
Works over arbitrary prime power q via support combinatorics; exact integers.
"""
import itertools
from collections import Counter

def parameters(q,degrees):
    r=len(degrees); singles=[i for i,d in enumerate(degrees) if d==1]
    for c in range(1,q):
        for mask in range(1,1<<r):
            for i in singles:
                if mask>>i&1:
                    yield (c,mask,i,-1)
                    for j in singles:
                        if not(mask>>j&1): yield(c,mask,i,j)

def permutations(degrees):
    groups=[]
    for deg in sorted(set(degrees)):
        groups.append([i for i,d in enumerate(degrees) if d==deg])
    for choices in itertools.product(*(itertools.permutations(g) for g in groups)):
        p=list(range(len(degrees)))
        for g,out in zip(groups,choices):
            for i,j in zip(g,out):p[i]=j
        yield p

def transform(t,p):
    c,mask,i,j=t
    mask2=sum(1<<p[k] for k in range(len(p)) if mask>>k&1)
    return c,mask2,p[i],(-1 if j==-1 else p[j])

def check(q,degrees):
    ts=set(parameters(q,degrees))
    seen=set();sizes=[]
    perms=list(permutations(degrees))
    for t in ts:
        if t in seen:continue
        orb={transform(t,p) for p in perms}
        assert orb <=ts
        seen.update(orb)
        sizes.append(len(orb))
    assert seen==ts
    s=degrees.count(1);multi=Counter(d for d in degrees if d>1)
    expected=(q-1)*(2*s-1) if s else 0
    for n in multi.values(): expected *= n+1
    assert len(sizes)==expected,(q,degrees,len(sizes),expected)
    print('PASS q=%s factors=%s labeled=%s orbits=%s orbit_sizes=%s' %(q,degrees,len(ts),len(sizes),sorted(Counter(sizes).items())))

if __name__=='__main__':
    for q,degs in [(2,(1,)),(3,(1,)),(2,(2,)),(2,(1,2)),(3,(1,2)),
                   (2,(1,1)),(3,(1,1)),(2,(1,1,1)),(3,(1,1,1)),
                   (2,(1,1,2)),(3,(1,1,2)),(2,(1,1,2,2)),(3,(1,1,1,2,2)),
                   (2,(1,2,3,3)),(5,(1,1,2,3,3))]:
        check(q,degs)
    print('VERIFY_OK')
