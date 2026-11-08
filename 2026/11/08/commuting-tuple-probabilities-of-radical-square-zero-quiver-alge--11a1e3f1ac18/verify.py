"""Finite checks for commuting tuples of radical-square-zero quiver algebras.

Uses direct algebra multiplication and independent spanning-subgraph expansion.
Only Python's standard library is required.
"""
from itertools import product, combinations
from collections import Counter
from fractions import Fraction
from math import comb


def subsets_components(n, edges):
    z = Counter()
    for mask in range(1 << len(edges)):
        parent = list(range(n))
        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x
        selected = 0
        for j, (u,v) in enumerate(edges):
            if (mask >> j) & 1:
                selected += 1
                pu, pv = root(u),root(v)
                if pu != pv: parent[pu] = pv
        k = len({root(i) for i in range(n)})
        z[(k,selected)] += 1
    return z


def predicted(n, edges, q, t):
    Q, v, m = q ** t, q ** (t - 1) - 1, len(edges)
    z = sum(cnt * Q ** k * v ** e for (k,e),cnt in subsets_components(n,edges).items())
    return Fraction(z, q ** (t*n+(t-1)*m))


def multiply(x, y, n, edges, q):
    # Vertices first, arrow coordinates second.  All length-two paths vanish.
    return tuple((x[i]*y[i]) % q for i in range(n)) + tuple(
        (x[u]*y[n+j] + x[n+j]*y[v]) % q
        for j,(u,v) in enumerate(edges))


def direct(n, edges, q, t):
    elems = list(product(range(q), repeat=n+len(edges)))
    N = len(elems)
    if t == 2:
        good = 0
        for x in elems:
            for y in elems:
                if multiply(x,y,n,edges,q) == multiply(y,x,n,edges,q):
                    good += 1
        return Fraction(good, N*N)
    # Explicit pairwise product for each triple; no formula used to count.
    assert t == 3 and N <= 64
    compatible = [[False] * N for _ in range(N)]
    for i,x in enumerate(elems):
        for j,y in enumerate(elems):
            compatible[i][j] = multiply(x,y,n,edges,q) == multiply(y,x,n,edges,q)
    good = 0
    for i in range(N):
        for j in range(N):
            if compatible[i][j]:
                good += sum(compatible[i][k] and compatible[j][k] for k in range(N))
    return Fraction(good, N**3)


def recover_injection(n,edges,t):
    m=len(edges)
    assert t > m
    Z=subsets_components(n,edges)
    H=Counter()
    # H(X,Y)=Z(X,Y-1); build coefficients with an unrelated expansion.
    for (i,e),v in Z.items():
        for j in range(e+1):
            H[(i,j)] += v * comb(e,j) * (-1)**(e-j)
    H={k:v for k,v in H.items() if v}
    E=Counter()
    for (i,j),v in H.items(): E[t*i+(t-1)*j] += v
    assert len(H)==len(E), (H,E)
    # Decode each exponent using division by t; 0 <= j < t.
    decoded=Counter()
    for exponent,v in E.items():
        r=exponent%t
        j=0 if r==0 else t-r
        total=(exponent+j)//t
        i=total-j
        assert (i,j) in H and H[(i,j)]==v
        decoded[(i,j)]=v
    assert dict(decoded)==H
    # Compare with direct Fortuin-Kasteleyn evaluations at two field orders.
    for q in (2,3):
        lhs=sum(v*q**e for e,v in E.items())
        rhs=sum(c*(q**t)**i*(q**(t-1)-1)**j for (i,j),c in Z.items())
        assert lhs==rhs
    return len(H)


def run():
    cases=[
        ('single_arrow',2,[(0,1)],2,2),
        ('Kronecker_2',2,[(0,1),(0,1)],2,2),
        ('path3',3,[(0,1),(1,2)],3,2),
        ('triangle',3,[(0,1),(1,2),(2,0)],2,2),
        ('triangle_reverse',3,[(1,0),(1,2),(0,2)],2,2),
        ('triangle_odd_field',3,[(0,1),(1,2),(2,0)],3,2),
        ('cycle4',4,[(0,1),(1,2),(2,3),(3,0)],2,2),
        ('tree4',4,[(0,1),(1,2),(2,3)],2,2),
        ('triangle_isolate',4,[(0,1),(1,2),(2,0)],2,2),
        ('triangle_triple',3,[(0,1),(1,2),(2,0)],2,3),
    ]
    for name,n,edges,q,t in cases:
        d=direct(n,edges,q,t)
        p=predicted(n,edges,q,t)
        assert d==p, (name,d,p)
        print('DIRECT_OK',name, 'q',q,'t',t, 'probability',str(p))
    # Formula derived in other work for the generalized two-vertex Kronecker case.
    for q in (2,3,4):
        for r in range(1,5):
            p=predicted(2,[(0,1)]*r,q,2)
            assert p == Fraction(1,q*q) + Fraction(q*q-1,q**(r+2))
    print('KRONECKER_SPECIALIZATION_OK')
    for n in (3,4,5,6):
        path=[(i,i+1) for i in range(n-1)]
        for q,t in ((2,2),(3,2),(2,3)):
            Q=q**t
            alpha=Fraction(1+(Q-1)*Fraction(1,q**(t-1)),Q)
            beta=Fraction(1-Fraction(1,q**(t-1)),Q)
            assert predicted(n,path,q,t)==alpha**(n-1)
            cycle=path+[(n-1,0)]
            assert predicted(n,cycle,q,t)==alpha**n+(Q-1)*beta**n
    print('TREE_CYCLE_FORMULAS_OK')
    for n,edges in ((3,[(0,1),(1,2),(2,0)]),
                    (4,[(0,1),(1,2),(2,3)]),
                    (4,[(0,1),(1,2),(2,0)]),
                    (4,[(0,1),(1,2),(2,3),(3,0)])):
        nterms=recover_injection(n,edges,len(edges)+1)
        print('RECONSTRUCTION_OK',n,len(edges),nterms)
    print('VERIFY_OK')

if __name__=='__main__':run()
