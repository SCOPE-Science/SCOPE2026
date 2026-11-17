#!/usr/bin/env python3
"""Reproduce exact face ranks and normal-angle classes for complete multipartite stable-set polytopes.

Requires only Python's standard library. The analytic face-measure identities are
proved in the accompanying mathematical statement, not inferred from finite tests.
"""
import itertools
from fractions import Fraction
from math import comb


def rank(rows):
    if not rows:
        return 0
    a = [[Fraction(z) for z in row] for row in rows]
    m, n = len(a), len(a[0]); pivot = 0
    for c in range(n):
        k = next((j for j in range(pivot, m) if a[j][c]), None)
        if k is None: continue
        a[pivot], a[k] = a[k], a[pivot]
        val = a[pivot][c]
        for j in range(c,n): a[pivot][j] /= val
        for i in range(pivot+1,m):
            val = a[i][c]
            if val:
                for j in range(c,n): a[i][j] -= val*a[pivot][j]
        pivot += 1
        if pivot == m: break
    return pivot


def calculate(profile):
    k=len(profile); N=sum(profile); Q=1
    for v in profile: Q*=v
    offs=[sum(profile[:i]) for i in range(k)]
    blocks=[tuple(range(o,o+n)) for o,n in zip(offs,profile)]
    vertices=[(0,)*N]
    for block in blocks:
        for mask in range(1,1<<len(block)):
            v=[0]*N
            for j,z in enumerate(block): v[z] = (mask>>j)&1
            vertices.append(tuple(v))
    facets=[]
    for i in range(N):
        facets.append(('L',i,tuple(-int(j==i) for j in range(N)),0))
    for chosen in itertools.product(*blocks):
        facets.append(('U',tuple(chosen),tuple(int(j in chosen) for j in range(N)),1))
    classes={'LL':0,'LU_right':0,'LU_acute':0,'UU':0}
    for A,B in itertools.combinations(facets,2):
        candidates=[v for v in vertices if sum(x*y for x,y in zip(A[2],v))==A[3] and sum(x*y for x,y in zip(B[2],v))==B[3]]
        r=rank([[x-y for x,y in zip(v,candidates[0])] for v in candidates[1:]]) if candidates else -1
        t=None
        if A[0]=='L' and B[0]=='L': t='LL'; expected=True
        elif A[0]=='L' and B[0]=='U':
            i=A[1]; chosen=B[1]
            if i not in chosen: t='LU_right';expected=True
            else:
                selected_block=next(z for z,block in enumerate(blocks) if i in block)
                t='LU_acute' if profile[selected_block]==1 else None
                expected=profile[selected_block]==1
        else:
            count=len(set(A[1]).intersection(B[1]));expected=(count==k-1)
            if expected:t='UU'
        assert (r==N-2)==expected,(profile,A[:2],B[:2],r,expected)
        if expected:
            classes[t]+=1
            dot=sum(x*y for x,y in zip(A[2],B[2])); na=sum(x*x for x in A[2]);nb=sum(x*x for x in B[2])
            if t in ('LL','LU_right'):assert dot==0
            if t=='LU_acute':assert (dot,na,nb)==(-1,1,k)
            if t=='UU':assert (dot,na,nb)==(k-1,k,k)
    s=sum(n==1 for n in profile)
    expected={'LL':comb(N,2),'LU_right':Q*(N-k),'LU_acute':s*Q,'UU':Q*(N-k)//2}
    assert classes==expected,(profile,classes,expected)
    return classes

if __name__=='__main__':
    profiles=[(1,1,1),(1,1,2),(1,2,2),(2,2,2),(1,1,1,2,2),(1,1,1,2,3),
              (1,1,1,3,3),(1,1,2,2,2),(1,2,2,2,2),(2,2,2,2)]
    for p in profiles:
        z=calculate(p)
        print('PASS',p,z)
    print('MULTIPARTITE_RIDGE_CLASSIFICATION_PASS profiles='+str(len(profiles)))
