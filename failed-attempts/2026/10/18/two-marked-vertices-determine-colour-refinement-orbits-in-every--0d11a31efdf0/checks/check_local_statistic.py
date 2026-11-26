#!/usr/bin/env python3
"""Independently verify the distance-pair neighbor decrement identity.
Finite exhaustive checks are corroboration only, not a substitute for proof.
"""
from itertools import product
from collections import defaultdict,Counter

def direct_check(q,d,b):
    x0=(0,)*d
    x1=(1,)*b+(0,)*(d-b)
    by_dist=defaultdict(set)
    by_stat=defaultdict(set)
    total=0
    for x in product(range(q),repeat=d):
        h0=sum(u!=v for u,v in zip(x,x0))
        h1=sum(u!=v for u,v in zip(x,x1))
        s=sum(x[i]!=0 for i in range(b,d))
        count=0
        for i in range(d):
            for letter in range(q):
                if letter==x[i]:continue
                y=x[:i]+(letter,)+x[i+1:]
                dy0=sum(u!=v for u,v in zip(y,x0))
                dy1=sum(u!=v for u,v in zip(y,x1))
                if dy0==h0-1 and dy1==h1-1:count+=1
        assert count==s,(q,d,b,x,s,count)
        v=b+s-h0
        w=b+s-h1
        assert v==sum(x[i]==0 for i in range(b))
        assert w==sum(x[i]==1 for i in range(b))
        by_dist[(h0,h1)].add((s,v,w))
        by_stat[(h0,h1,count)].add((s,v,w))
        total+=1
    assert all(len(v)==1 for v in by_stat.values())
    return total,len(by_stat),sum(len(v)>1 for v in by_dist.values())

def main():
    trials=0;verts=0;ambig=0
    for q,mx in [(3,6),(4,5),(5,4),(6,3)]:
        for d in range(1,mx+1):
            for b in range(1,d+1):
                n,c,a=direct_check(q,d,b)
                trials+=1;verts+=n;ambig+=a
    anchor0=(0,0,0);anchor1=(0,1,1)
    x=(0,2,2);y=(2,0,1)
    def distances(z):return tuple(sum(u!=v for u,v in zip(z,m)) for m in (anchor0,anchor1))
    assert distances(x)==distances(y)==(2,2)
    def down(z):
        return sum(distances(z[:i]+(t,)+z[i+1:])==(1,1) for i in range(3) for t in range(3) if t!=z[i])
    assert (down(x),down(y))==(0,1)
    print(f'PASS independent_distance_tests={trials} aggregate_vertices={verts} distance_pair_ambiguous_cells={ambig}')
    print('PASS explicit_ternary_cube_distance_collision: same_distances=(2,2), decrement_counts=(0,1)')

if __name__=='__main__':main()
