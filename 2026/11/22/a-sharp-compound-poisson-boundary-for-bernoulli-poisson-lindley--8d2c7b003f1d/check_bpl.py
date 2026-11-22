"""Exact arithmetic checks for the Bernoulli--Poisson--Lindley law.

Requires only Python 3 standard library. This checks formulas and finite examples;
full infinite-support conclusions follow from the analytical proof.
"""
from fractions import Fraction as Q
from math import log

checks = 0
for theta in (Q(1,5), Q(1,2), Q(1), Q(2), Q(5)):
    q = 1/(1+theta)
    r = 1/(2+theta)
    critical = 1/(2+theta)
    for alpha in (critical/2, critical, (1+critical)/2, Q(9,10)):
        b = alpha/(1-alpha)
        p0 = (1-alpha)*theta**2*(theta+2)/(theta+1)**3
        assert (1-alpha)*(1+b)*(1-r) == (1-alpha)/(1-alpha)*(1-r)
        assert p0*(1+b)*(1-r)/(1-q)**2 == 1
        checks += 2
        def plmass(k):
            return theta**2*(k+theta+2)/(theta+1)**(k+3)
        def mass(k):
            return (1-alpha)*plmass(k) + (alpha*plmass(k-1) if k else Q(0))
        assert mass(0) == p0
        checks += 1
        masses = [mass(j)/p0 for j in range(16)]
        # Independently derive each logarithmic coefficient recursively from masses.
        coeff = [Q(0)]*16
        for k in range(1,16):
            coeff[k] = masses[k] - sum(Q(j,k)*coeff[j]*masses[k-j]
                                           for j in range(1,k))
            claimed = (2*q**k-r**k+(-1)**(k+1)*b**k)/k
            assert coeff[k] == claimed, (alpha, theta, k)
            checks += 1
        if alpha <= critical:
            for k in range(1,101):
                assert 2*q**k-r**k+(-1)**(k+1)*b**k > 0
                checks += 1
        else:
            assert any(2*q**(2*m)-r**(2*m)-b**(2*m)<0 for m in range(1,200))
            checks += 1

# A concrete overdispersed parameter choice that is not infinitely divisible.
q, r, b = Q(1,2), Q(1,3), Q(1)
assert (2*q**2-r**2-b**2)/2 == -Q(11,36)
alpha, theta = Q(1,2), Q(1)
mean = alpha + (2+theta)/(theta*(theta+1))
variance = (2+theta*(6+theta*(4+theta+(1-alpha)*alpha*(1+theta)**2))) / (theta**2*(theta+1)**2)
assert mean == 2 and variance == Q(7,2) and variance>mean
checks += 2

# Non-proof numerical illustration of the first forbidden coefficient index.
for theta in (0.4,1.0,3.0):
    rho = (1+theta)/(2+theta)
    for delta in (0.1,0.05,0.02,0.01):
        k = next(2*m for m in range(1,10000)
                 if (1+delta)**(2*m)+rho**(2*m)>2)
        assert abs(k*log(1+delta)-log(2)) < .16
        checks += 1

print(f'PASS: {checks} formula and finite-example assertions')
