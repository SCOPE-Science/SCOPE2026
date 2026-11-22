"""Exact upper-tail checks for equally stratified uniform one-dimensional samples.
Public reproducibility code; uses only Python 3 standard library and NumPy.
"""
from fractions import Fraction as F
from math import comb, exp, factorial
from itertools import combinations
import random
import numpy as np

def pgf_coeffs(n, delta):
    # E[(1+v)^N], with v=z-1, for n independent strata
    q=delta*delta/2
    return [F(comb(n-k,k))*q**k for k in range((n)//2+1)]

def no_large_gap(n,delta):
    return sum(((-1)**k)*a for k,a in enumerate(pgf_coeffs(n,delta)))

def independent_sets(n):
    # events indexed 0,...,n-2, count subsets without consecutive indices
    nums=[]
    for k in range(n//2+1):
        t=sum(all(b-a>=2 for a,b in zip(s,s[1:])) for s in combinations(range(n-1),k))
        nums.append(t)
    return nums

def analytic_numerical_cdf(n,delta,grid=10001):
    # Integration transfer, independent of inclusion-exclusion derivation.
    x=np.linspace(0,1,grid)
    c=1-float(delta)
    f=np.ones_like(x)
    for _ in range(n-1):
        # f_next(v)=integral_{max(0,v-c)}^1 f(u)du
        cum=np.zeros(grid)
        cum[1:]=np.cumsum((f[:-1]+f[1:])/(2*(grid-1)))
        lo=np.maximum(0,x-c)
        f=cum[-1]-np.interp(lo,x,cum)
    return np.trapezoid(f,x)

def test():
    tests=0
    for n in range(2,16):
        a=independent_sets(n)
        for k,ak in enumerate(a):
            assert ak==comb(n-k,k)
            tests+=1
        for delta in [F(1,12),F(1,4),F(2,5),F(1,2)]:
            q=delta*delta/2
            ps=pgf_coeffs(n,delta)
            assert ps==[F(c)*q**k for k,c in enumerate(a)]
            tests+=1
            assert no_large_gap(n,delta)==(no_large_gap(n-1,delta)-q*no_large_gap(n-2,delta) if n>=4 else no_large_gap(n,delta))
            tests+=1
            assert F(0)<no_large_gap(n,delta)<F(1)
            tests+=1
            # Exact factorial moments of large-gap count.
            mean=ps[1]
            variance=mean + 2*(ps[2] if len(ps)>2 else F(0))-mean*mean
            assert mean==(n-1)*q
            assert variance==(n-1)*q-(3*n-5)*q*q
            tests+=1
    for n in [2,3,4,5,7,9]:
        for delta in [F(1,4),F(1,3),F(1,2)]:
            predicted=float(no_large_gap(n,delta))
            by_integral=analytic_numerical_cdf(n,delta,4001)
            assert abs(by_integral-predicted)<0.00013,(n,delta,by_integral,predicted)
            tests+=1
    # asymptotic Poisson zero-event probability from exact polynomial
    for t in [0.5,1,2]:
        target=exp(-t*t/2)
        n=10000
        q=t*t/(2*n)
        # Float recurrence of the exact hard-core path polynomial, avoids huge rational denominators.
        a,b=1.0,1.0-q
        for nn in range(3,n+1):
            a,b=b,b-q*a
        exact=b
        assert abs(exact-target)<0.0003,(t,exact,target)
        tests+=1
    # Finite Monte Carlo comparison is only illustrative, NOT a proof.
    seed=20261116
    rng=random.Random(seed)
    n=10;delta=F(1,3)
    samples=60000
    hit=0
    for _ in range(samples):
        u=[rng.random() for j in range(n)]
        maxscaled=max(u[0],1-u[-1],*(1+u[j+1]-u[j] for j in range(n-1)))
        hit+= maxscaled<=2-float(delta)
    frequency=hit/samples
    predicted=float(no_large_gap(n,delta))
    assert abs(frequency-predicted)<0.013,(frequency,predicted)
    tests+=1
    print('PASS',tests,'exact identities and numerical comparisons; random seed',seed)
    print('n=10 delta=1/3: exact',predicted,'simulation',frequency)
    print('Rayleigh survival t=1:',exp(-0.5))

if __name__=='__main__': test()
