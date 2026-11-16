#!/usr/bin/env python3
"""Exact fourth-order complex Fourier-minor rank census, using a certified finite-field lift.
Standalone Python 3; no external dependencies.
"""
from itertools import combinations
from collections import Counter

N=12
P=65581  # prime, P = 1 modulo 12, P > 4**8
ROOT=62640


def prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p**.5)+1))


def exact_rank(rows, cols, powers):
    # Independent modular Gaussian elimination, column-first full pivot search.
    a=[[powers[(r*c)%12] for c in cols] for r in rows]
    rank=0
    for j in range(4):
        i=next((k for k in range(rank,4) if a[k][j]),None)
        if i is None:continue
        a[rank],a[i]=a[i],a[rank]
        inv=pow(a[rank][j],P-2,P)
        for k in range(rank+1,4):
            if a[k][j]:
                h=a[k][j]*inv%P
                for l in range(j,4):
                    a[k][l]=(a[k][l]-h*a[rank][l])%P
        rank+=1
        if rank==4:break
    return rank


def main():
    assert prime(P) and P>65536 and (P-1)%12==0
    assert pow(ROOT,12,P)==1 and pow(ROOT,6,P)==P-1 and pow(ROOT,4,P)!=1
    powers=[pow(ROOT,j,P) for j in range(12)]
    sets=list(combinations(range(12),4))
    assert len(sets)==495
    counts=Counter()
    profiles={}
    for rows in sets:
        rs=Counter(exact_rank(rows,cols,powers) for cols in sets)
        assert sum(rs.values())==495 and not rs[0] and not rs[1]
        profiles[rows]=tuple(rs[r] for r in range(1,5))
        counts.update(rs)
    assert tuple(counts[r] for r in range(1,5))==(0,1224,39384,204417)
    assert sum(counts.values())==245025
    assert sum(p[3]==495 for p in profiles.values())==24
    # All orbits under affine bijections of Z/12Z; certify that every member
    # of each orbit has identical rank profile.
    units=(1,5,7,11)
    left=set(sets)
    orbits=[]
    while left:
        rep=min(left)
        orbit={tuple(sorted((u*r+b)%12 for r in rep)) for u in units for b in range(12)}
        assert orbit <= left
        assert len({profiles[r] for r in orbit})==1
        orbits.append((rep,len(orbit),profiles[rep]))
        left-=orbit
    assert sum(s for _,s,_ in orbits)==495
    print('EXACT_Z12_TOTALS',dict(sorted(counts.items())))
    print('FULL_SPARK_ROWS',sum(p[3]==495 for p in profiles.values()))
    print('AFFINE_ORBITS',len(orbits))
    for rep,size,counts in orbits:
        print('ORBIT',','.join(map(str,rep)),size,*counts)
    print('EXACT_Z12_CHECK_PASS')

if __name__=='__main__':main()
