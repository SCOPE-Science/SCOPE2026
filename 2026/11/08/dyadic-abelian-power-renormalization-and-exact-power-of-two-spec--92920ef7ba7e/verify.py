#!/usr/bin/env python3
"""Reproduce finite tests for dyadic Abelian-power renormalization.
All unbounded assertions require the mathematical proof, not these tests.
"""
from fractions import Fraction


def valuation2(z):
    assert z >= 1
    return (z & -z).bit_length() - 1


def word(m, length):
    return [valuation2(i + 1) % m for i in range(length)]


def image_fixedpoint(m, min_length):
    v = [0]
    while len(v) < min_length:
        v = [v0 for c in v for v0 in (0, (c + 1) % m)]
    return v[:min_length]


def parikh_prefix(v, m):
    p = [[0] * m]
    for x in v:
        nxt = p[-1].copy()
        nxt[x] += 1
        p.append(nxt)
    return p


def parikh(pref, i, n):
    return tuple(b - a for a, b in zip(pref[i], pref[i + n]))


def abelian_power(pref, i, d, exponent):
    t = parikh(pref, i, d)
    return all(parikh(pref, i + q * d, d) == t for q in range(1, exponent))


def run():
    checks = 0
    for m in range(2, 10):
        L = 32768
        v = word(m, L)
        assert v[:2048] == image_fixedpoint(m, 2048)
        checks += 2048
        P = parikh_prefix(v, m)
        for k in range(0, 7):
            unit = 1 << k
            # The substitution-block common Parikh vector, independent of the final symbol.
            C = parikh(P, 0, unit - 1)
            for d in range(1, 11):
                for i in range(0, 220):
                    q = i // unit
                    LHS = parikh(P, i, d * unit)
                    BASE = parikh(P, q, d)
                    RHS = tuple(d * C[j] + BASE[(j - k) % m] for j in range(m))
                    assert LHS == RHS, (m, k, d, i, LHS, RHS)
                    checks += 1
            for exponent in range(2, 6):
                d = unit
                for i in range(0, 800):
                    q = i // unit
                    a = q // 2
                    equal = valuation2(a + 1) % m == m - 1
                    pred = equal if exponent == 2 else (equal and q % 2 == 0 if exponent == 3 else False)
                    obs = abelian_power(P, i, d, exponent)
                    assert pred == obs, (m, k, exponent, i, pred, obs)
                    checks += 1
        # Exact combinatorial valuation count on dyadic windows against its periodic truncation.
        # For all residues j modulo 2**R except j=2**R, valuation j is fixed.
        R = m + 6
        count = sum(1 for j in range(1, 1 << R) if valuation2(j) % m == m - 1)
        frac = Fraction(count, (1 << R))
        target = Fraction(1, (1 << m) - 1)
        assert abs(frac - target) <= Fraction(1, (1 << R))
        checks += 1
    print('VERIFY_OK', 'moduli=8', 'shifts=7', 'checks=' + str(checks))


if __name__ == '__main__':
    run()
