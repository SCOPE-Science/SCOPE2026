#!/usr/bin/env python3
"""Independent finite-field subspace enumeration and closed-form comparisons."""
from itertools import combinations, product
from math import prod

def gauss(n,k,q):
    if k<0 or k>n:return 0
    if k==0:return 1
    numerator=prod(q**(n-i)-1 for i in range(k))
    denominator=prod(q**(k-i)-1 for i in range(k))
    return numerator//denominator

def formula(m,q):
    n=2*m
    def degree(k):
        return sum(gauss(k,n-j,q)*q**((n-k)*(n-j)) for j in range(n-k,n))
    def isotropic(k):
        return gauss(m,k,q)*prod(q**(m-i)+1 for i in range(k))
    base_order=sum(gauss(n,k,q) for k in range(n))
    extra=sum(isotropic(k)*q**k for k in range(1,m+1))
    e0=sum(gauss(n,k,q)*degree(k) for k in range(1,n))//2
    e1=sum(isotropic(k)*q**k*degree(k) for k in range(1,m+1))
    e2=isotropic(m)*q**(m*(m+1)//2+2*m)//2
    return (base_order+extra,e0+e1+e2, (q**n-1)//(q-1), (e0,e1,e2))

def rref(rows,q,dim):
    rows=[list(x) for x in rows if any(x)]
    r=0
    for c in range(dim):
        pivot=next((i for i in range(r,len(rows)) if rows[i][c]%q),None)
        if pivot is None:continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        mul=pow(rows[r][c],-1,q)
        rows[r]=[(mul*x)%q for x in rows[r]]
        for i in range(len(rows)):
            if i!=r and rows[i][c]:
                mul=rows[i][c]
                rows[i]=[(a-mul*b)%q for a,b in zip(rows[i],rows[r])]
        r+=1
        if r==len(rows):break
    return tuple(tuple(x) for x in rows[:r])

def all_subspaces(d,q):
    for k in range(d+1):
        for piv in combinations(range(d),k):
            locations=[(i,j) for i,p in enumerate(piv) for j in range(p+1,d) if j not in piv]
            for values in product(range(q),repeat=len(locations)):
                rows=[[int(j==p) for j in range(d)] for p in piv]
                for (i,j),v in zip(locations,values):rows[i][j]=v
                yield tuple(tuple(x) for x in rows)

def br(a,b,m,q):
    v=sum(a[i]*b[m+i]-a[m+i]*b[i] for i in range(m))%q
    return (0,)*(2*m)+(v,)

def subalgebra(U,m,q):
    dim=2*m+1
    return all(rref(U+(br(a,b,m,q),),q,dim)==U for a in U for b in U)

def run(m,q):
    d=2*m+1
    allsub=list(all_subspaces(d,q))
    assert len(allsub)==sum(gauss(d,k,q) for k in range(d+1))
    vertices=[U for U in allsub if 0<len(U)<d and subalgebra(U,m,q)]
    classes={}
    for U in vertices:
        W=rref(tuple(v[:-1] for v in U),q,d-1)
        classes.setdefault(W,[]).append(U)
    expectedN,expectedE,expectedClique,parts=formula(m,q)
    assert len(vertices)==expectedN,(m,q,len(vertices),expectedN)
    assert len(classes)==sum(gauss(d-1,k,q) for k in range(d-1)),len(classes)
    # Each fiber cardinality is checked independently from the bracket and basis enumeration.
    for W,fiber in classes.items():
        k=len(W)
        iso=all(br(a+(0,),b+(0,),m,q)==(0,)*d for a in W for b in W)
        expected=1+(q**k if k>0 and iso else 0)
        assert len(fiber)==expected,(W,len(fiber),expected)
    E=0
    for i,U in enumerate(vertices):
        for B in vertices[i+1:]:
            generators=U+B+tuple(br(a,b,m,q) for a in U for b in B)
            generated=len(rref(generators,q,d))==d
            projU=rref(tuple(x[:-1] for x in U),q,d-1)
            projB=rref(tuple(x[:-1] for x in B),q,d-1)
            proj=len(rref(projU+projB,q,d-1))==d-1
            assert generated==proj,(m,q,U,B)
            E+=generated
    assert E==expectedE,(m,q,E,expectedE)
    print('DIRECT_OK', 'm=',m,'q=',q,'ambient_subspaces=',len(allsub),'subalgebras=',len(vertices),'edges=',E,'fiber_classes=',len(classes),'edge_parts=',parts, 'clique=',expectedClique)

if __name__=='__main__':
    for m,q in [(1,2),(1,3),(2,2),(2,3)]:run(m,q)
    for m in range(1,6):
        for q in [2,3,4,5]:
            n,e,h,parts=formula(m,q)
            assert n>0 and e>0 and 2*e<=n*(n-1)
            assert h==(q**(2*m)-1)//(q-1)
    print('VERIFY_OK direct_cases=4 symbolic_configs=20')
