"""Reproduce the finite-frequency identity and selected phase-window checks.
No external packages needed for exact checks; mpmath enables optional asymptotic tests.
"""
from fractions import Fraction
from itertools import product
from math import comb

def conditional_cov(M, r):
    return 2*r**(M+1)/(1-r**(M+1))

def exhaustive(n, a, b, p, r):
    q = 1-p
    ans = Fraction(0)
    for bits in product((0,1), repeat=n):
        k = sum(bits)
        M = a**(n-k) * b**k
        ans += p**(n-k)*q**k*conditional_cov(M,r)
    return ans

def grouped(n, a, b, p, r):
    q=1-p
    return sum((comb(n,k)*p**(n-k)*q**k*conditional_cov(a**(n-k)*b**k,r)
                for k in range(n+1)),Fraction(0))

checks=0
for a,b in ((2,3),(2,4),(3,5),(3,9)):
    for p in (Fraction(1,3),Fraction(2,5),Fraction(5,7)):
        for r in (Fraction(1,2), Fraction(2,3)):
            for n in range(0,7):
                assert exhaustive(n,a,b,p,r)==grouped(n,a,b,p,r)
                checks+=1
print('Exact Fourier / word-enumeration identities:',checks)

try:
    import mpmath as mp
    mp.mp.dps=75
    a,b=2,3
    rho=mp.mpf(b)/a
    s=mp.mpf(1)
    for j in (0,1,2):
        threshold=s*(rho-1)*rho**j
        for xi in (-1,0,1):
            for n in (18,25,32):
                L=mp.mpf(a)**n
                tau=threshold-(mp.log(n)-xi)/L
                p=mp.exp(-tau*L)
                q=1-p
                F=lambda k: s*rho**k-tau*k
                Fbase=F(j)
                # Divide by: 2 exp(-s) binom(n,j) exp(-tau*n*L-L*F(j)).
                # All amplitudes are logarithmically reduced before exponentiating.
                total=mp.mpf(0)
                for k in range(n+1):
                    M=L*rho**k
                    coeff=mp.binomial(n,k)/mp.binomial(n,j)*q**k
                    e=mp.exp(-L*(F(k)-Fbase))
                    total+=coeff*e/(1-mp.exp(-s*(1+M)))
                expected=1+mp.exp(xi)/(j+1)
                # The exact finite-n first correction is (n-j)/n times the crossover term.
                finite=1+(n-j)/mp.mpf(n)*mp.exp(xi)/(j+1)
                assert abs(total-finite)<mp.mpf('1e-6'), (j,xi,n,total,finite)
                assert abs(total-expected)<mp.mpf('0.13'), (j,xi,n,total,expected)
                checks+=1
    print('Crossover log-sum identities:',27)
except ImportError:
    print('mpmath unavailable: crossover numerics skipped (proof is analytic)')
print('Total checks:',checks)
