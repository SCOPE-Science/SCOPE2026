"""Reproducible finite checks of analytic weighted-Haar/BV identities.

Tests use exact fractions for key identities; they do not establish the
infinite-dimensional theorem or certify global maxima numerically.
"""
from fractions import Fraction as Q
from math import isclose, pi, log, sqrt

checks = 0

def expect(t, description):
    global checks
    checks += 1
    if not t:
        raise AssertionError(description)

def phi(x):
    x = x % 1
    return min(x, 1-x)

def v(x):
    x = x % 1
    return x*(1-x)

def F(r, x, n):
    ans, fac = Q(0), Q(1)
    for _ in range(n):
        ans += fac*phi(x)**2
        fac *= r
        x = (2*x)%1
    return ans

# Calibration identity, exact on rational points in both tent branches.
for den in range(2,61):
    for num in range(den+1):
        x = Q(num,den)
        T = (2*x)%1
        expect(phi(x)**2 == Q(1,9) + Q(2,3)*(v(x)-v(T)) - (phi(x)-Q(1,3))**2,
               'calibrated squared-tent identity')

# Compare Haar-step coefficient obtained by direct interval integration.
for k in range(8):
    L = Q(1,2**k)
    for j in range(2**k):
        left=j*L; right=(j+1)*L; mid=(left+right)/2
        for h in range(1,16):
            t=left + Q(h,16)*L
            # Integrating h_{k,j} against 1_[t,1] amounts to
            # coefficient = -2^(k/2) * min(t-left, right-t).
            predicted_scaled= -min(t-left,right-t)*2**k
            actual_scaled= ((left-t) if t < mid else (t-right))/L
            expect(predicted_scaled == actual_scaled == -phi(t/L), 'Haar step coefficient')

# Exact s=0 Parseval identity for dyadic jumps, all finite coefficients.
for k in range(1,12):
    d=2**k
    for j in range(d+1):
        x=Q(j,d)
        expect(F(Q(1,2), x,k+1)==x*(1-x), 'dyadic Parseval')

# On dyadic jumps the improvement expression is exact.
for r in (Q(51,100),Q(3,5),Q(3,4),Q(9,10)):
    for m in range(2,30):
        x=Q(1,2)-Q(1,2**m)
        exact= -Q(1,2**m)+Q(1,4**m)*(1+sum((4*r)**k for k in range(1,m)))
        expect(F(r,x,m+1)-Q(1,4)==exact, 'dyadic jump advantage identity')
    expect(any(F(r,Q(1,2)-Q(1,2**m),m+1)>Q(1,4) for m in range(2,30)),
           'positive-s smoothness improves midpoint')

# The repeating doubling orbit of 1/3 gives a closed discounted lower bound.
for r in (Q(1,10),Q(1,2),Q(3,4),Q(9,10),Q(99,100)):
    for n in (1,2,9,35):
        expect(F(r,Q(1,3),n) == (1-r**n)/(9*(1-r)), 'period-two orbit sum')

# Finite approximate tent sums obey the certified uniform upper bound.
for r in (Q(1,2),Q(3,5),Q(9,10),Q(99,100)):
    bound=Q(1,9)/(1-r)+Q(1,6)
    for d in range(2,22):
        for j in range(d+1):
            expect(F(r,Q(j,d),80) <= bound, 'calibration upper bound')

# For every r < 1, on any maximizing jump the occupation variance
# is at most (1-r)/6. The finite test here validates only the algebraic
# pointwise inequality used to establish that statement.
for r in (Q(51,100),Q(2,3),Q(3,4),Q(9,10)):
    for d in range(2,30):
        for j in range(d+1):
            x=Q(j,d)
            left=F(r,x,60)
            # Discounted telescoping accounting for finite tail.
            y=x; vv=Q(0); defect=Q(0)
            for k in range(60):
                vv += r**k * (v(y)-v((2*y)%1))
                defect += r**k * (phi(y)-Q(1,3))**2
                y=(2*y)%1
            right= (1-r**60)/(9*(1-r))+Q(2,3)*vv-defect
            expect(left==right, 'discounted telescoping')

print(f'PASS: {checks} exact rational assertions; analytic proof required for infinite claims.')
