#!/usr/bin/env python3
"""Finite consistency tests for a deterministic two-Hermite spectral-zero theorem.

These checks supplement, but do not prove, the infinite-family theorem.
Only the Python standard library is required.
"""
import cmath
import math

COUNT = 0


def check(condition, label):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(label)


def R(s, m, k):
    d = m - k
    return s ** (d / 2) * abs(m - s) / abs(k - s)


def pivots(m, k):
    d = m - k
    if d <= 2 + math.sqrt(8 * k):
        return []
    D = (d - 2) ** 2 - 8 * k
    return [(m + k - 2 - math.sqrt(D)) / 2,
            (m + k - 2 + math.sqrt(D)) / 2]


def bisect_for(slo, shi, m, k, c):
    # R is strictly monotone inside each subinterval.
    f_lo = R(slo, m, k) - c
    f_hi = R(shi, m, k) - c
    check(f_lo * f_hi < 0, 'bracket')
    for _ in range(110):
        mid = (slo + shi) / 2
        fm = R(mid, m, k) - c
        if fm * f_lo <= 0:
            shi = mid
            f_hi = fm
        else:
            slo = mid
            f_lo = fm
    return (slo + shi) / 2


def rings(m, k, c):
    T = pivots(m, k)
    barriers = [0., float(k)] + T + [float(m), math.inf]
    roots = []
    for lo, hi in zip(barriers, barriers[1:]):
        L = 1e-12 if lo == 0 else math.nextafter(lo, math.inf)
        H = (max(float(m) + 100, (2 * c) ** (2 / (m - k)) + 100)
             if math.isinf(hi) else math.nextafter(hi, -math.inf))
        if (R(L, m, k) - c) * (R(H, m, k) - c) < 0:
            roots.append(bisect_for(L, H, m, k, c))
    return roots


def analytic_charge(s, m, k):
    # Numerator of d/ds log(R(s)), multiplied by denominators.
    if s < k or s > m:
        return 1
    P = (m - s) * (s - k) - 2 * s
    return 1 if P > 0 else -1


def G(z, m, k, c):
    return m * z ** (m - 1) + c * k * z ** (k - 1) - z.conjugate() * (z ** m + c * z ** k)


def jacobian(z, m, k, c):
    F = z ** m + c * z ** k
    Fp = m * z ** (m - 1) + c * k * z ** (k - 1)
    Fpp = m * (m - 1) * z ** (m - 2)
    if k >= 2:
        Fpp += c * k * (k - 1) * z ** (k - 2)
    return abs(Fpp - z.conjugate() * Fp) ** 2 - abs(F) ** 2


def test_one(m, k, c):
    d = m - k
    rr = rings(m, k, c)
    if pivots(m, k):
        sm, sp = pivots(m, k)
        cm, cp = R(sm, m, k), R(sp, m, k)
        expected = 5 if cm < c < cp else 3
    else:
        expected = 3
    check(len(rr) == expected, f'rings m={m} k={k} c={c}')
    check(rr == sorted(rr), 'ordered rings')
    for s in rr:
        check(abs(R(s, m, k) / c - 1) < 1e-7, 'radial amplitude')
        phi0 = math.pi / d if s < k or s > m else 0.0
        for j in range(d):
            z = math.sqrt(s) * cmath.exp(1j * (phi0 + 2 * j * math.pi / d))
            scale = max(1., abs(m * z ** (m-1)), abs(c * k * z ** (k-1)))
            check(abs(G(z, m, k, c)) / scale < 5e-8, 'STFT zero')
            J = jacobian(z, m, k, c)
            check(J * analytic_charge(s, m, k) > 0, 'charged zero')
    signed = sum(d * analytic_charge(s, m, k) for s in rr) + (k - 1)
    check(signed == m - 1, 'total signed index')
    if k >= 2:
        check(abs(G(0j, m, k, c)) < 1e-14, 'origin')
    else:
        check(abs(G(0j, m, k, c) - c) < 1e-14, 'origin excluded')


def main():
    for m in range(2, 12):
        for k in range(1, m):
            test_one(m, k, 1.0)
            pp = pivots(m, k)
            if pp:
                s0, s1 = pp
                cm, cp = R(s0, m, k), R(s1, m, k)
                check(k < s0 < s1 < m and cm < cp, 'ordered folds')
                test_one(m, k, (cm + cp) / 2)
                test_one(m, k, cm / 2)
                test_one(m, k, cp * 2)
    check(not pivots(5, 1), 'smallest absent degree')
    check(pivots(6, 1) == [2.0, 3.0], 'smallest degree roots')
    low, high = [R(s, 6, 1) for s in (2, 3)]
    check(abs(low - 2 ** (9 / 2)) < 1e-12, 'lower fold exact')
    check(abs(high - 3 ** (7 / 2) / 2) < 1e-12, 'upper fold exact')
    for t in (1, 2, 3):
        k = 2 * t * t
        m = 2 * (t + 1) * (t + 1)
        d = m - k
        sstar = 2 * t * (t + 1)
        cstar = sstar ** (d / 2) * (t + 1) / t
        check((d - 2)**2 == 8 * k, 'resonant integer equality')
        check(abs(R(sstar, m, k) / cstar - 1) < 1e-14, 'cubic contact amplitude')
        for s in (sstar - 0.25, sstar, sstar + 0.25):
            P = (m - s) * (s - k) - 2 * s
            check(abs(P + (s - sstar)**2) < 1e-9, 'double critical root')
        if t <= 2:
            z = math.sqrt(sstar)
            check(abs(G(z, m, k, cstar)) / (abs(cstar * k * z**(k-1)) + 1) < 1e-11,
                  'resonance polynomial zero')
            Fp = m * z**(m-1) + cstar*k*z**(k-1)
            Fpp = m*(m-1)*z**(m-2) + cstar*k*(k-1)*z**(k-2)
            Jscale = abs(Fpp-z*Fp)**2 + abs(z**m+cstar*z**k)**2
            check(abs(jacobian(z,m,k,cstar)) / Jscale < 1e-11,
                  'resonant zero Jacobian vanishes')
    print('PASS:', COUNT, 'finite assertions; no exhaustive proof is claimed')

if __name__ == '__main__':
    main()
