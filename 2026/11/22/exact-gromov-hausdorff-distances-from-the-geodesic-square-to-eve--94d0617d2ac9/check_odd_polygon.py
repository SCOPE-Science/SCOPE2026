#!/usr/bin/env python3
"""Exact integer checks for four- versus odd-vertex circle-geodesic spaces.
Distances are scaled by 4m; continuous/all-m conclusions use the published proof.
"""
from itertools import product

def cyclic(i,j,n):
    d=abs(i-j)
    return min(d,n-d)

def blocks(m):
    assert m>=5 and m%2==1
    k=m//4
    sizes=[k+1,k,k,k] if m%4==1 else [k+1,k+1,k+1,k]
    assert sum(sizes)==m and min(sizes)>=1
    labels=[]
    for v,n in enumerate(sizes): labels.extend([v]*n)
    return labels

def distortion(labels):
    m=len(labels)
    return max((abs(m*cyclic(labels[i],labels[j],4)-4*cyclic(i,j,m))
                for i in range(m) for j in range(i)),default=0)

def parity_check(m):
    s=m//4 if m%4==1 else m//4+1
    threshold=m-1
    # Under a distortion strictly below threshold, all step-s edges
    # must map to adjacent (opposite parity) square labels.
    eligible=[q for q in [0,1,2] if abs(m*q-4*s)<threshold]
    assert eligible==[1], (m,s,eligible)
    # Every +s orbit has odd length since it partitions an odd set.
    seen=set(); lengths=[]
    for start in range(m):
        if start in seen: continue
        x=start; L=0
        while x not in seen:
            seen.add(x);L+=1;x=(x+s)%m
        assert x==start
        assert L%2==1
        lengths.append(L)
    assert sum(lengths)==m


def exhaustive_map_check(m):
    # Complete search over surjective single-valued maps, modulo
    # rotation of square labels, as a finite consistency check only.
    best=2*m
    count=0
    for tail in product(range(4),repeat=m-1):
        labels=(0,)+tail
        if len(set(labels))<4: continue
        count+=1
        d=distortion(labels)
        best=min(best,d)
    assert best==m-1,(m,best,m-1)
    return count

def main():
    checked=0
    for m in range(5,402,2):
        labels=blocks(m)
        assert set(labels)==set(range(4))
        d=distortion(labels)
        assert d==m-1,(m,d,m-1)
        parity_check(m)
        checked+=1
    finite={m:exhaustive_map_check(m) for m in (5,7,9)}
    print('PASS: '+str(checked)+' odd sizes, exact upper-bound distortions; parity obstruction for each')
    print('PASS: complete surjective map search for small orders '+str(finite))
    print('ANALYTIC: odd-cycle bipartite obstruction proves lower bound for all correspondences')

if __name__=='__main__': main()
