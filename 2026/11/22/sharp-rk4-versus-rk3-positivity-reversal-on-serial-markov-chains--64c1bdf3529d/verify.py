"""Reproducibility checks for positivity horizons of truncated exponential maps.
Uses only Python 3 standard library; finite tests supplement analytic proofs.
"""
from fractions import Fraction as F
from math import factorial


def mul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def markov(rates):
    n = len(rates) + 1
    Q = [[F(0) for _ in range(n)] for _ in range(n)]
    for i, rate in enumerate(rates):
        Q[i][i] = -F(rate)
        Q[i][i+1] = F(rate)
    return Q


def rk(Q, h, order):
    n = len(Q)
    I = [[F(int(i==j)) for j in range(n)] for i in range(n)]
    R = [row[:] for row in I]
    P = I
    for k in range(1, order+1):
        P = mul(P, Q)
        c = F(h)**k / factorial(k)
        for i in range(n):
            for j in range(n):
                R[i][j] += c*P[i][j]
    return R


def homogeneous(seq, k):
    if k == 0: return F(1)
    v = [F(0)]*(k+1)
    v[0] = F(1)
    for a in seq:
        for j in range(1, k+1):
            v[j] += F(a)*v[j-1]
    return v[k]


def closed_entry(rates, i, k, h, order):
    z = list(map(F, rates)) + [F(0)]
    if k > order: return F(0)
    if k == 0:
        return sum((-F(h)*z[i])**j/factorial(j) for j in range(order+1))
    factor = F(h)**k
    for t in range(k): factor *= z[i+t]
    return factor * sum((-F(h))**ell*homogeneous(z[i:i+k+1],ell)/factorial(k+ell)
                         for ell in range(order-k+1))


def bisect(f, lo, hi):
    assert f(lo) > 0 > f(hi)
    for _ in range(95):
        mid = (lo+hi)/2
        if f(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def r3(z): return 1-z+z*z/2-z**3/6

def g4(a,b,h):
    return 1-(a+b)*h/2+(a*a+a*b+b*b)*h*h/6-(a**3+a*a*b+a*b*b+b**3)*h**3/24

rho = bisect(r3, 1, 2)
delta = bisect(lambda z: 1-z/2+z*z/6-z**3/24, 2, 4)
assert 1.5960716379<rho<1.5960716381
assert 2.7852935633<delta<2.7852935636


def limits(rates):
    z = list(map(float,rates))+[0.0]
    M = max(z)
    T = max((sum(z[i:i+3]) for i in range(len(z)-2)), default=0.0)
    H3 = min(rho/M, 3/T if T else float("inf"))
    pair = [bisect(lambda h:g4(z[i],z[i+1],h), 0, 5/max(z[i],z[i+1]))
            for i in range(len(z)-1)]
    if len(z)>=4:
        S = max(sum(z[i:i+4]) for i in range(len(z)-3))
        H4 = min(min(pair),4/S)
    else: H4 = min(pair)
    return H3,H4

checks = 0
for rates in [(1,),(1,2),(2,3,1),(1,2,3,4),(5,2,3,1),(1,1,1,1),
              (1,4,2,3,1),(3,2,1,2,4,1),(7,2,1,3,5,2,1)]:
    Q=markov(rates)
    n=len(Q)
    for p in (3,4):
        for h in (F(1,7),F(2,5),F(3,2),F(17,6)):
            R=rk(Q,h,p)
            for i in range(n):
                assert sum(R[i]) == 1
                checks += 1
                for j in range(n):
                    assert R[i][j] == closed_entry(rates,i,j-i,h,p) if j>=i else R[i][j] == 0
                    checks += 1

for rates in [(1,2,3,4),(4,3,2,1),(2,1,1,2),(5,2,1,2),(1,5,1,1),
              (5,1,1,1),(2,3,5,7),(1,1,1,1,1),(1,2,3,4,5,6)]:
    H3,H4=limits(rates)
    assert 4/(3+rho)-1e-11 <=H4/H3<=delta/rho+1e-11
    checks+=1
    for p,H in ((3,H3),(4,H4)):
        for h,good in ((H*.99999,True),(H*1.00001,False)):
            R=rk(markov(rates),F(h).limit_denominator(100000000),p)
            assert (min(min(row) for row in R)>=0)==good
            checks+=1

b=(3-rho)/2
h3,h4=limits((rho,b,b,rho))
assert abs(h3-1)<1e-12 and abs(h4-4/(3+rho))<1e-12
checks+=2
for eps in (1e-2,1e-3,1e-4):
    h3,h4=limits((1,eps,eps,eps))
    assert abs(h3-rho)<1e-12
    assert h4/h3 < delta/rho and h4/h3 > 1.73
    checks+=2

for rates in [(1,), (1,2), (1,2,3), (4,1,5)]:
    a,b=limits(rates)
    assert b>=a-1e-12
    checks+=1

print('PASS', checks, 'exact matrix/entry checks and finite boundary/ratio checks')
print('rho=',repr(rho),'delta=',repr(delta))
print('sharp lower=',repr(4/(3+rho)),'sharp upper=',repr(delta/rho))
