"""Standalone finite checks for additive energy of modular inverse graphs.

Usage: python3 verify_energy.py
Python standard library only; finite checks do not replace the proof.
"""
from collections import Counter
from math import gcd


def units(q):
    return [x for x in range(q) if gcd(x, q) == 1]


def direct_energy(q):
    U = units(q)
    inv = {x: pow(x, -1, q) for x in U}
    fibers = Counter(((x + y) % q, (inv[x] + inv[y]) % q)
                     for x in U for y in U)
    return sum(c * c for c in fibers.values())


def local_formula(p, k):
    return 3 * p ** (2 * k - 2) * (p - 1) * (k * (p - 1) - 1)


def product_formula(q):
    m = q
    product = 1
    p = 2
    while p * p <= m:
        if m % p == 0:
            k = 0
            while m % p == 0:
                m //= p
                k += 1
            product *= local_formula(p, k)
        p += 1
    if m > 1:
        product *= local_formula(m, 1)
    return product


def root_count(q, t):
    # Fix first index 1, second index t. Count all legal third indices.
    U = units(q)
    s = (1 + t) % q
    count = 0
    for z in U:
        w = (s - z) % q
        if gcd(w, q) == 1 and s * (z - 1) * (z - t) % q == 0:
            count += 1
    return count


def directly_enumerated_local_counts(p, k):
    q = p ** k
    return sum(root_count(q, t) for t in units(q))


def test():
    tested_local = 0
    tested_composite = 0
    tested_roots = 0
    for p in (3, 5, 7, 11, 13):
        for k in range(1, 6):
            q = p ** k
            if q > 650:
                continue
            actual = direct_energy(q)
            theoretical = local_formula(p, k)
            assert actual == theoretical, (p, k, actual, theoretical)
            reduced = directly_enumerated_local_counts(p, k)
            assert actual == len(units(q)) * reduced, (p, k, actual, reduced)
            tested_roots += len(units(q))
            tested_local += 1
    for q in (15, 21, 33, 35, 45, 55, 63, 65, 75, 77, 99, 105, 117, 135, 175, 189, 225, 315):
        actual = direct_energy(q)
        theoretical = product_formula(q)
        assert actual == theoretical, (q, actual, theoretical)
        tested_composite += 1
    print(f"VERIFY_OK local_moduli={tested_local} composite_moduli={tested_composite} fixed_first_root_cases={tested_roots}")


if __name__ == "__main__":
    test()
