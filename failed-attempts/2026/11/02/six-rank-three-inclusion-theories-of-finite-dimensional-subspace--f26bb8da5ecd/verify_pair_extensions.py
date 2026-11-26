#!/usr/bin/env python3
"""Exact three-round order-extension profiles of finite vector-space subspace lattices.

No third-party packages are required. Direct finite enumeration is an independent
check of the field-independent algebraic conditions, not proof of the theorem.
"""
from itertools import combinations, product
from collections import defaultdict

# The three entries of each triple describe X versus Y, X versus Z, Y versus Z.
# Relation codes: 0 equal; 1 proper subset; 2 proper superset; 3 incomparable.
def profile(p,u,v,w):
    out=set()
    if u==0 and v==0:
        out.add((0,0,0))
        if w:out.add((0,1,1))
        if p:out.add((0,2,2))
        if p and w:out.add((0,3,3))
    elif u==0: # X proper subset Y
        out.update([(1,0,2),(1,1,0)])
        if w:out.update([(1,1,1),(1,1,3)])
        if v>=2:out.add((1,1,2))
        if p:out.update([(1,2,2),(1,3,2)])
        if p and w:out.add((1,3,3))
    elif v==0: # X proper superset Y
        out.update([(2,0,1),(2,2,0)])
        if w:out.update([(2,1,1),(2,3,1)])
        if u>=2:out.add((2,2,1))
        if p:out.update([(2,2,2),(2,2,3)])
        if p and w:out.add((2,3,3))
    else: # X and Y incomparable
        out.update([(3,0,3),(3,1,1),(3,2,2),(3,3,0),(3,3,3)])
        if p+u>=2:out.add((3,2,3))
        if p+v>=2:out.add((3,3,2))
        if v>=2 or w:out.add((3,1,3))
        if u>=2 or w:out.add((3,3,1))
    return frozenset(out)

def root_type(a,b):
    return frozenset(profile(p,a-p,v,b-v)
                     for p in range(a+1) for v in range(b+1))

def total_type(n):
    return frozenset(root_type(a,n-a) for a in range(n+1))

def subspaces(n,q):
    """Enumerate all subspaces by unique reduced-row-echelon bases (prime q)."""
    powers=[q**i for i in range(n)]
    result=[]
    for k in range(n+1):
        for piv in combinations(range(n),k):
            free=[(i,j) for i in range(k) for j in range(piv[i]+1,n)
                  if j not in piv]
            for values in product(range(q),repeat=len(free)):
                basis=[[0]*n for _ in range(k)]
                for i,j in enumerate(piv):basis[i][j]=1
                for (i,j),value in zip(free,values):basis[i][j]=value
                vec={0}
                for row in basis:
                    vec={sum(((v//powers[i]%q+c*row[i])%q)*powers[i]
                             for i in range(n))
                         for v in vec for c in range(q)}
                result.append(sum(1<<v for v in vec))
    assert len(result)==len(set(result))
    return result

def rel(X,Y):
    if X==Y:return 0
    if X&Y==X:return 1
    if X&Y==Y:return 2
    return 3

def test_orbits(n,q):
    ss=subspaces(n,q)
    orbit_count=0
    for p in range(n+1):
        for u in range(n-p+1):
            for v in range(n-p-u+1):
                w=n-p-u-v
                a=p+u
                X=(1<<(q**a))-1
                axes=list(range(p))+list(range(a,a+v))
                Y=0
                for z in range(q**len(axes)):
                    Y|=1<<sum((z//q**j%q)*q**i
                               for j,i in enumerate(axes))
                actual=frozenset((rel(X,Y),rel(X,Z),rel(Y,Z)) for Z in ss)
                expect=profile(p,u,v,w)
                assert actual==expect,(n,q,p,u,v,w,actual^expect)
                orbit_count+=1
    return len(ss),orbit_count

if __name__=='__main__':
    families={}
    for n in range(1,41):
        t=total_type(n)
        assert len(t)==min(n,6)+1
        families.setdefault(t,[]).append(n)
        for a in range(n+1):
            assert root_type(a,n-a)==root_type(min(a,3),min(n-a,3))
    assert len(families)==6
    print('ANALYTIC: exactly six classes for dimensions 1..40; stable from dimension 6')
    for n,q in [(j,2) for j in range(1,8)]+[(j,3) for j in range(1,6)]:
        count,orbits=test_orbits(n,q)
        print(f'DIRECT_ORBITS: dimension={n} field={q} subspaces={count} ordered_pair_orbits={orbits} PASS')
    print('SHARP_REPRESENTATIVE: dimension=6 field=2 subspaces=2825')
    print('VERIFY_PAIR_EXTENSIONS_PASS')
