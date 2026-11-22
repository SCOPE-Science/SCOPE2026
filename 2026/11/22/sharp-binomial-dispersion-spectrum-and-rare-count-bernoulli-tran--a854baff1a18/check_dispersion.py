"""Standalone checks for the quadratic-weighted beta-binomial dispersion theorem.

The analytical proof handles arbitrary real parameters and all positive integers n>=2.
These finite tests only validate normalization, a rational witness, and numerical
asymptotic behavior; they do not substitute for that proof.
"""
from fractions import Fraction as F
from math import comb, sqrt, fsum


def baseline(n, a, b):
    a, b = F(a), F(b)
    den = F(1)
    for j in range(n):
        den *= a + b + j
    result = []
    for x in range(n + 1):
        num = F(comb(n, x))
        for j in range(x):
            num *= a + j
        for j in range(n - x):
            num *= b + j
        result.append(num / den)
    assert sum(result) == 1
    return result


def base_moments(n, a, b):
    a, b = F(a), F(b)
    mu = n * a / (a + b)
    var = n * a * b * (a + b + n) / ((a + b)**2 * (a + b + 1))
    return mu, var


def weighted_exact_scaled_q(n, a, b, t):
    """Pass q=t*sigma so each weight is an exact rational number."""
    mu, var = base_moments(n, a, b)
    p = baseline(n, a, b)
    q_squared = F(t)**2 * var
    w = [p[k] * (1 + (1 - F(t) * (k - mu))**2) / (2 + q_squared)
         for k in range(n + 1)]
    assert sum(w) == 1
    return w


def dispersion(n, masses):
    mu = sum(k*p for k,p in enumerate(masses))
    var = sum((k - mu)**2*p for k,p in enumerate(masses))
    return var / (mu * (1 - mu/F(n)))


def weighted_float(n, a, b, q):
    p = baseline(n, a, b)
    mu, var = base_moments(n, a, b)
    m, sigma = float(mu), sqrt(float(var))
    values = [float(v)*(1+(1-q*(k-m)/sigma)**2)/(2+q*q)
              for k,v in enumerate(p)]
    assert abs(fsum(values)-1.0) < 3e-10
    return values


def main():
    checks = 0
    for n in (2,3,4,7,15):
        for a in (1,2,7):
            for b in (1,3,10,100):
                for t in (-50,-3,0,2,20,50):
                    masses = weighted_exact_scaled_q(n,a,b,t)
                    val = dispersion(n,masses)
                    assert 0 < val < n
                    checks += 1
                # Unweighted beta-binomial has exact relative dispersion factor.
                masses = weighted_exact_scaled_q(n,a,b,0)
                assert dispersion(n,masses) == F(a+b+n,a+b+1)
                checks += 1
    # Entirely rational certificate of strict equimean-binomial underdispersion.
    n, a, b, t = 2, 1, 100, 50
    masses = weighted_exact_scaled_q(n,a,b,t)
    result = dispersion(n,masses)
    assert result == F(2329513809177953,9120943935192402)
    assert result < F(1,3)
    checks += 2
    print('Exact rational witness R:', result, float(result))
    # Fixed nonzero q rare-event Bernoulli law, and the first-order TV rate.
    for n,a,q in ((2,1,3.0),(7,2,-2.0),(4,F(1,2),1.0)):
        limit = q*q/(2+q*q)
        tv_constant = 2*abs(q)*sqrt(n*float(a))/(2+q*q)
        for beta in (10000,100000):
            probs = weighted_float(n,a,beta,q)
            tv = .5*(abs(probs[0]-(1-limit)) + abs(probs[1]-limit) + sum(probs[2:]))
            assert abs(sqrt(beta)*tv-tv_constant) < 0.06
            checks += 1
    print('Fixed q rare-event Bernoulli and TV limit tests passed.')
    print('Total assertions groups passed:',checks)


if __name__ == '__main__':
    main()
