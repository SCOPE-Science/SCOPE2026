"""Finite exact-arithmetic diagnostics for Bergman CP-map survival laws.

These checks are finite examples, not proofs of asymptotic or infinite-dimensional statements.
"""
from fractions import Fraction
from math import comb

checks = 0
for rho in (Fraction(1,2), Fraction(1,3), Fraction(2,5), Fraction(3,4)):
    r = [rho + (1-rho)/Fraction(k+1) for k in range(8)]
    assert r[0] == 1
    assert all(r[k] > r[k+1] > rho for k in range(7))
    checks += 2
    for N in range(7):
        coeff = []
        for j in range(N+1):
            c=Fraction(1)
            for i in range(N+1):
                if i != j:
                    c *= r[i]/(r[i]-r[j])
            coeff.append(c)
        assert sum(coeff) == 1
        checks += 1
        mass = [Fraction(1)] + [Fraction(0)] * 8
        for m in range(13):
            survival = sum(mass[:N+1])
            exact = sum(coeff[j]*(1-r[j])**m for j in range(N+1))
            assert survival == exact, (rho,N,m,survival,exact)
            checks += 1
            mass_next = [Fraction(0)]*9
            for k in range(8):
                mass_next[k] += mass[k]*(1-r[k])
                mass_next[k+1] += mass[k]*r[k]
            mass = mass_next
        if N > 0:
            assert coeff[N] == __import__('functools').reduce(
                lambda a,j: a*r[j]/(r[j]-r[N]), range(N), Fraction(1))
            checks += 1
# Confirm exact binomial comparison bound for the Bernoulli baseline.
for rho in (Fraction(1,2), Fraction(1,3), Fraction(2,5)):
    for t in range(1,15):
        exp = sum(Fraction(comb(t,k))*rho**k*(1-rho)**(t-k)/(k+1)
                  for k in range(t+1))
        rhs = (1-(1-rho)**(t+1))/((t+1)*rho)
        assert exp == rhs
        checks+=1
print('BERGMAN_CP_BIRTH_DIAGNOSTICS_OK',checks)
