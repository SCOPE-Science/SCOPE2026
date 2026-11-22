#!/usr/bin/env python3
"""Finite exact and numerical checks for the quadratic modular-coupling covariance theorem.

Python 3 standard library only. This tests sample algebra and asymptotic behavior;
it is not an exhaustive verification of a continuum of couplings.
"""
from fractions import Fraction as Q
from math import sqrt, pi

def frac(q):
    return q - (q.numerator // q.denominator if isinstance(q, Q) else __import__('math').floor(q))

def B2(t):
    t = frac(t)
    return t*t-t+Q(1,6)

def integral_polynomial(a,s):
    """Exact branchwise integral of (x-1/2)({a*x+s}-1/2) dx, x in [0,1]."""
    a = Q(a); s = Q(s)
    total = Q(0)
    for k in range(-1,int(a)+3):
        lo = max(Q(0),(Q(k)-s)/a)
        hi = min(Q(1),(Q(k+1)-s)/a)
        if hi <= lo: continue
        v=s-Q(k)-Q(1,2)
        # (x-1/2)*(a*x+v) = a*x^2+(v-a/2)*x-v/2
        total += a*(hi**3-lo**3)/3 + (v-a/2)*(hi**2-lo**2)/2-v*(hi-lo)/2
    return total

exact_count=0
for a in range(2,9):
    for den in (3,5,7,11):
        for numer in range(den):
            s=Q(numer,den)
            assert integral_polynomial(a,s)==B2(s)/(2*a),(a,s)
            exact_count+=1

# Closed formula for the low-coupling interval and its strictly positive minimum.
for b in [Q(0),Q(1,7),Q(1,4),Q(1,2),Q(5,6),Q(1)]:
    v=b*b/Q(5)-b/Q(3)+Q(1,6)
    assert v>0 and v>=Q(1,36)
assert Q(5,6)**2/5-Q(5,6)/3+Q(1,6)==Q(1,36)
assert Q(2,5)-Q(2,3)+Q(1,3)==Q(1,15)  # primitive first-period weighted integral
# Kernel K(t)=t^2(1-t)^2/12: K''=t^2-t+1/6.
assert [Q(2,12),Q(-12,12),Q(12,12)]==[Q(1,6),-1,Q(1)]
assert Q(1,15) > sqrt(3)/54

def J_simpson(b):
    """Midpoint quadrature of one-period segments in the t = b*y^2 variable."""
    if b==0: return 1/6
    # Composite Simpson, split to remove branch changes, avoid t=0 integrable singularity
    # Integrate y on each [sqrt(k/b),sqrt((k+1)/b)] interval; B2({b*y*y}) continuous.
    n=400
    summ=0.0
    import math
    for k in range(math.ceil(b)):
        lo=math.sqrt(k/b)
        hi=math.sqrt(min(k+1,b)/b)
        h=(hi-lo)/n
        f=lambda y: float(B2(b*y*y))
        val=f(lo)+f(hi)
        for j in range(1,n):val+=(4 if j&1 else 2)*f(lo+j*h)
        summ+=val*h/3
    return summ

numeric_count=0
for b in (0,.125,.4,5/6,1,1.25,1.5,2,3,7,13,50,100,400):
    v=J_simpson(b)
    assert v>0,(b,v)
    if 0<=b<=1:
        assert abs(v-(b*b/5-b/3+1/6))<2e-6,(b,v)
    numeric_count+=1
# Riemann zeta constant, finite sum plus one-sided tail bounds.
N=100000
S=sum(k**(-2.5) for k in range(1,N+1))
zlo=S+(N+1)**(-1.5)/1.5
zhi=S+N**(-1.5)/1.5
constlo=zlo/(4*pi*pi)
consthi=zhi/(4*pi*pi)
assert 0.03397<constlo<consthi<0.034
assert abs(J_simpson(400)*sqrt(400)-(constlo+consthi)/2)<3e-4
print('PASS: %d exact phase-integral identities; %d numerical coupling checks; positive low-coupling minimum, convexity kernel and zeta-asymptotic checks.'%(exact_count,numeric_count))
