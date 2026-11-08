"""Finite consistency tests for fixed-gap Hartogs numerator boundary layers.

Requires mpmath. These tests do not replace the proof for all parameters.
"""
import math
from collections import defaultdict
import mpmath as mp

mp.mp.dps = 75
checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def centered_coefficients(k, n):
    m = n + k
    out = defaultdict(int)
    for A in range(-m + 1, m):
        b0 = -(n * A) // m
        for B in range(b0 - 2, b0 + 3):
            V = n * A + m * B
            if abs(V) < m:
                out[k + A + B] += (m - abs(A)) * (m - abs(V))
    return [out[j] for j in range(2 * k + 1)]

def original_coefficients(k, n):
    m = n + k
    c = [0] * (2 * k + 1)
    c[k] += m * m
    for j in range(m - 1):
        L = (1 + n * (j + 1) + m - 1) // m
        kap = m + n - 1 + n * j - m * L
        ex = j + 1 - L
        for shift, coeff in (
            (0, (j + 1) * (kap + 1)),
            (1, (j + 1) * (m - kap - 1)),
            (k, (m - j - 1) * (kap + 1)),
            (k + 1, (m - j - 1) * (m - kap - 1)),
        ):
            c[ex + shift] += coeff
    return c

def limiting_coefficients(k):
    c = [0] * (2 * k + 1)
    geom = [1] * k
    tri = [0] * (2 * k - 1)
    for a in range(k):
        for b in range(k):
            tri[a + b] += 1
    for j, t in enumerate(tri):
        c[j] += t
        c[j + 1] += 4 * t
        c[j + 2] += t
    return c

def radial_constant(k, j, m):
    h = j * pow(m, -1, k) % k
    theta = 2 * mp.pi * j / k
    return mp.sqrt(
        24 * mp.sin(mp.pi * j / k) ** 4
        / ((4 + 2 * mp.cos(theta)) * mp.sin(mp.pi * h / k) ** 2)
    )

for k in range(1, 11):
    for n in range(1, 36):
        if math.gcd(k, n) != 1:
            continue
        coeff = centered_coefficients(k, n)
        check(coeff == original_coefficients(k, n), f'source normalization k={k},n={n}')
        check(coeff == coeff[::-1], f'reciprocity k={k},n={n}')
        check(sum(coeff) == (k+n)**3, f'normalization k={k},n={n}')

for k in range(2, 11):
    for n in range(1, 32):
        if math.gcd(k, n) != 1:
            continue
        m = n + k
        coeff = centered_coefficients(k, n)
        for j in range(1, k):
            theta = 2 * mp.pi * j/k
            root = mp.e ** (1j*theta)
            val = sum(c * root**r for r,c in enumerate(coeff)) / root**k
            h = (j*pow(m,-1,k)) % k
            expected = m*mp.sin(mp.pi*j/k)**2/mp.sin(mp.pi*h/k)**2
            check(abs(val-expected) < mp.mpf('1e-60')*(1+expected),
                  f'root-of-unity exact fiber k={k},n={n},j={j}')

for k in range(1, 12):
    for n in (101, 211):
        if math.gcd(n,k)!=1:
            continue
        m=k+n
        c=centered_coefficients(k,n)
        p=limiting_coefficients(k)
        errs=[abs(mp.mpf(6*k*k)*c[j]/m**3 - p[j]) for j in range(2*k+1)]
        check(max(errs)<mp.mpf(200000)/m**2,
              f'quadrature consistency k={k},n={n}')

# Local zero computations are a numerical supplement to the analytical root argument.
for k, n in [(3,61),(4,61),(5,61),(5,62),(5,63),(5,64),(6,61),(6,121)]:
    m=n+k
    coeff=centered_coefficients(k,n)
    sc=mp.mpf(coeff[-1])
    roots=mp.polyroots([mp.mpf(v)/sc for v in coeff[::-1]],
                       maxsteps=1500,extraprec=110,error=False)
    inside=[z for z in roots if abs(z)<1]
    check(len(inside)==k, f'inner count k={k},n={n}')
    for j in range(1,k):
        theta=2*mp.pi*j/k
        picked=min(inside,key=lambda z: abs(mp.arg(z)-theta) if j<=k//2 else abs(mp.arg(z)-(theta-2*mp.pi)))
        expected=radial_constant(k,j,m)
        observed=m*(1-abs(picked))
        check(abs(observed-expected)<mp.mpf('0.40'),
              f'boundary layer k={k},n={n},j={j}: {observed}, {expected}')

print(f'PASS: {checks} finite exact and numerical consistency checks')
