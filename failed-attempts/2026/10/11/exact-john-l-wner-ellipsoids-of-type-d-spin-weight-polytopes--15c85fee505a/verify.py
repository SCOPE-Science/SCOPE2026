#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

def rank(mat):
    a=[[Fraction(x) for x in row] for row in mat]
    if not a:
        return 0
    r=0
    cols=len(a[0])
    for c in range(cols):
        piv=next((i for i in range(r,len(a)) if a[i][c]),None)
        if piv is None:
            continue
        a[r],a[piv]=a[piv],a[r]
        z=a[r][c]
        a[r]=[x/z for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                z=a[i][c]
                a[i]=[x-z*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):
            break
    return r

checks=0
for n in range(4,13):
    verts=[e for e in product((-1,1),repeat=n) if __import__('math').prod(e)==1]
    assert len(verts)==2**(n-1)

    # Work with doubled coordinates e; coordinate bounds are |e_i|<=1.
    for e in verts:
        assert all(abs(x)<=1 for x in e)
        for s in product((-1,1),repeat=n):
            if __import__('math').prod(s)==-1:
                # Original inequality is s dot (e/2) <= (n-2)/2.
                assert sum(x*y for x,y in zip(s,e)) <= n-2
                checks+=1

    # Representative coordinate facet e_0=1 has affine dimension n-1.
    eq=[e for e in verts if e[0]==1]
    base=eq[0]
    diffs=[[x-y for x,y in zip(e,base)] for e in eq[1:]]
    assert rank(diffs)==n-1

    # Representative parity facet s=(-1,1,...,1), equality s.e=n-2.
    s=(-1,)+(1,)*(n-1)
    eq2=[e for e in verts if sum(x*y for x,y in zip(s,e))==n-2]
    assert len(eq2)==n
    base=eq2[0]
    diffs=[[x-y for x,y in zip(e,base)] for e in eq2[1:]]
    assert rank(diffs)==n-1

    coord_d2=Fraction(1,4)
    parity_d2=Fraction((n-2)**2,4*n)
    if n==4:
        assert parity_d2==coord_d2
    else:
        assert parity_d2>coord_d2

    circum_d2=Fraction(n,4)
    assert all(sum(Fraction(x*x,4) for x in e)==circum_d2 for e in verts)

print(f"VERIFY_OK type-D-spin-ellipsoids n=4..12 parity_checks={checks}")
