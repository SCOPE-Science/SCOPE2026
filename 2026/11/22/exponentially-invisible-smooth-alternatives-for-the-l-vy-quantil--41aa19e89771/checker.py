"""Reproduce numerical checks for a quantile-band blindness theorem.

Standard-library-only script; mathematical proof is in RESULT.md.
Run: python3 checker.py
"""
from math import comb, exp, log, pi, sqrt, sin
from statistics import NormalDist
from random import Random

P, R, EPS = 0.4, 0.7, 0.1
nd = NormalDist()
checks = 0

def check(statement, comment):
    global checks
    if not statement:
        raise AssertionError(comment)
    checks += 1

def Q(u):
    assert 0 < u < 1
    z = nd.inv_cdf(1-u/2)
    return 1/(z*z)

def bump(u):
    return sin(pi*(u-P)/(R-P))**4 if P < u < R else 0.0

def Qe(u):
    return Q(u) + EPS*bump(u)

def k1(n): return int(0.3*n + 1e-10)
def k2(n): return int(0.8*n + 1e-10)+1
def j2(n): return int(0.95*n + 1e-10)

def statistic_ratio(sample):
    n = len(sample)
    assert k1(n)>=1 and j2(n)>=k2(n)
    s = sorted(sample)
    low = sum(s[:k1(n)])/k1(n)
    hi = sum(s[k2(n)-1:j2(n)])/(j2(n)-k2(n)+1)
    return low/hi

def pmf(n,p,k):
    return comb(n,k)*p**k*(1-p)**(n-k)

def lo_tail(n,p,k): return sum(pmf(n,p,j) for j in range(k+1))
def hi_tail(n,p,k): return sum(pmf(n,p,j) for j in range(k,n+1))
def kl(x,p): return x*log(x/p)+(1-x)*log((1-x)/(1-p))

# A global analytic derivative bound: Q' >= 1 / sup f_Levy.
f_max = 3**1.5 * exp(-1.5)/sqrt(2*pi)
max_bump_derivative = 3*sqrt(3)*pi/(4*(R-P))
check(1/f_max - EPS*max_bump_derivative > 0.8, 'strict global monotonicity margin')
for i in range(1,10000):
    u = i/10000
    check(abs(Qe(u)-Q(u)) < 1e-14 if u<=P or u>=R else Qe(u)>Q(u), 'identity outside / change inside')
    if i>1:
        check(Qe(u) > Qe((i-1)/10000), 'strict monotonicity grid')

# Finite-sample coupling: every ordered sample on the safe event gives identical ratio.
rng = Random(20261116)
for n in (20,50,100,200,500):
    for trial in range(900):
        U = sorted(rng.random() for _ in range(n))
        Np = sum(u<=P for u in U)
        Nq = sum(u<=R for u in U)
        a=statistic_ratio([Q(u) for u in U]); b=statistic_ratio([Qe(u) for u in U])
        if Np>=k1(n) and Nq<k2(n):
            check(abs(a-b) <= 3e-12*max(1,abs(a)), 'exact equality on safe event')
        if Np==k1(n)-1 and k1(n)<=Nq<k2(n):
            check(b>a, 'strict direction on lower excursion')

# Exact binomial bounds and fixed-rank large-deviation constants.
Dlo=kl(.3,.4); Dhi=kl(.8,.7)
check(Dlo<Dhi, 'dominant lower-rank excursion')
for n in (20,50,100,200,500,1000):
    k=k1(n); ell=k2(n)
    bd=lo_tail(n,P,k-1)+hi_tail(n,R,ell)
    Chernoff=exp(-n*kl((k-1)/n,P))+exp(-n*kl(ell/n,R))
    check(bd<=Chernoff*(1+1e-10), 'Chernoff bound')
    # Lower bound on probability of disagreement in the explicit quantile coupling.
    m=n-k+1
    cond=sum(pmf(m,(R-P)/(1-P),j) for j in range(1,ell-k+1))
    lower=pmf(n,P,k-1)*cond
    check(0<lower<=bd*(1+1e-10), 'lower event subset of upper event')
    print(f'n={n:4d}: coupling-disagreement lower={lower:.9g}, upper={bd:.9g}, Chernoff={Chernoff:.9g}')

# Observable non-null alternative: its CDF at the original median-quantile is different.
x0=Q(.55)
lo, hi=P,R
for _ in range(100):
    mid=(lo+hi)/2
    if Qe(mid)<x0: lo=mid
    else: hi=mid
u_alt=(lo+hi)/2
delta=.55-u_alt
check(0<delta<0.1, 'strictly distinguishable distributions')
print(f'KL exponents: lower={Dlo:.15f}; upper={Dhi:.15f}')
print(f'CDF separation at x=Q(.55) : delta={delta:.12f}')
print(f'Assertions passed: {checks}')
