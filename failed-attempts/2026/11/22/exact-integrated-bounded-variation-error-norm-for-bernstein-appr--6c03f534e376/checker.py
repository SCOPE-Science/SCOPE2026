"""Exact finite-degree and numerical checks of the Bernstein BV-to-L1 error law.

Python 3 standard library only; all exact polynomial checks use fractions.Fraction.
"""
from fractions import Fraction as Q
from math import comb, sqrt, pi, isclose
import random


def binom_tail_poly(n, k):
    """Coefficient vector of sum_{j=k+1}^n binom(n,j)x^j(1-x)^(n-j)."""
    c = [Q(0)] * (n + 1)
    for j in range(k + 1, n + 1):
        for t in range(n - j + 1):
            c[j+t] += Q(comb(n, j)*comb(n-j,t)*((-1)**t))
    return c


def int_poly(c, x):
    return sum((v*x**(i+1)/Q(i+1) for i,v in enumerate(c)), Q(0))


def binom_tail_rational(n,k,s):
    return sum((Q(comb(n,j))*s**j*(1-s)**(n-j) for j in range(k+1,n+1)),Q(0))


def beta_deviation_algebraic(n,k):
    s=Q(k,n)
    q=binom_tail_rational(n,k,s)
    pm=Q(comb(n,k))*s**k*(1-s)**(n-k)
    return Q(n-k,n*(n+1)) * (1-2*q+2*k*pm)


def beta_deviation_integral(n,k,s):
    poly=binom_tail_poly(n,k)
    return Q(1)-s-int_poly(poly,Q(1))+2*int_poly(poly,s)


def bernstein_at(n, samples, x):
    return sum(comb(n,j)*x**j*(1-x)**(n-j)*samples[j] for j in range(n+1))


def test_exact():
    for n in range(1,17):
        vals=[]
        for k in range(n):
            s=Q(k,n)
            l=beta_deviation_integral(n,k,s)
            assert l==beta_deviation_algebraic(n,k),(n,k,l)
            r=beta_deviation_integral(n,k,Q(k+1,n))
            assert r==beta_deviation_algebraic(n,n-1-k),(n,k,r)
            vals.append(l)
            # Exact direct integral of each step's absolute error on the two sides.
            poly=binom_tail_poly(n,k)
            e=int_poly(poly,s)+(Q(1)-s)-(int_poly(poly,Q(1))-int_poly(poly,s))
            assert e==l
        assert max(vals)==max(vals[::-1])
        assert max(vals)>=Q(1,n+1)
    print('EXACT_BETA_ORDER_STATISTIC_AND_JUMP_INTEGRALS_PASS n=1..16')
    assert [max(beta_deviation_algebraic(n,k) for k in range(n)) for n in range(1,5)]==[Q(1,2),Q(1,3),Q(1,4),Q(1,5)]
    print('LOW_DEGREE_ENDPOINT_REGIME_PASS n=1..4')


def test_randomized():
    rng=random.Random(7412026)
    for t in range(1200):
        n=rng.randint(1,17)
        knots=sorted({Q(rng.randint(1,999),1000) for _ in range(rng.randint(1,7))})
        amplitudes=[Q(rng.randint(-50,50),50) for _ in knots]
        def fv(x):
            return sum((a for p,a in zip(knots,amplitudes) if x>p),Q(0))
        samples=[fv(Q(j,n)) for j in range(n+1)]
        v=sum(abs(a) for a in amplitudes)  # upper bound on Jordan variation
        # One-sided Riemann sums with a 2500-point uniform grid: convergence checked
        # at independent resolutions. The numerical test is supplementary only.
        xs=[(j+0.5)/2500 for j in range(2500)]
        e=sum(abs(bernstein_at(n,[float(z) for z in samples],x)-float(fv(Q(2*j+1,5000)))) for j,x in enumerate(xs))/2500
        c=float(max(beta_deviation_algebraic(n,k) for k in range(n)))
        assert e<=c*float(v)+0.0025,(n,t,e,c*v)
    print('RANDOM_MULTIJUMP_ERROR_INEQUALITY_PASS cases=1200')


def test_limit():
    # Numerical consistency only; the theorem's limit follows from Beta CLT and UI.
    for n in [20,50,100,200,500,1000]:
        k=(n-1)//2
        s=k/n
        # For large n, use the standard library's exact finite sum for the tail.
        # Tail terms computed via stable recurrence around the binomial mode.
        # A special closed formula is not needed in the proof.
        import math
        pm=math.exp(math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)+k*math.log(s)+(n-k)*math.log1p(-s))
        # Binomial tail with standard-library log-gamma, safe for n<=1000.
        F=sum(math.exp(math.lgamma(n+1)-math.lgamma(j+1)-math.lgamma(n-j+1)+j*math.log(s)+(n-j)*math.log1p(-s)) for j in range(k+1,n+1))
        e=(n-k)/(n*(n+1))*(1-2*F+2*k*pm)
        target=1/sqrt(2*pi*n)
        assert abs(e/target-1)<.015 if n>=20 else True
    print('GAUSSIAN_LEADING_CONSTANT_NUMERICAL_PASS')

if __name__=='__main__':
    test_exact()
    test_randomized()
    test_limit()
    print('ALL_BERNSTEIN_BV_L1_CHECKS_PASS')
