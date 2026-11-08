"""Reproducible exact and numerical checks for a bit-limited scalar contraction.
Only standard Python and NumPy are needed. No external data or services are used.
"""
from fractions import Fraction
from math import ceil, factorial, isclose, pi
import random
import numpy as np


def ceilfrac(a):
    return -(-a.numerator // a.denominator)


def transition(n, q, r):
    """Exact step-down probabilities, via the two actual rounding operations."""
    B = 2**r
    eps = Fraction(1, q*B)
    assert n < q*B
    result = []
    for j in range(1, n+1):
        z = (1-eps)*j
        fine = Fraction((z*B).numerator // (z*B).denominator, B)
        assert j-1 <= fine <= j
        p_from_rounding = Fraction(j, 1) - fine
        p_closed = Fraction(ceilfrac(Fraction(j,q)), B)
        assert p_from_rounding == p_closed
        result.append(p_closed)
    return result


def moments_exact(ps):
    mean = sum((1/p for p in ps), Fraction(0))
    var = sum(((1-p)/p**2 for p in ps), Fraction(0))
    return mean, var


def hitting_cdf_dynamic(ps, steps):
    n = len(ps)
    states = [Fraction(0) for _ in range(n+1)]
    states[n] = Fraction(1)
    out = []
    for _ in range(steps):
        nxt = [Fraction(0) for _ in range(n+1)]
        nxt[0] = states[0] + states[1]*ps[0]
        for j in range(1,n):
            nxt[j] = states[j]*(1-ps[j-1])+states[j+1]*ps[j]
        nxt[n] = states[n]*(1-ps[n-1])
        states = nxt
        out.append(states[0])
    return out


def hitting_cdf_convolution(ps, steps):
    pmf = [Fraction(0)]* (steps+1)
    pmf[0] = Fraction(1)
    for p in ps:
        new = [Fraction(0)]* (steps+1)
        for t in range(steps+1):
            if pmf[t]:
                power = Fraction(1)
                for m in range(1,steps-t+1):
                    new[t+m] += pmf[t] * p*power
                    power *= (1-p)
        pmf = new
    cumul = Fraction(0)
    out=[]
    for t in range(1,steps+1):
        cumul+=pmf[t]
        out.append(cumul)
    return out


checks=0
for n in range(1,8):
    for q in range(1,9):
        for r in range(2,8):
            if n >= q*(2**r):
                continue
            ps=transition(n,q,r)
            checks += len(ps)*2
            mean,var = moments_exact(ps)
            c = [ceilfrac(Fraction(j,q)) for j in range(1,n+1)]
            assert mean == 2**r*sum((Fraction(1,t) for t in c),Fraction(0))
            assert var == 2**(2*r)*sum((Fraction(1,t*t) for t in c),Fraction(0))-mean
            checks+=2
            steps=n+5
            assert hitting_cdf_dynamic(ps,steps)==hitting_cdf_convolution(ps,steps)
            checks += steps
            if q>=n:
                p=Fraction(1,2**r)
                assert all(x==p for x in ps)
                assert mean==n/p and var==n*(1-p)/p**2
                checks+=2
            if n%q==0:
                m=n//q
                harmonic=sum((Fraction(1,j) for j in range(1,m+1)),Fraction(0))
                assert Fraction(1,q*2**r)*mean==harmonic
                checks+=1

# Exact finite-difference identity for a block probability and log expectation.
for q in range(1,9):
    for m in range(1,10):
        n=q*m
        r=9
        assert n<q*2**r
        ps=transition(n,q,r)
        mean,var=moments_exact(ps)
        H=sum((Fraction(1,j) for j in range(1,m+1)),Fraction(0))
        H2=sum((Fraction(1,j*j) for j in range(1,m+1)),Fraction(0))
        eps=Fraction(1,q*2**r)
        assert eps*mean==H
        assert eps**2*var==Fraction(1,q)*H2-Fraction(1,q*2**r)*H
        checks+=2

# Bounded numerical confirmations: limit variance and the expected q-fold Gumbel convolution.
for q in [1,2,3,5,9]:
    m=2000
    H2=sum(1/j**2 for j in range(1,m+1))
    assert abs(H2/q-pi*pi/(6*q))<1/(q*m)
    checks+=1

rng=np.random.default_rng(240917)
for q in [1,2,4,8]:
    m=800
    n=q*m
    r=18
    B=2**r
    p=np.repeat(np.arange(1,m+1,dtype=float)/B,q)
    # Geometric waiting times, not an approximation to the chain.
    draws=rng.geometric(p, size=(320,n)).sum(axis=1)/(q*B)-np.log(n)
    exact_mean = sum(1/j for j in range(1,m+1))-np.log(n)
    exact_var = (sum(1/j**2 for j in range(1,m+1))-sum(1/j for j in range(1,m+1))/B)/q
    assert abs(draws.mean()-exact_mean)<0.22
    assert abs(draws.var()-exact_var)<0.26
    checks+=2

# Concrete large-q CLT regime via independent geometric waiting times.
n=3000; q=100; r=16
p=np.ceil(np.arange(1,n+1)/q)/(2**r)
means=np.sum(1/p)
vars_=np.sum((1-p)/p**2)
raw=rng.geometric(p, size=(420,n)).sum(axis=1)
z=(raw-means)/np.sqrt(vars_)
assert abs(z.mean())<0.20
assert 0.75<z.var()<1.27
checks+=2

print('PASS', checks, 'exact algebraic / finite-distribution identities and bounded numerical checks')
print('Example q=2 has limiting scaled variance pi^2/12 =',pi*pi/12)
print('Example q=1 has limiting scaled variance pi^2/6 =',pi*pi/6)
print('These finite checks are not proofs of weak convergence.')
