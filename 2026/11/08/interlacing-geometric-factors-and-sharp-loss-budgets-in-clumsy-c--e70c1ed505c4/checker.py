"""Exact rational checks for heterogeneous clumsy coupon stopping times.

Standalone: Python 3 standard library only. Compares an independently
assembled absorbing-state Markov system to proposed integral identities.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial


def solve(A, b):
    n = len(A)
    A = [list(row) + [b[i]] for i, row in enumerate(A)]
    for j in range(n):
        pivot = next((i for i in range(j,n) if A[i][j]), None)
        assert pivot is not None
        A[j], A[pivot] = A[pivot], A[j]
        scale = A[j][j]
        for k in range(j, n+1):
            A[j][k] /= scale
        for i in range(n):
            if i == j: continue
            w = A[i][j]
            if not w: continue
            for k in range(j,n+1):
                A[i][k] -= w*A[j][k]
    return [A[i][n] for i in range(n)]


def absorbing(ps, z=None):
    m = len(ps)
    full = (1 << m) - 1
    M = full
    A = [[F(int(a==b)) for b in range(M)] for a in range(M)]
    rhs = [F(1) if z is None else F(0) for _ in range(M)]
    for mask in range(M):
        for i,p in enumerate(ps):
            for nextmask, prob in [(mask | (1<<i),1-p),(mask & ~(1<<i),p)]:
                if not prob: continue
                prob /= m
                if z is not None:
                    prob *= z
                if nextmask == full:
                    if z is not None: rhs[mask] += prob
                else:
                    A[mask][nextmask] -= prob
    return solve(A,rhs)[0]


def product_polynomial(rs):
    c=[F(1)]
    for r in rs:
        nc=[F(0)]*(len(c)+1)
        for k,v in enumerate(c):
            nc[k]+=v
            nc[k+1]+=v*r
        c=nc
    return c


def explicit_pgf(ps,z):
    m=len(ps)
    r=[p/(1-p) for p in ps]
    v=m*(1-z)/z
    A=sum((F((-1)**k*comb(m,k),1)/(v+k) for k in range(m+1)),F(0))
    B=sum((a/(v+k) for k,a in enumerate(product_polynomial(r))),F(0))
    return A/B


def explicit_mean(ps):
    m=len(ps)
    rs=[p/(1-p) for p in ps]
    return m*sum((a-F((-1)**k*comb(m,k)))/k
                 for k,a in enumerate(product_polynomial(rs)) if k)


def exp_fast_mean(m,P):
    return m*sum((F(1,k) for k in range(1,m+1)),F(0))+m*P/(1-P)


def exp_min_mean(m,P):
    r=P/(m-P)
    return m*sum((F(1,k) for k in range(1,m+1)),F(0)) + m*sum((F(comb(m,k))*r**k/k for k in range(1,m+1)),F(0))


def geometric_sum_pgf(m,P,z):
    s=(1-z)/z
    res=1/(1+m*s/(1-P))
    for j in range(2,m+1): res*=F(j)/(j+m*s)
    return res


def check():
    nchecks=0
    presets={
      2:[(F(0),F(0)),(F(1,3),F(1,5)),(F(1,2),F(0)),(F(1,4),F(1,4))],
      3:[(F(0),)*3,(F(1,3),F(1,7),F(2,9)),(F(1,2),F(0),F(0)),(F(1,6),)*3],
      4:[(F(0),)*4,(F(1,3),F(1,7),F(2,9),F(1,11)),(F(1,2),F(0),F(0),F(0)),(F(1,8),)*4]
    }
    for m, vectors in presets.items():
        for ps in vectors:
            mean1=absorbing(ps)
            mean2=explicit_mean(ps)
            assert mean1==mean2,(m,ps,mean1,mean2)
            nchecks+=1
            for z in (F(1,2),F(2,3),F(4,5)):
                x=absorbing(ps,z); y=explicit_pgf(ps,z)
                assert x==y,(m,ps,z,x,y)
                nchecks+=1
    for m in range(2,7):
        for P in (F(0),F(1,7),F(1,2),F(4,5)):
            hi=(P,)+(F(0),)*(m-1)
            lo=(P/m,)*m
            assert explicit_mean(hi)==exp_fast_mean(m,P)
            assert explicit_mean(lo)==exp_min_mean(m,P)
            assert explicit_mean(hi)>=explicit_mean(lo)
            nchecks+=3
            for z in (F(1,2),F(2,3),F(4,5)):
                assert explicit_pgf(hi,z)==geometric_sum_pgf(m,P,z)
                assert explicit_pgf(hi,z)<=explicit_pgf(lo,z)
                nchecks+=2
    # Independent exact certificates for the alternating-sign root interlacing.
    # Q(v) is obtained by multiplying the denominator Stieltjes transform
    # by the full lattice pole polynomial, without root-finding tolerances.
    for m in range(2,7):
        profiles=[(F(0),)*m,(F(1,3),)+(F(0),)*(m-1),
                  (F(1,5),)*m,
                  tuple(F((i+1),2*(m+1)) for i in range(m))]
        for ps in profiles:
            e=product_polynomial([p/(1-p) for p in ps])
            for j in range(m+1):
                v=-j
                Q=sum((e[k]*__import__('math').prod((v+l for l in range(m+1) if l!=k))
                       for k in range(m+1)),F(0))
                target=F((-1)**j * factorial(j) * factorial(m-j))*e[j]
                assert Q==target
                nchecks+=1
            d=sum(bool(p) for p in ps)
            for j in range(1,d+1):
                lhs=(-1)**j * factorial(j)*factorial(m-j)*e[j]
                rhs=(-1)**(j-1)*factorial(j-1)*factorial(m-j+1)*e[j-1]
                assert lhs*rhs<0
                nchecks+=1
    # Verify strict pair-balancing for rational p with the same total budget.
    for m in range(2,6):
        for P in (F(1,5),F(2,3)):
            xs=(P,)+(F(0),)*(m-1)
            ys=(P/2,P/2)+(F(0),)*(m-2)
            assert explicit_mean(xs)>explicit_mean(ys)
            nchecks+=1
            for z in (F(1,4),F(1,2),F(3,4)):
                assert explicit_pgf(xs,z)<explicit_pgf(ys,z)
                nchecks+=1
    print('PASS:',nchecks,'independent exact rational assertions')


if __name__=='__main__': check()
