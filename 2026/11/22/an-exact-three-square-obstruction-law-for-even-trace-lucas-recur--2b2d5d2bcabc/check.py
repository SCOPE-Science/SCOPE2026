"""Reproducible finite verification of an exact Lucas three-square index criterion.

Usage: python check.py
Only finite evidence; the all-index theorem requires the accompanying proof.
"""
from fractions import Fraction


def predicted(P, B, n):
    assert P > 0 and P % 2 == 0 and B > 0 and B % 2 == 1 and n > 0
    t = (P & -P).bit_length() - 1
    a = P >> t
    s = (n & -n).bit_length() - 1
    if s == 0:
        if t == 1:
            return ((B % 8 == 3 and n % 8 == 3)
                    or (B % 8 == 7 and n % 8 == 7))
        return B % 8 == 7 and n % 4 == 3
    if (t + s - 1) % 2:
        return False
    c = 1 if s == 1 else (B + (2 if t == 1 else 0))
    r = 7 * pow((a * c) % 8, -1, 8) % 8
    return (n >> s) % 8 == r


def predicted_density(P, B):
    t = (P & -P).bit_length() - 1
    if t == 1:
        return Fraction(1, 24) + (Fraction(1, 8) if B % 8 in (3, 7) else 0)
    if t % 2 == 0:
        return Fraction(1, 12) + (Fraction(1, 4) if B % 8 == 7 else 0)
    return Fraction(1, 24) + (Fraction(1, 4) if B % 8 == 7 else 0)


def from_actual_term(u):
    if u == 0:
        return False
    v = (u & -u).bit_length() - 1
    return (v % 2 == 0) and ((u >> v) % 8 == 7)


def verify():
    # Independent direct integer recurrence, deliberately not using a Lucas polynomial.
    direct = 0
    for P in (2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 28, 30, 48, 64):
        for B in (1, 3, 5, 7, 9, 11, 15, 21, 31):
            prev, curr = 0, 1
            for n in range(1, 181):
                prev, curr = curr, P * curr + B * prev
                assert predicted(P, B, n) == from_actual_term(prev), (P, B, n)
                direct += 1

    # Independent fixed-width residue recurrence, much broader parameter coverage.
    # All terms at tested indices have 2-adic valuation < 24.
    modular = 0
    modulus = 1 << 24
    for P in range(2, 130, 2):
        for B in range(1, 130, 2):
            prev, curr = 0, 1
            for n in range(1, 401):
                prev, curr = curr, (P * curr + B * prev) % modulus
                assert prev != 0, (P, B, n, "modulus insufficient")
                assert predicted(P, B, n) == from_actual_term(prev), (P, B, n)
                modular += 1

    # Every claimed density is realized among some parameters.
    classes = {predicted_density(P, B) for P in (2, 4, 6, 8, 12)
               for B in (1, 3, 5, 7)}
    expected = {Fraction(1, 24), Fraction(1, 12), Fraction(1, 6),
                Fraction(7, 24), Fraction(1, 3)}
    assert classes == expected, classes
    # Independent dyadic-prefix counts for every density phase.
    census = []
    N = 1 << 14
    for P, B in ((2, 1), (2, 3), (4, 1), (4, 7), (8, 7)):
        prev, curr = 0, 1
        count = 0
        for n in range(1, N + 1):
            prev, curr = curr, (P * curr + B * prev) % modulus
            assert prev != 0
            count += from_actual_term(prev)
        density = predicted_density(P, B)
        assert abs(Fraction(count) - N * density) <= 20, (P, B, count, density)
        census.append((P, B, count, str(density)))
    print(f"PASS: {direct} exact-integer + {modular} modular index checks")
    print("PASS: five independent dyadic-prefix obstruction counts:", census)
    print("PASS: all five densities:", ', '.join(map(str, sorted(classes))))


if __name__ == '__main__':
    verify()
