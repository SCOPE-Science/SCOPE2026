"""Exact rank-three census for finite two-sorted bipartite graphs.
Self-contained Python 3 standard-library program. Run python structural_census.py.
"""
from collections import Counter
from itertools import permutations


def pair_rank_one(rows, a, b):
    # a,b=(side,index); sides 0=row, 1=column.
    sa,ia=a; sb,ib=b
    if sa==sb==0:
        return len({((rows[ia]>>j)&1,(rows[ib]>>j)&1) for j in range(4)})==4
    if sa==sb==1:
        return len({((rows[i]>>ia)&1,(rows[i]>>ib)&1) for i in range(4)})==4
    if sa==1:
        ia,ib=ib,ia
    return (len({(rows[ia]>>j)&1 for j in range(4) if j!=ib})==2
            and len({(rows[i]>>ib)&1 for i in range(4) if i!=ia})==2)


def singleton_rank_two(rows, side, i):
    if not any(pair_rank_one(rows,(side,i),(side,j)) for j in range(4) if i!=j):
        return False
    other=1-side
    for value in (0,1):
        if not any(((rows[i]>>j)&1 if side==0 else (rows[j]>>i)&1)==value
                   and pair_rank_one(rows,(side,i),(other,j)) for j in range(4)):
            return False
    return True


def root_rank_three(rows):
    return (any(singleton_rank_two(rows,0,i) for i in range(4))
            and any(singleton_rank_two(rows,1,j) for j in range(4)))


def canon_orbit(rows):
    allperms=tuple(permutations(range(4)))
    variants=set()
    for cp in allperms:
        moved=[sum(((r>>cp[j])&1)<<j for j in range(4)) for r in rows]
        for rp in allperms:
            variants.add(tuple(moved[i] for i in rp))
    return min(variants),len(variants)


def main():
    count=0; orbit_reps={}; orbits=Counter(); edge_profile=Counter(); bad=0
    for m in range(1<<16):
        rows=tuple((m>>(4*i))&15 for i in range(4))
        if root_rank_three(rows):
            count+=1
            key,size=canon_orbit(rows)
            if key in orbit_reps:
                assert orbit_reps[key]==size
            else:
                orbit_reps[key]=size
                orbits[size]+=1
            edge_profile[sum(r.bit_count() for r in rows)]+=1
    assert count==9672,(count,)
    assert len(orbit_reps)==29
    assert orbits==Counter({576:8,288:16,96:4,72:1}),orbits
    assert sum(size*count for size,count in orbits.items())==9672
    print('ALL_CHECKS_OK')
    print('LABELED=9672 ORBITS=29 ORBIT_SIZES='+str(sorted(orbits.items())))
    print('EDGE_DISTRIBUTION='+str(sorted(edge_profile.items())))
    for rep,size in sorted(orbit_reps.items()):
        print('REP',','.join(format(r,'04b')[::-1] for r in rep),'ORBIT',size)

if __name__=='__main__': main()
