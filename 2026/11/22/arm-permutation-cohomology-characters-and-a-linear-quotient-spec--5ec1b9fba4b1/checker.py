#!/usr/bin/env python3
"""Finite exact chain-level checks for the graded arm-permutation character.

Public mathematical computation only; no external libraries or network.
Uses modular linear algebra over F_1009 in test ranks n=1..4, where
the script tests the stated formulas over this finite field for the indicated
small cases; this is not a characteristic-zero proof.
"""
from itertools import combinations, permutations
from math import factorial

MOD = 1009

def parity_sorted(xs):
    return -1 if sum(xs[i] > xs[j] for i in range(len(xs)) for j in range(i+1,len(xs))) % 2 else 1

def image_basis(columns, m):
    basis = {}
    for v in columns:
        w = list(v)
        for piv,b in sorted(basis.items()):
            a=w[piv]
            if a:
                for j,bj in enumerate(b):
                    if bj:w[j]=(w[j]-a*bj)%MOD
        nz=next((j for j,a in enumerate(w) if a),None)
        if nz is not None:
            inv=pow(w[nz],-1,MOD)
            fresh=[(a*inv)%MOD for a in w]
            for oldpivot,old in basis.items():
                factor=old[nz]
                if factor:
                    basis[oldpivot]=[(a-factor*b)%MOD for a,b in zip(old,fresh)]
            basis[nz]=fresh
    return dict(sorted(basis.items()))

def coefficient_image(v,basis):
    w=list(v); coords={}
    for piv,b in basis.items():
        a=w[piv]
        coords[piv]=a
        if a:
            for j,bj in enumerate(b):
                if bj:w[j]=(w[j]-a*bj)%MOD
    assert not any(w), 'invariant image not preserved'
    return coords

def matrix_data(n,r):
    # indices 2i = x_i, 2i+1 = z_i
    bas=list(combinations(range(2*n),r)); pos={b:i for i,b in enumerate(bas)}
    cols=[]
    for a in bas:
        v=[0]*len(bas)
        for j,index in enumerate(a):
            if index % 2 == 1 and index-1 not in a:
                targ=list(a);targ[j]=index-1
                sgn=parity_sorted(targ)
                key=tuple(sorted(targ))
                v[pos[key]]=(v[pos[key]]+sgn)%MOD
        cols.append(v)
    return bas,pos,image_basis(cols,len(bas))

def action_basis(v, bas, pos, perm):
    m=len(bas)
    w=[0]*m
    for j,a in enumerate(bas):
        if not v[j]: continue
        b=[2*perm[i//2]+i%2 for i in a]
        sign=parity_sorted(b)
        w[pos[tuple(sorted(b))]]=(w[pos[tuple(sorted(b))]]+sign*v[j])%MOD
    return w

def trace_kernel(n,r,perm):
    bas,pos,im=matrix_data(n,r)
    trace_ambient=0
    for a in bas:
        b=[2*perm[i//2]+i%2 for i in a]
        if tuple(sorted(b))==a:trace_ambient+=parity_sorted(b)
    trace_image=0
    for piv,b in im.items():
        trans=action_basis(b,bas,pos,perm)
        c=coefficient_image(trans,im)
        trace_image+=c[piv]
    return (trace_ambient-trace_image)%MOD, len(bas)-len(im)

def character_polynomial(n,perm):
    cycles=[]; unseen=set(range(n))
    while unseen:
        i=min(unseen); j=i; length=0
        while j in unseen:
            unseen.remove(j);length+=1;j=perm[j]
        cycles.append(length)
    # dictionary monomial (tdegree,qweight) -> coefficient
    poly={(0,0):1}
    for ell in cycles:
        # (1-(-tq)^ell)(1-(-tq^-1)^ell)
        fact={(0,0):1,(ell,ell):(-1)**(ell+1),(ell,-ell):(-1)**(ell+1),(2*ell,0):1}
        nxt={}
        for (k,w),c in poly.items():
            for (l,v),d in fact.items():
                nxt[(k+l,w+v)]=nxt.get((k+l,w+v),0)+c*d
        poly=nxt
    high=[poly.get((k,0),0)+poly.get((k,1),0) for k in range(2*n+1)]
    return [(high[k] if k < len(high) else 0)+(high[k-1] if k else 0) for k in range(2*n+2)]

def predicted_invariants(n):
    high=[0]*(2*n+1)
    for j in range(n+1):high[2*j]+=1
    for j in range(n):high[2*j+1]+=1
    for j in range(n-1):high[2*j+2]+=1
    return [(high[k] if k < len(high) else 0)+(high[k-1] if k else 0) for k in range(2*n+2)]

def main():
    for n in range(1,5):
        perms=list(permutations(range(n)))
        trace_by_rank={}
        for r in range(2*n+1):
            for perm in perms:
                ker,dim=trace_kernel(n,r,perm)
                trace_by_rank[(r,perm)]=ker
        for perm in perms:
            expect=character_polynomial(n,perm)
            observed=[]
            for k in range(2*n+2):
                val=(trace_by_rank.get((k,perm),0)+trace_by_rank.get((k-1,perm),0))%MOD
                assert val==expect[k]%MOD,(n,perm,k,val,expect[k])
                observed.append(val)
        invariant=[]
        for k in range(2*n+2):
            total=sum((trace_by_rank.get((k,p),0)+trace_by_rank.get((k-1,p),0))%MOD for p in perms)%MOD
            invariant.append(total*pow(factorial(n),-1,MOD)%MOD)
        target=predicted_invariants(n)
        assert invariant==[x%MOD for x in target]
        dimension=character_polynomial(n,tuple(range(n)))
        print('n=',n,'permutations=',len(perms),'graded_trace_checks=',len(perms)*(2*n+2),'Betti=',dimension,'S_n_invariant=',target)
    print('PASS: separate chain-level finite-field tests for all n=1..4')

if __name__=='__main__':main()
