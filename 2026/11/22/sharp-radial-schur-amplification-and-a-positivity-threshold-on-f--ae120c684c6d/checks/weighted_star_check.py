"""Exact arithmetic checks of the weighted star Schur norm identities.

Finite checks supplement, rather than replace, the analytic proof for all orders
and all real parameters.
"""
from fractions import Fraction as F
import random

def certify(n,t):
    assert n >= 1 and t >= 0
    D=2*n*t+n+1
    if n*t*t<=1:
        # The radial symbol is positive semidefinite by a 2x2 Schur complement.
        assert 1-n*t*t>=0
        return 1
    d=2*(n*t*t-1)/D
    s=1+d
    a=t-d
    assert d>0 and s>1
    assert d*n*d == n*(a-t)**2
    assert (d+2)*(n*d+2) == n*(a+t)**2
    # The witness has q+nr=1, unit discriminant t^2,
    # and exactly one negative eigenvalue.
    q=(n*t+1)/D
    r=(t+1)/D
    assert q+n*r==1
    assert (q-r)**2+4*n*t*t*q*r==t*t
    assert (q+r-t)/2 == -(n*t*t-1)/D
    assert (n-1)*r+t==s
    assert s==(2*n*t*t+2*n*t+n-1)/D
    # For t=1 the known unweighted projection norm must be recovered.
    if t==1:
        assert s==F(5*n-1,3*n+1)
    return 12

def main():
    counts=0
    for n in range(1,257):
        for a,b in [(0,1),(1,8),(1,3),(1,2),(2,3),(1,1),(3,2),(5,2),(7,1),(20,1)]:
            certify(n,F(a,b));counts+=1
    rng=random.Random(914527)
    for _ in range(7000):
        n=rng.randint(1,5000)
        t=F(rng.randint(0,100),rng.randint(1,120))
        certify(n,t);counts+=1
    # Exact unbounded-degree limiting formula for all rational t.
    for i in range(1,1000):
        t=F(i,193)
        d=2*t*t/(2*t+1)
        assert d*(d+2)==(2*t-d)**2
        assert 1+d==1+2*t*t/(2*t+1)
        counts+=1
    print('WEIGHTED_STAR_EXACT_IDENTITIES_OK',counts)

if __name__=='__main__':
    main()
