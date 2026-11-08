"""Reproducible small-instance core tests and two-quota binomial checks.

Requires Python >=3.10 and scipy. Analytic all-size claims are proved in RESULT.md.
"""
from math import comb, sqrt
from scipy.optimize import linprog
from scipy.stats import binom, norm


def core_predicate(a, b, r, s):
    q = min(a // r, b // s)
    if q == 0:
        return True
    return a == q * r or b == q * s


def core_lp(a, b, r, s):
    n = a + b
    q = min(a // r, b // s)
    rows, rhs = [], []
    for mask in range(1, (1 << n) - 1):
        i = (mask & ((1 << a) - 1)).bit_count()
        j = (mask >> a).bit_count()
        value = min(i // r, j // s)
        rows.append([-((mask >> t) & 1) for t in range(n)])
        rhs.append(-value)
    sol = linprog([0.0] * n, A_ub=rows, b_ub=rhs,
                  A_eq=[[1.0] * n], b_eq=[float(q)],
                  bounds=(0, None), method='highs')
    return bool(sol.success)


def membership_event(a, m, r, s):
    b = m - a
    if a < r or b < s:
        return False
    q = min(a // r, b // s)
    return a == q * r or b == q * s


def threshold_event(a, m, r, s):
    b = m - a
    if a < r or b < s:
        return False
    return ((a * (r + s) <= m * r and a % r == 0)
            or (a * (r + s) >= m * r and b % s == 0))


def exact_fraction_probability(m, r, s, u, v):
    # Conditional on at least r objects of type A and s of type B.
    den, num = 0, 0
    for a in range(r, m - s + 1):
        weight = comb(m, a) * u**a * (v-u)**(m-a)
        den += weight
        if membership_event(a, m, r, s):
            num += weight
    from fractions import Fraction
    return Fraction(num, den)


def binomial_probability(m, r, s, p):
    valid = binom.sf(r-1,m,p) - binom.sf(m-s,m,p)
    prob = sum(float(binom.pmf(a,m,p)) for a in range(r,m-s+1)
               if membership_event(a,m,r,s))
    return prob / valid


def critical_limit(r,s,beta):
    sigma = sqrt(r*s)/(r+s)
    return float(norm.cdf(-beta/sigma)/r + norm.cdf(beta/sigma)/s)


def main():
    lp_tests=0
    for a in range(1,7):
        for b in range(1,7):
            if a+b>11:
                continue
            for r in range(1,a+1):
                for s in range(1,b+1):
                    assert core_lp(a,b,r,s)==core_predicate(a,b,r,s), (a,b,r,s)
                    lp_tests+=1
    event_tests=0
    for r in range(2,6):
        for s in range(2,6):
            for m in range(r+s,35):
                for a in range(m+1):
                    assert threshold_event(a,m,r,s)==membership_event(a,m,r,s)
                    event_tests+=1
    fraction_tests=0
    for m in range(5,18):
        for r,s in [(2,3),(2,4),(3,2)]:
            if m<r+s:
                continue
            f=exact_fraction_probability(m,r,s,2,5)
            # Compare independent summation using the threshold predicate.
            weights=[comb(m,a)*2**a*3**(m-a) for a in range(r,m-s+1)]
            n=sum(w for a,w in zip(range(r,m-s+1),weights)
                  if threshold_event(a,m,r,s))
            from fractions import Fraction
            assert f==Fraction(n,sum(weights))
            fraction_tests+=1
    checks=[]
    for r,s in [(2,3),(3,4),(2,5)]:
        p0=r/(r+s)
        for beta in [-0.6,0.0,0.6]:
            limit=critical_limit(r,s,beta)
            obs=binomial_probability(12000,r,s,p0+beta/sqrt(12000))
            assert abs(obs-limit)<0.005, (r,s,beta,obs,limit)
            checks.append((r,s,beta,round(obs,6),round(limit,6)))
    print('PASS core_LP=',lp_tests,'exact_event_equivalences=',event_tests,
          'exact_fraction_compares=',fraction_tests,'large_m_asymptotic_checks=',len(checks))
    for entry in checks:
        print('  ',entry)

if __name__=='__main__':
    main()
