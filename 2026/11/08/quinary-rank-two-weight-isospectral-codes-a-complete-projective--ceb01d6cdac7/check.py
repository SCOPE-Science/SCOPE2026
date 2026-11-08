#!/usr/bin/env python3
"""Exact arithmetic checks for quinary rank-two weight-isospectral classes."""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product

Q = 5
POINTS = range(6)  # 0,1,2,3,4,infinity

def pgl():
    perms = set()
    for a,b,c,d in product(range(Q), repeat=4):
        if (a*d-b*c) % Q == 0:
            continue
        out = []
        for x in POINTS:
            if x == 5:
                out.append(5 if c==0 else (a*pow(c,-1,Q))%Q)
            else:
                den=(c*x+d)%Q
                out.append(5 if den==0 else ((a*x+b)*pow(den,-1,Q))%Q)
        perms.add(tuple(out))
    return tuple(sorted(perms))

def cycles(p):
    seen = set(); lens=[]
    for i in POINTS:
        if i in seen: continue
        length=0; j=i
        while j not in seen:
            seen.add(j); length+=1; j=p[j]
        lens.append(length)
    return tuple(sorted(lens))

def partitions(n, maxpart=None):
    if n==0:
        yield ()
        return
    if maxpart is None: maxpart=n
    for k in range(min(n,maxpart), 1-1, -1):
        for p in partitions(n-k,k):
            yield (k,)+p

def orbit_classes(pattern, group):
    assignment=tuple(i for i,s in enumerate(pattern) for _ in range(s))
    remaining=set(permutations(assignment));sizes=[];representatives=[]
    while remaining:
        a=min(remaining)
        orbit={tuple(a[g[i]] for i in POINTS) for g in group}
        assert orbit<=remaining
        remaining-=orbit
        sizes.append(len(orbit));representatives.append(a)
    return tuple(sorted(sizes)),representatives

def burnside_count(pattern,group):
    assignment=tuple(i for i,s in enumerate(pattern) for _ in range(s))
    arr=set(permutations(assignment))
    return sum(sum(all(a[g[i]]==a[i] for i in POINTS) for a in arr) for g in group)//len(group)

def make_columns(m):
    columns=[(1,x) for x in range(5)]+[(0,1)]
    return [columns[i] for i in POINTS for _ in range(m[i])]

def spectrum(m):
    cols=make_columns(m)
    return Counter(sum((u*a+v*b)%5!=0 for a,b in cols) for u,v in product(range(5),repeat=2))

def distortion(m1,m2,g):
    n=sum(m1);assert sum(m2)==n
    r=[Fraction(n-m2[g[i]],n-m1[i]) for i in POINTS]
    return max(r)/min(r)

def main():
    group=pgl()
    assert len(group)==120
    expected_cycles={
      (1,1,1,1,1,1):1,
      (1,1,2,2):15,
      (2,2,2):10,
      (3,3):20,
      (1,1,4):30,
      (1,5):24,
      (6,):20
    }
    assert dict(Counter(cycles(g) for g in group))==expected_cycles
    expected_counts={
      (6,):1,(5,1):1,(4,2):1,(4,1,1):1,(3,3):1,
      (3,2,1):1,(3,1,1,1):1,(2,2,2):2,
      (2,2,1,1):2,(2,1,1,1,1):3,(1,1,1,1,1,1):6
    }
    assert len(expected_counts)==11
    for profile in partitions(6):
        sizes,reps=orbit_classes(profile,group)
        assert len(sizes)==expected_counts[profile]
        assert burnside_count(profile,group)==expected_counts[profile]
        print('equality pattern',profile,'classes',len(sizes),'orbit sizes',sizes)
    m1=(0,0,1,1,2,2);m2=(0,0,1,2,1,2)
    assert spectrum(m1)==Counter({4:8,5:8,6:8,0:1})
    assert spectrum(m2)==spectrum(m1)
    assert set(tuple(m1[g[i]] for i in POINTS) for g in group).isdisjoint(
           set(tuple(m2[g[i]] for i in POINTS) for g in group))
    orbit1={tuple(m1[g[i]] for i in POINTS) for g in group}
    orbit2={tuple(m2[g[i]] for i in POINTS) for g in group}
    assert len(orbit1)==60 and len(orbit2)==30 and len(orbit1|orbit2)==90
    best=min((distortion(m1,m2,g),g) for g in group)
    assert best[0]==Fraction(36,25)
    print('first ambiguity: 6 columns; orbits 60/30, spectrum',dict(spectrum(m1)))
    print('exact minimum distortion',best[0], 'witness projective permutation',best[1])
    # The minimum length for a label-equality partition uses 0,1,... as labels.
    minimum_by_classes={1:999,2:999,3:999,6:999}
    for profile,k in expected_counts.items():
        minsum=sum(j*s for j,s in enumerate(sorted(profile,reverse=True)))
        minimum_by_classes[k]=min(minimum_by_classes[k],minsum)
    assert minimum_by_classes=={1:0,2:6,3:10,6:15}
    print('first spectral class multiplicities',minimum_by_classes)
    print('ALL CHECKS PASSED')

if __name__=='__main__':main()
