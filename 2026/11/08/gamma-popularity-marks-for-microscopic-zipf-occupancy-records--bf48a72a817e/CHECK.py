#!/usr/bin/env python3
"""Independent finite combinatorial and asymptotic sanity checks for Zipf r-record marks.
Uses Python standard library only; tests do not replace the proof.
"""
import math
from fractions import Fraction

checks=0

def assert_close(x,y,tol=1e-8):
    global checks
    assert math.isfinite(x) and abs(x-y)<=tol, (x,y,tol)
    checks+=1

def assert_equal(x,y):
    global checks
    assert x==y, (x,y)
    checks+=1

# Exact finite-n multinomial occupancy probability vs explicit joint counting:
# Draws from four categories with nonuniform rational probabilities.
p=[Fraction(1,2),Fraction(1,4),Fraction(1,8),Fraction(1,8)]
for n in range(1,9):
    for a in range(n+1):
        for b in range(n-a+1):
            joint=(Fraction(math.factorial(n),math.factorial(a)*math.factorial(b)*math.factorial(n-a-b))
                   *p[0]**a*p[1]**b*(1-p[0]-p[1])**(n-a-b))
            brute=Fraction(0)
            # Reduce four-category distribution to three-category by merging 2 and 3.
            for k in range(n-a-b+1):
                z=n-a-b-k
                brute+=(Fraction(math.factorial(n),math.factorial(a)*math.factorial(b)*math.factorial(k)*math.factorial(z))
                        *p[0]**a*p[1]**b*p[2]**k*p[3]**z)
            assert_equal(joint,brute)

# Exact first-hit/single-future-hit approximation for each prefix state and window.
for n in range(1,9):
    for m in range(1,9):
        for r in range(1,5):
            for prob in [Fraction(1,3),Fraction(1,5),Fraction(1,11)]:
                eligibility=(math.comb(n,r-1)*prob**(r-1)*(1-prob)**(n-r+1) if r-1<=n else Fraction(0))
                # Exact chance prefix count r-1 and at least one future hit.
                exact=eligibility*(1-(1-prob)**m)
                first_order=eligibility*m*prob
                assert_equal(exact<=first_order,True)
                assert_equal(first_order-exact<=eligibility*Fraction(m*(m-1),2)*prob**2,True)

# Numerical Zipf tail, r intensity constants and Gamma mark transformation.
a=2.0
gamma=1/a
c=6/(math.pi**2)
lam=1.4
for r in range(1,5):
    total=lam*gamma*(c**gamma)*math.gamma(r-gamma)/math.factorial(r-1)
    # Numerically integrate the y-transformed (Gamma) density via uniform midpoint rule.
    step=0.001
    integral=0.0
    for i in range(1,30001):
        y=(i-0.5)*step
        integral+= (lam*gamma*c**gamma/math.factorial(r-1))*y**(r-1-gamma)*math.exp(-y)*step
    assert_close(integral,total,0.012)

# Deterministic (annealed) rank intensity converges to its explicit limit.
# Numerical tests only: finite-n binomial occupancy probabilities via loggamma.
for n in (10000,1000000):
    m=math.floor(lam*n**(1-gamma))
    limit_rank=400000
    for r in (1,2,3):
        weighted=0.0
        for j in range(1,limit_rank+1):
            pj=c/(j*j)
            k=r-1
            logpr=(math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)
                   +k*math.log(pj)+(n-k)*math.log1p(-pj))
            weighted+=pj*math.exp(logpr)
        rate=m*weighted
        expected=lam*gamma*c**gamma*math.gamma(r-gamma)/math.factorial(r-1)
        assert_close(rate/expected,1.0,0.04 if n==10000 else 0.01)

print(f'PASS: {checks} standalone exact/numeric assertions')
