#!/usr/bin/env python3
"""Exact integer checks for coordinate-subgroup residue monotonicity.
Python standard library only; no external data.
"""
from itertools import product, combinations
from math import prod
from random import Random

def centered(a,n):
    u=a%n
    return min(u,n-u)

def residue_count(A,free,idx,q,r):
    return len({tuple(a[j] for j in free)+tuple(a[j]%(r*q[k]) for k,j in enumerate(idx)) for a in A})

def centered_count(A,free,idx,q,r):
    slices={tuple(a[j] for j in free) for a in A}
    out=0
    for fv in slices:
        for zz in product(*(range(r*v) for v in q)):
            a=[None]*(len(free)+len(idx))
            for j,v in zip(free,fv): a[j]=v
            for k,j in enumerate(idx):
                n=r*q[k];t=zz[k]
                a[j]=t if t<=n//2 else t-n
                if n%2==0 and t==n//2: a[j]=t
            if tuple(a) in A:
                out+=1
    return out

def abs_ideal(maxvec, gens):
    return {z for z in product(*(range(-m,m+1) for m in maxvec)) if any(all(abs(z[i])<=g[i] for i in range(len(z))) for g in gens)}

def run():
    cases=0; comps=0; strict=0; equal=0; checked_formula=0; equality_checks=0
    rng=Random(20261103)
    for d in (1,2,3,4):
        maxvec=(2,)*d
        families=[]
        for m in range(3):
            gens=[tuple(rng.randrange(3) for _ in range(d)) for __ in range(m+1)]
            families.append(abs_ideal(maxvec,gens))
        for radius in range(5):
            families.append({z for z in product(*(range(-radius,radius+1) for _ in range(d))) if sum(abs(v) for v in z)<=radius})
        for A in families:
            for sz in range(1,d+1):
                for idx in combinations(range(d),sz):
                    free=tuple(j for j in range(d) if j not in idx)
                    for q in ((1,)*sz,(2,)*sz):
                        vals=[]
                        for r in range(1,6):
                            direct=residue_count(A,free,idx,q,r)
                            cent=centered_count(A,free,idx,q,r)
                            assert direct==cent,(d,idx,q,r,direct,cent)
                            checked_formula+=1
                            vals.append((direct,r**sz))
                        for offset, ((v,a),(w,b)) in enumerate(zip(vals, vals[1:])):
                            s=offset+2
                            slices={tuple(z[j] for j in free) for z in A}
                            fills=True
                            for f in slices:
                                for zz in product(*(range(-((s*q[k])//2), (s*q[k])//2+1) for k in range(sz))):
                                    z=[0]*d
                                    for j,u in zip(free,f): z[j]=u
                                    for j,u in zip(idx,zz): z[j]=u
                                    if tuple(z) not in A:
                                        fills=False;break
                                if not fills:break
                            assert ((v*b==w*a)==fills),(d,idx,q,s,v,a,w,b,fills)
                            equality_checks+=1
                            assert v*b>=w*a,(d,idx,q,v,a,w,b)
                            comps+=1
                            if v*b>w*a: strict+=1
                            else: equal+=1
                        cases+=1
    A={z for z in product(range(-2,3),repeat=3) if sum(abs(v) for v in z)<=2}
    assert [residue_count(A,(),(0,1,2),(1,1,1),r) for r in range(1,6)]==[1,7,19,22,25]
    print(f'ABSOLUTE_IDEALS_OK cases={cases} monotonic_pairs={comps} strict={strict} equal={equal} formula_checks={checked_formula}')
    print('THREE_DIMENSIONAL_L1_COUNTS 1,7,19,22,25')
    print('EQUALITY_BOX_CHECKS',equality_checks)
if __name__=='__main__':run()
