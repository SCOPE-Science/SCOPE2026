"""Exact finite checks for the 11-adic residue theorem on three-column lonesum counts.

Requires Python 3 standard library only. This checks finite levels; the infinite
classification is proved separately by analytic lifting and the quadratic normal form.
"""
from collections import Counter
from math import comb

P = 11
BASES = (4, 3, 2)
COEFFS = (6, -6, 1)
R = 10
NORMAL = {0: 1, 1: 1, 2: 1, 4: 1, 5: 2, 8: 1, 10: 2}


def value(n, modulus):
    return sum(c * pow(a, n, modulus) for a, c in zip(BASES, COEFFS)) % modulus


def log_unit_mod(a, modulus_exponent):
    """log(a^10) modulo 11^N, summing terms with rigorous valuation cutoff."""
    p = P
    modulus = p ** modulus_exponent
    u = pow(a, R, modulus) - 1
    total = 0
    # For j>=3N the valuation of u^j/j exceeds N.
    for j in range(1, 3 * modulus_exponent + 5):
        q = j
        v = 0
        while q % p == 0:
            v += 1
            q //= p
        if j-v >= modulus_exponent:
            continue
        t = pow(u, j, modulus * p**v) // p**v
        term = t * pow(q, -1, modulus) % modulus
        total = (total + (term if j & 1 else -term)) % modulus
    return total


def critical_data(level):
    """Return critical value and quadratic unit modulo p^level.

    The 11-adic critical point is found at the precision needed to identify
    the translated square at modulus 11^(level+2).
    """
    if level == 0:
        return value(5, P*P), 1
    precision = level + 2
    mod = P**precision
    logs = tuple(log_unit_mod(a, precision) for a in BASES)

    def derivative(t):
        numerator = sum(c * pow(a, 5, mod) * pow(pow(a, R, mod), t, mod) * v
                        for a, c, v in zip(BASES, COEFFS, logs)) % mod
        assert numerator % (P*P) == 0
        return numerator // (P*P)

    t = 0
    for j in range(1, level + 1):
        matches = [t + d * P**(j-1) for d in range(P)
                   if derivative(t + d * P**(j-1)) % P**j == 0]
        assert len(matches) == 1, (j, matches)
        t = matches[0]
    a = value(5 + R * t, mod)
    second = sum(c * pow(a0, 5, mod) * pow(pow(a0, R, mod), t, mod) * v*v
                 for a0, c, v in zip(BASES, COEFFS, logs)) % mod
    assert second % (P*P) == 0
    unit = (second // (P*P)) * pow(2, -1, P**level) % P**level
    assert t % P == 4 and unit % P == 7
    return a, unit


def roots_of_square_mod(z, m):
    if m == 0:
        return 1
    mod = P**m
    z %= mod
    if z == 0:
        return P**(m//2)
    v = 0
    while z % P == 0:
        z //= P
        v += 1
    if v & 1:
        return 0
    if pow(z % P, (P-1)//2, P) != 1:
        return 0
    return 2 * P**(v//2)


def predicted_fiber(y, k, a, u):
    result = NORMAL.get(y % P, 0)
    if k == 1:
        return result + (y % P == 10)
    if (y - a) % (P*P):
        return result
    m = k-2
    if not m:
        return result + P
    z = ((y-a)//(P*P) * pow(u, -1, P**m)) % P**m
    return result + P * roots_of_square_mod(z, m)


def check():
    assert [value(n, 10**8) for n in range(5)] == [1, 8, 46, 230, 1066]
    normal_residues = []
    for r in range(R):
        first = sum(c * a**r * ((a**R-1)//P)
                    for a, c in zip(BASES, COEFFS)) % P
        if r == 5:
            assert first == 0
            c1 = sum(c*a**r*(a**R-1) for a,c in zip(BASES,COEFFS))
            c2 = sum(c*a**r*(a**R-1)**2 for a,c in zip(BASES,COEFFS))
            assert c1 % P**2 == 0 and c1//P**2 % P == 6
            assert c2 % P**2 == 0 and c2//P**2 % P == 3
        else:
            assert first != 0
            normal_residues.append(value(r, P))
    assert Counter(normal_residues) == Counter(NORMAL)
    for k in range(1, 6):
        mod = P**k
        period = R * P**(k-1)
        observed = Counter(value(n, mod) for n in range(period))
        if k == 1:
            a = u = 0
        else:
            a, u = critical_data(k-2)
            assert a % (P*P) == 120
        assert len(observed) == len(NORMAL)*P**(k-1)
        for y in range(mod):
            assert observed[y] == predicted_fiber(y, k, a, u), (k, y, observed[y], predicted_fiber(y,k,a,u))
        assert sum(observed.values()) == period
        if k <= 4:
            divisors = [d for d in range(1, period) if period%d==0]
            values = [value(n, mod) for n in range(period)]
            assert all(any(values[n] != values[n%d] for n in range(period)) for d in divisors)
        print(f'k={k}: period={period}, image={len(observed)}, min_fiber={min(observed.values())}, max_fiber={max(observed.values())}; checks passed')

if __name__ == '__main__':
    check()
