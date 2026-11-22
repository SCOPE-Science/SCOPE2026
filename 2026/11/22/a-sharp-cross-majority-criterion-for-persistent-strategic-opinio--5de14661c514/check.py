"""Exact-arithmetic checks for sign-flipping two-bin strategic opinion dynamics.

Run: python3 check.py. No external packages are required.
The infinite-family theorem is proved in RESULT.md; these tests verify algebraic
identities, concrete witnesses, and small finite cases.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def influence(m, p):
    n = 2*m
    W = []
    for i in range(n):
        W.append([F(0) if i == j else
                  p/F(m-1) if i//m == j//m else (1-p)/F(m)
                  for j in range(n)])
    return W


def mv(W, x):
    return [sum((v*t for v,t in zip(row,x)), F(0)) for row in W]


def update(W, a, x):
    sig = [F(1,2) if v > 0 else F(-1,2) if v < 0 else None for v in x]
    assert all(v is not None for v in sig), 'no threshold point in these tests'
    y = mv(W, sig)
    return [ai*xi+(1-ai)*yi for ai,xi,yi in zip(a,x,y)]


def formula(W, a, s):
    return [-((1-ai)/(1+ai))*t/F(2) for ai,t in zip(a,mv(W,s))]


def cross_majority(W,s):
    return all(sum((v for v,sj in zip(row,s) if sj != s[i]),F(0)) > F(1,2)
               for i,row in enumerate(W))


def assert_criterion(W,a,s):
    n=len(s)
    assert len(W)==len(a)==n
    assert all(W[i][i]==0 and sum(W[i],F(0))==1 and all(w>=0 for w in W[i]) for i in range(n))
    # Under these strict inertias, nonzero audience columns imply exaggeration > 1.
    xi=[]
    for j in range(n):
        v=[(1-a[i])*W[i][j] for i in range(n) if W[i][j]>0]
        assert v
        xi.append(sum(v,F(0))/sum((t*t for t in v),F(0)))
    assert all(v>1 for v in xi)
    x = formula(W,a,s)
    good = all(s[i]*x[i]>0 for i in range(n))
    assert good == cross_majority(W,s)
    if good:
        y=update(W,a,x)
        assert y==[-v for v in x]
        assert update(W,a,y)==x
        assert all(-s[i]*y[i]>0 for i in range(n))
        assert max(abs(t) for t in x)<F(1)
        # The exact local basin radius is half of the minimum distance to a threshold.
        delta=min(abs(v) for v in x)/2
        # Rational perturbations chosen strictly within that ball.
        for e in [F(0),delta/3,-delta/3]:
            z=[xi+e*F((i%3)-1,1) for i,xi in enumerate(x)]
            znext=update(W,a,z)
            assert max(abs(u-v) for u,v in zip(znext,y))<delta
            ztwo=update(W,a,znext)
            assert ztwo == [xi+(ai*ai)*(zi-xi) for xi,ai,zi in zip(x,a,z)]
    return good


def main():
    tests=0
    for m in range(2,9):
        for p in [F(1,100),F(1,4),F(2,5),F(49,100),F(1,2),F(3,4)]:
            W=influence(m,p)
            s=[F(1) if i<m else F(-1) for i in range(2*m)]
            for av in [F(1,100),F(1,3),F(1,2),F(99,100),F(999,1000)]:
                a=[av]*(2*m)
                assert assert_criterion(W,a,s)==(p<F(1,2))
                tests+=1
    # The primitive four-vertex graph remains periodic for near-unit inertia.
    W=influence(2,F(1,4)); a=[F(99,100)]*4
    s=[F(1),F(1),F(-1),F(-1)]
    x=formula(W,a,s)
    assert x == [F(1,796),F(1,796),F(-1,796),F(-1,796)]
    assert update(W,a,x)==[-v for v in x]
    assert all(W[i][j]>0 for i in range(4) for j in range(4) if i!=j)
    # Primitive: every entry of W^2 must be positive.
    assert all(v>0 for row in [[sum(W[i][k]*W[k][j] for k in range(4)) for j in range(4)] for i in range(4)] for v in row)
    # Heterogeneous inertia and asymmetric positive off-diagonal weights.
    W=[[F(0),F(1,8),F(5,8),F(1,4)],
       [F(1,4),F(0),F(3,8),F(3,8)],
       [F(1,2),F(3,8),F(0),F(1,8)],
       [F(3,8),F(3,8),F(1,4),F(0)]]
    a=[F(1,9),F(3,4),F(7,8),F(999,1000)]
    assert assert_criterion(W,a,s)
    tests+=1
    # Independent small-model comparisons for all nontrivial sign partitions.
    rng=Random(41222)
    for n in range(2,7):
        for _ in range(12):
            W=[]
            for i in range(n):
                row=[F(0) if i==j else F(rng.randint(1,20)) for j in range(n)]
                total=sum(row,F(0)); W.append([t/total for t in row])
            a=[F(rng.randint(1,999),1000) for _ in range(n)]
            for bits in product((-1,1),repeat=n):
                if bits==(1,)*n or bits==(-1,)*n: continue
                assert_criterion(W,a,[F(t) for t in bits])
                tests+=1
    print('VERIFY_OK',tests,'exact criterion and cycle cases; primitive rational witness 1/796')

if __name__=='__main__': main()
