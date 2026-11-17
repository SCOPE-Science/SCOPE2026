#!/usr/bin/env python3
"""Full symmetry decomposition of the longest-transient states, using only Python 3."""
from collections import Counter
from pathlib import Path

V=range(12)
E=set()
for i in range(5):
    j=(i+1)%5
    for a,b in ((0,1+i),(11,6+i),(1+i,1+j),(6+i,6+j),(1+i,6+i),(1+i,6+(i+4)%5)):
        E.add(tuple(sorted((a,b))))
assert len(E)==30
N={i:set() for i in V}
for a,b in E:
    N[a].add(b)
    N[b].add(a)
assert all(len(N[i])==5 for i in V)

# For an image of vertex 0, and either cyclic orientation of its 5-neighbor link,
# the remaining images are uniquely forced by adjacent neighbor pairs.
autos=[]
for apex in V:
    link=N[apex]
    for first in link:
        for second in sorted(N[first] & link):
            ring=[first, second]
            while len(ring)<5:
                next_options=(N[ring[-1]] & link)-{ring[-2]}
                assert len(next_options)==1
                ring.append(next(iter(next_options)))
            assert ring[-1] in N[ring[0]]
            p=[None]*12
            p[0]=apex
            for i in range(5):
                p[1+i]=ring[i]
            for i in range(5):
                common=(N[ring[i]] & N[ring[(i+1)%5]])-{apex}
                assert len(common)==1
                p[6+i]=next(iter(common))
            other=set(V)-set(p[:-1])
            assert len(other)==1
            p[11]=next(iter(other))
            assert len(set(p))==12
            assert {tuple(sorted((p[a],p[b]))) for a,b in E}==E
            autos.append(tuple(p))
assert len(autos)==120 and len(set(autos))==120

def action(x,p):
    y=0
    for i,j in enumerate(p):
        y|=((x>>(2*i))&3)<<(2*j)
    return y

codes={int(x) for x in Path('extremal_codes.txt').read_text(encoding='ascii').splitlines()}
assert len(codes)==240
unclassified=set(codes)
classes=[]
while unclassified:
    rep=min(unclassified)
    orb={action(rep,p) for p in autos}
    assert orb<=codes
    unclassified.difference_update(orb)
    classes.append((rep,len(orb)))
assert len(classes)==2 and all(size==120 for _,size in classes)
print('automorphism_order=',len(autos),sep='')
print('extremal_state_count=',len(codes),sep='')
print('geometric_orbit_count=',len(classes),sep='')
for rep,size in classes:
    print('representative=',rep,', orbit_size=',size,sep='')
