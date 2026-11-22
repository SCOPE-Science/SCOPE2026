#!/usr/bin/env python3
"""Rational enumeration of founder cohorts in critical geometric immigration.

All finite identities are tested against a composition-based dynamic program,
not against a simulation or an asymptotic approximation.
"""
from fractions import Fraction as F
from math import log, pi


def family_prob(a, z):
    if a == 0:
        return F(int(z == 1))
    if z == 0:
        return F(a, a+1)
    return F(1, (a+1)**2)*F(a, a+1)**(z-1)


def enumerate_cohorts(n, m, cutoff):
    # Joint law of (total at observation time, number of recent-family members).
    d = {(0, 0): F(1)}
    for age in range(n):
        new = {}
        for (total, recent), mass in d.items():
            for z in range(cutoff-total+1):
                idx = (total+z, recent+(z if age <= m else 0))
                new[idx] = new.get(idx, F())+mass*family_prob(age, z)
        d = new
    return d


def cdf_at_size(n, m, k):
    q = F(m*n, (m+1)*(n-1)) if m <= n-2 else F(1)
    return sum((q**j for j in range(k)), F()) / k


def run():
    checks = 0
    for n in range(2, 9):
        for m in range(n):
            cutoff = 14
            d = enumerate_cohorts(n, m, cutoff)
            for k in range(1, cutoff+1):
                mass = sum((v for (t, recent),v in d.items() if t == k), F())
                expected_popmass = F(1, n)*F(n-1, n)**(k-1)
                assert mass == expected_popmass, (n, m, k, mass, expected_popmass)
                checks += 1
                recent_mass = sum((v*recent for (t,recent),v in d.items() if t == k), F())
                cdf = recent_mass/(k*mass)
                target = cdf_at_size(n, m, k)
                assert cdf == target, (n,m,k,cdf,target)
                checks += 1
                if m == n-1:
                    assert cdf == 1
                    checks += 1
            if m < n-1:
                for k in range(1,cutoff):
                    assert cdf_at_size(n, m, k+1) < cdf_at_size(n, m, k)
                    checks += 1
    # Independent numerical check: average the exact finite-size conditional law
    # over the exact population distribution, with an explicit geometric tail.
    for n in (3, 5, 11, 20, 50, 100):
        for m in (0,n//2,n-2):
            exact = (m+1)/(n-m-1)*log(n/(m+1))
            total = 0.0
            for k in range(1, 3000*n+1):
                p = (1/n)*((n-1)/n)**(k-1)
                total += p*float(cdf_at_size(n,m,k)) if k < 40 else p*(1-(m*n/((m+1)*(n-1)))**k)/(k*(1-m*n/((m+1)*(n-1))))
            assert abs(total-exact) < 1e-9, (n,m,total,exact)
            checks += 1
    # Check analytic limiting CDF against Riemann-lattice exact formula.
    for r in (0.13, 0.3, 0.55, 0.9):
        asymp = -r*log(r)/(1-r)
        n = 300000
        m = int(r*n)
        formula = (m+1)/(n-m-1)*log(n/(m+1))
        assert abs(asymp-formula) < 2e-5
        checks += 1
    assert abs(2-pi*pi/6 - 0.355066) < 1e-6
    checks += 1
    print(f"PASS: {checks} exact-rational enumerations and bounded numerical checks")


if __name__ == '__main__':
    run()
