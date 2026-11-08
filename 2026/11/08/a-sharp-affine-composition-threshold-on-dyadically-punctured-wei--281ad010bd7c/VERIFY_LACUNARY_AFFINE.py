"""Finite checks of binomial Gram and sparse-weight identities.

Run with Python 3: python VERIFY_LACUNARY_AFFINE.py
Only the analytical argument proves the universal theorem.
"""
from fractions import Fraction
from math import comb, sqrt, pi

checks = 0

def beta(j, alpha):
    if j and (j & (j-1)) == 0:
        return Fraction(1, j**alpha)
    return Fraction(1)

def p(n, j, t):
    if 0 <= j <= n:
        return Fraction(comb(n,j))*t**j*(1-t)**(n-j)
    return Fraction(0)

# Exact Vandermonde equality at the symmetric affine parameter.
t = Fraction(1,2)
for n in range(29):
    for m in range(29):
        gram = sum((p(n,j,t)*p(m,j,t) for j in range(min(n,m)+1)),Fraction(0))
        assert gram == Fraction(comb(n+m,n),2**(n+m))
        checks += 1

# Exact weighted loss formula for several nonsymmetric affine parameters.
for t in (Fraction(1,3),Fraction(1,2),Fraction(2,3)):
    for alpha in (0,1,2):
        for n in (1,2,4,8,16,32):
            for m in (1,2,4,8,16,32):
                h2 = sum((p(n,j,t)*p(m,j,t)
                          for j in range(min(n,m)+1)),Fraction(0))
                direct = sum((beta(j,alpha)*p(n,j,t)*p(m,j,t)
                              for j in range(min(n,m)+1)),Fraction(0))
                loss = sum(((1-beta(j,alpha))*p(n,j,t)*p(m,j,t)
                            for j in range(min(n,m)+1)
                            if j and (j & (j-1)) == 0),Fraction(0))
                assert h2 - loss == direct
                checks += 1

# Exact moment/Markov overlap certificate for each rational example.
# The universal proof chooses u>1 sufficiently close to 1 for each 0<t<1.
u = Fraction(6,5)
for t in (Fraction(1,3),Fraction(1,2),Fraction(2,3)):
    rho_sq = (1-t+t*u)*(1-t+t/u)**2
    assert rho_sq < 1
    checks += 1

# Critical diagonal check at increasing dyadic scales, numerical only.
for t in (Fraction(1,3),Fraction(1,2),Fraction(2,3)):
    tf=float(t)
    c=1/(2*sqrt(pi*tf*(1-tf)))
    for k in range(5,10):
        n=2**k
        row=[float(p(n,j,t)) for j in range(n+1)]
        h2=sum(x*x for x in row)
        loss=sum((1-(1<<j)**(-0.5))*row[1<<j]**2 for j in range(k+1))
        scaled=sqrt(n)*(h2-loss)
        assert abs(scaled-c)<0.15
        checks += 1

print('LACUNARY_AFFINE_BINOMIAL_CHECKS_OK', checks)
