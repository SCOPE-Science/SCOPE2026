#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

def M(n, lam, r):
    lam = Fraction(lam)
    if r == 0:
        return (Fraction(1) - 2 * lam / n) ** n
    if r <= lam:
        return ((n - 2 * lam + r) / (n - r)) ** (n - r)
    return ((2 * lam - r) / r) ** r

def base_bounds(n, lam):
    lam = Fraction(lam)
    assert 0 <= lam <= Fraction(n, 2)
    max_r = int(2 * lam)
    even = [r for r in range(max_r + 1) if r % 2 == 0]
    hi = max(M(n, lam, r) for r in even)
    if lam <= Fraction(1, 2):
        lo = 1 - 2 * lam
    else:
        odd = [r for r in range(1, max_r + 1, 2)]
        lo = -max(M(n, lam, r) for r in odd)
    return lo, hi

def bias_bounds(n, lam):
    lam = Fraction(lam)
    assert 0 <= lam <= n
    if lam <= Fraction(n, 2):
        return base_bounds(n, lam)
    lo, hi = base_bounds(n, n - lam)
    return (lo, hi) if n % 2 == 0 else (-hi, -lo)

def bias(ps):
    out = Fraction(1)
    for p in ps:
        out *= 1 - 2 * p
    return out

def sign_extremizer(n, lam, r):
    lam = Fraction(lam)
    if r == 0:
        return [lam / n] * n
    if r <= lam:
        return [Fraction(1)] * r + [(lam - r) / (n - r)] * (n - r)
    return [lam / r] * r + [Fraction(0)] * (n - r)

def base_endpoint_vectors(n, lam):
    lam = Fraction(lam)
    max_r = int(2 * lam)
    even = [r for r in range(max_r + 1) if r % 2 == 0]
    r_hi = max(even, key=lambda r: M(n, lam, r))
    hi_vec = sign_extremizer(n, lam, r_hi)
    if lam <= Fraction(1, 2):
        lo_vec = [lam] + [Fraction(0)] * (n - 1)
    else:
        odd = [r for r in range(1, max_r + 1, 2)]
        r_lo = max(odd, key=lambda r: M(n, lam, r))
        lo_vec = sign_extremizer(n, lam, r_lo)
    return lo_vec, hi_vec

def endpoint_vectors(n, lam):
    lam = Fraction(lam)
    if lam <= Fraction(n, 2):
        return base_endpoint_vectors(n, lam)
    qlo, qhi = base_endpoint_vectors(n, n - lam)
    plo = [1 - q for q in qlo]
    phi = [1 - q for q in qhi]
    if n % 2 == 0:
        return plo, phi
    return phi, plo

def run():
    grid_vectors = 0
    endpoint_cases = 0
    sign_cases = 0

    # Exhaustive rational grids: every grid vector must lie inside the theorem.
    for n in range(1, 7):
        for d in range(2, 7):
            vals = [Fraction(k, d) for k in range(d + 1)]
            for ps in product(vals, repeat=n):
                lam = sum(ps, Fraction(0))
                lo, hi = bias_bounds(n, lam)
                b = bias(ps)
                assert lo <= b <= hi
                grid_vectors += 1

    # Exact endpoint constructions for many rational means.
    for n in range(1, 11):
        for d in range(2, 13):
            for L in range(n * d + 1):
                lam = Fraction(L, d)
                lo, hi = bias_bounds(n, lam)
                vlo, vhi = endpoint_vectors(n, lam)
                assert sum(vlo, Fraction(0)) == lam
                assert sum(vhi, Fraction(0)) == lam
                assert all(Fraction(0) <= p <= Fraction(1) for p in vlo + vhi)
                assert bias(vlo) == lo
                assert bias(vhi) == hi
                endpoint_cases += 1

    # Every base sign-class formula has an explicit exact attaining vector.
    for n in range(1, 13):
        for d in range(2, 13):
            for L in range((n * d) // 2 + 1):
                lam = Fraction(L, d)
                for r in range(int(2 * lam) + 1):
                    vec = sign_extremizer(n, lam, r)
                    assert sum(vec, Fraction(0)) == lam
                    target = M(n, lam, r)
                    b = bias(vec)
                    if target != 0:
                        assert abs(b) == target
                        assert (b > 0) == (r % 2 == 0)
                    else:
                        assert b == 0
                    sign_cases += 1

    print(
        "VERIFY_OK "
        f"grid_vectors={grid_vectors} "
        f"endpoint_cases={endpoint_cases} "
        f"sign_cases={sign_cases}"
    )

if __name__ == "__main__":
    run()
