#!/usr/bin/env python3
"""Exhaustive bracket fibers for four families of 6D two-step Lie algebras.
Proof-independent direct 4-vector enumeration and 4x4 row reduction.
No external dependencies.
"""
from itertools import product
from collections import Counter

def beta(x,y,kind,T,q):
    if kind=='singular':
        return ((x[0]*y[1]-y[0]*x[1])%q,(x[0]*y[2]-y[0]*x[2])%q)
    a=(x[0]*y[2]+x[1]*y[3]-y[0]*x[2]-y[1]*x[3])%q
    b=(x[0]*(T[0][0]*y[2]+T[0][1]*y[3])+x[1]*(T[1][0]*y[2]+T[1][1]*y[3])
        -y[0]*(T[0][0]*x[2]+T[0][1]*x[3])-y[1]*(T[1][0]*x[2]+T[1][1]*x[3]))%q
    return (a,b)

def rank(a,q):
    a=[list(row) for row in a];k=0
    for j in range(len(a[0])):
        p=next((i for i in range(k,len(a)) if a[i][j]%q),None)
        if p is None: continue
        a[k],a[p]=a[p],a[k]
        t=pow(a[k][j],-1,q)
        a[k]=[(x*t)%q for x in a[k]]
        for i in range(len(a)):
            if i!=k:
                w=a[i][j]
                a[i]=[(a[i][c]-w*a[k][c])%q for c in range(len(a[0]))]
        k+=1
        if k==len(a):break
    return k

def check(q,kind,T):
    assert q in (2,3,5)
    vec=list(product(range(q),repeat=4))
    e=[tuple(int(i==j) for i in range(4)) for j in range(4)]
    def form_matrix(lam):
        return [[sum(lam[t]*beta(e[i],e[j],kind,T,q)[t] for t in range(2))%q
                 for j in range(4)] for i in range(4)]
    # Represent projective lines in k^2 by (1,t) and (0,1).
    lines=[(1,t) for t in range(q)]+[(0,1)]
    bad={l for l in lines if rank(form_matrix(l),q)==2}
    assert all(rank(form_matrix(l),q) in (2,4) for l in lines)
    r=len(bad)
    hist=Counter()
    for x in vec:
        for y in vec: hist[beta(x,y,kind,T,q)]+=1
    assert sum(hist.values())==q**8
    t=q**4-q**2
    for z in product(range(q),repeat=2):
        if z==(0,0): exp=q**6+q**4-q**2+t*r*(q-1)
        else:
            s=int(any((l[0]*z[0]+l[1]*z[1])%q==0 for l in bad))
            exp=q**6-q**2+t*(q*s-r)
        if hist[z]!=exp:raise AssertionError((q,kind,T,z,hist[z],exp,bad))
    vals=Counter(hist.values())
    print(f'q={q}; pencil={kind}; r={r}; bad={sorted(bad)}; multiplicities={dict(sorted(vals.items()))}; pairs={q**8}; PASS',flush=True)

if __name__=='__main__':
    for q in (2,3,5):
        check(q,'singular',None)
        check(q,'repeated',((0,1),(0,0)))
        check(q,'split',((0,0),(0,1)))
    # Irreducible quadratic at q=3,5 using x^2+1 for q=3, and x^2-2 for q=5.
    check(3,'nonsplit',((0,2),(1,0)))
    check(5,'nonsplit',((0,2),(1,0)))
    print('PFAFFIAN_PENCIL_COMPLETE_BRACKET_FIBERS_PASS')
