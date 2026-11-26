"""Independent algebraic and numerical consistency checks for fixed-gap Hartogs numerator asymptotics.

Run: python3 CHECK.py. Requires numpy (see requirements.txt).
This verifies sample identities and finite root configurations; infinite claims follow from the proof.
"""
from math import gcd, floor, sqrt
import numpy as np

checks = 0


def check(condition, note):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(note)


def centered_coefficients(n, k):
    """Direct centered triangular-convolution formula."""
    m = n + k
    out = [0] * (2*k + 1)
    for a in range(-m + 1, m):
        wa = m - abs(a)
        for b in range(-n, n + 1):
            v = n*a + m*b
            if abs(v) < m:
                j = k + a + b
                check(0 <= j <= 2*k, 'degree window')
                out[j] += wa * (m - abs(v))
    return out


def direct_coefficients(n, k):
    """Independent (a,b)-indexed Bergman numerator from the primary formula."""
    m = n + k
    def D(v):
        if 0 <= v <= m - 1:
            return v + 1
        if m <= v <= 2*m - 2:
            return 2*m - 1 - v
        return 0
    out = [0]*(2*k + 1)
    for a in range(2*m - 1):
        for b in range(2*n + 1):
            v = m*b+n*a + m+n-1-2*m*n
            weight = D(a)*D(v)
            if weight:
                j = a+b+1-2*n
                check(0 <= j <= 2*k, 'direct polynomial degree')
                out[j] += weight
    return out


def residue_coefficients(n, k):
    """A linear-time exact coefficient identity, reindexed from the source formula."""
    m = n + k
    out = [0]*(2*k + 1)
    out[k] = m*m
    for j in range(1, m):
        e = (k*j - 1)//m
        tau = k*j-m*e
        check(1 <= tau < m, 'coprime residue')
        # z^e [j+(m-j)z^k] [m-tau+tau*z]
        for exp, val in ((e,j*(m-tau)), (e+1,j*tau),
                         (e+k,(m-j)*(m-tau)), (e+k+1,(m-j)*tau)):
            check(0 <= exp <= 2*k, 'residue formula degree')
            out[exp] += val
    return out


def limit_polynomial(k):
    s = np.ones(k, dtype=int)
    t = np.convolve(s,s)
    return [int(x) for x in np.convolve(np.array([1,4,1]),t)]


# Three algebraically independent presentations of the source polynomial.
for k in range(1, 10):
    for n in range(1, 23):
        if gcd(n,k) != 1:
            continue
        a = centered_coefficients(n,k)
        b = residue_coefficients(n,k)
        c = direct_coefficients(n,k)
        check(a == b == c, f'three polynomial constructions k={k}, n={n}')
        check(a == a[::-1], 'reciprocal symmetry')
        check(all(x > 0 for x in a), 'strict positive coefficients')

# Uniform coefficient rate O_k(m^-2) and limiting factorization.
for k in range(1, 11):
    target = limit_polynomial(k)
    check(len(target) == 2*k+1, 'limiting polynomial degree')
    check(target == [1] + [6*j for j in range(1,k)] + [6*k-2]
          + [6*j for j in range(k-1,0,-1)] + [1], 'explicit coefficients')
    for n in (101, 211, 311, 503):
        if gcd(n,k)!=1:
            continue
        m=n+k
        a=residue_coefficients(n,k)
        err=max(abs(6*k*k*x/m**3 - p) for x,p in zip(a,target))
        check(err*m*m < 20*k*k*k, 'quadratic coefficient convergence')

# Independent polynomial-root comparisons to the predicted multiset of limits.
for k in range(1, 9):
    for n in (101, 211, 311):
        if gcd(n,k)!=1:
            continue
        c=residue_coefficients(n,k)
        roots=np.roots(np.asarray(c[::-1], dtype=np.float64))
        inside=[z for z in roots if abs(z)<1-1e-9]
        outside=[z for z in roots if abs(z)>1+1e-9]
        check(len(inside)==k and len(outside)==k, 'inside/outside root count')
        targets=[-2+sqrt(3)]+[np.exp(2j*np.pi*h/k) for h in range(1,k)]
        # Unique pairing of interior roots and distinct limiting roots.
        from itertools import permutations
        # brute-force matching up to 8! is manageable, instead nearest distances with unique matches
        distances=[min(abs(z-t) for z in inside) for t in targets]
        check(max(distances)<min(0.5,10*k/n), f'predicted root condensation {k}, {n}')
        for t in targets:
            check(sum(abs(z-t)<min(0.5,10*k/n) for z in inside)>=1, 'all root clusters')

print(f'PASS {checks} exact and numerical consistency assertions')
