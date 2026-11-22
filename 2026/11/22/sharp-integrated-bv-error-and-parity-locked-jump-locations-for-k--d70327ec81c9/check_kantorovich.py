"""Standalone finite sanity checks for the stated classical Kantorovich BV-to-L1 theorem.
The mathematical argument is in RESULT.md; these tests do not establish infinite quantifiers.
Run: python3 check_kantorovich.py
"""
from fractions import Fraction as F
from math import comb, sqrt, pi, floor
import random


def binom_pmf(n, k, s):
    return F(comb(n,k)) * s**k * (1-s)**(n-k)


def integral_basis(n,k,s):
    # Exact antiderivative via binomial tail.
    return sum(binom_pmf(n+1,z,s) for z in range(k+1,n+2))/F(n+1)


def error_jump(n,s):
    if s==0 or s==1: return F(0)
    N=n+1; j=min(n, (N*s).numerator//(N*s).denominator)
    u=N*s-j
    return 2*(sum(integral_basis(n,k,s) for k in range(j+1,n+1)) + (1-u)*integral_basis(n,j,s))


def peak(n,j):
    s=F(j+1,n+2)
    return 2*F(comb(n,j))*s**(j+1)*(1-s)**(n-j+1)


# Exact symbolic-identity consequences at every interior cell maximum.
exact_count=0
for n in range(0,29):
    vals=[]
    for j in range(n+1):
        s=F(j+1,n+2)
        ej=error_jump(n,s)
        assert ej == peak(n,j), (n,j,ej,peak(n,j))
        vals.append(ej)
        exact_count+=1
        # Test derivative sign change by strict local neighborhoods in same cell.
        h=F(1,20*(n+1)*(n+2))
        assert error_jump(n,s-h)<ej and error_jump(n,s+h)<ej
        exact_count+=2
    best=max(vals)
    winners=[j for j,v in enumerate(vals) if v==best]
    assert winners == ([n//2] if n%2==0 else [(n-1)//2,(n+1)//2]), (n,winners)
    assert vals == vals[::-1]
    if n%2==0:
        m=n//2
        assert best == F(comb(2*m,m),2*4**m)
    else:
        m=(n-1)//2
        assert best==2*F(comb(2*m+1,m))*F(m+1,2*m+3)**(m+1)*F(m+2,2*m+3)**(m+2)
    exact_count+=3
print('EXACT_CELL_PEAK_SYMMETRY_PARITY_CHECKS_PASS', exact_count)

# Direct rational evaluation of the step response and the exact L1 error.
rng=random.Random(246801)
checks=0
for n in range(0,14):
    for _ in range(80):
        s=F(rng.randint(1,99),100)
        N=n+1; j=min(n, int(N*s)); u=N*s-j
        q=lambda x: sum(binom_pmf(n,k,x) for k in range(j+1,n+1))+(1-u)*binom_pmf(n,j,x)
        assert 0<=q(F(1,7))<=1 and 0<=q(F(4,7))<=1
        mass=sum(F(1,N) for k in range(j+1,n+1))+(1-u)*F(1,N)
        assert mass==1-s
        # Analytical derivative inside the cell: q(s)-N integral p_j.
        deriv_half=q(s)-N*integral_basis(n,j,s)
        assert deriv_half==binom_pmf(n,j,s)*(j+1-(n+2)*s)
        checks+=3
print('EXACT_KERNEL_MARGINAL_AND_DERIVATIVE_CHECKS_PASS',checks)

# Dense numerical quadrature for random signed multi-jump BV inputs.
try:
    import numpy as np
    from scipy.special import comb as sccomb
    rng2=random.Random(117)
    count=0
    for n in (0,1,2,3,5,8,12,20):
        x=np.linspace(0,1,30001)
        ps=np.stack([sccomb(n,k)*x**k*(1-x)**(n-k) for k in range(n+1)])
        C=float(max(peak(n,j) for j in range(n+1)))
        for _ in range(110):
            jumps=sorted(rng2.uniform(.02,.98) for i in range(rng2.randrange(1,7)))
            coeffs=[rng2.uniform(-1,1) for s in jumps]
            f=np.zeros_like(x); Kf=np.zeros_like(x)
            for s,c in zip(jumps,coeffs):
                j=min(n,int((n+1)*s));u=(n+1)*s-j
                f+=c*(x>s)
                Kf+=c*(ps[j+1:,:].sum(axis=0)+(1-u)*ps[j,:])
            error=np.trapezoid(np.abs(Kf-f),x)
            assert error <= C*sum(map(abs,coeffs))+0.0004, (n,error,C)
            count+=1
    print('NUMERICAL_SIGNED_MULTIJUMP_CHECKS_PASS',count)
except ImportError:
    print('NUMERICAL_SIGNED_MULTIJUMP_CHECKS_SKIPPED_MISSING_NUMPY_SCIPY')

for n in (100,101,400,401,1000,1001):
    # Floating point evaluation of exact formula (no large integers converted directly).
    import math
    from math import lgamma,log
    j=n//2
    s=(j+1)/(n+2)
    logc=math.log(2)+lgamma(n+1)-lgamma(j+1)-lgamma(n-j+1)+(j+1)*log(s)+(n-j+1)*math.log1p(-s)
    scaled=math.exp(logc)*sqrt(n)
    assert abs(scaled - 1/sqrt(2*pi))<0.05
print('ASYMPTOTIC_SCALE_SANITY_PASS')
print('ALL_KANTOROVICH_BV_L1_CHECKS_PASS')
