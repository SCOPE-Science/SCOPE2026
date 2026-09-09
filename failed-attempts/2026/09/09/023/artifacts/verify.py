#!/usr/bin/env python3
"""Independent verifier for the 65-class distinct covering (min modulus 7, LCM 10080).

Checks:
 1. All 65 moduli are distinct, each >= 7, each divides 10080.
 2. Minimum modulus is exactly 7 and lcm of moduli is exactly 10080.
 3. Every residue mod 10080 is covered by at least one class.
 4. Exact reciprocal-sum certificates: top-13 sum = 1669/1680 <= 1 (so k<=13
    impossible for distinct moduli in D), top-14 sum = 115/112 > 1.
 5. Irredundancy report: which classes have a private residue (informational only).
Uses only the Python standard library. Exit 0 with VERIFY_OK iff checks 1-4 pass.
"""
from math import gcd
from fractions import Fraction

L0 = 10080
SYS = [
    (6, 7), (7, 8), (8, 9), (6, 10), (9, 12), (8, 14), (12, 15), (3, 16),
    (14, 18), (0, 20), (4, 21), (13, 24), (26, 28), (24, 30), (27, 32),
    (33, 35), (5, 36), (11, 40), (16, 42), (2, 45), (1, 48), (52, 56),
    (30, 60), (7, 63), (28, 70), (29, 72), (59, 80), (10, 84), (74, 90),
    (43, 96), (93, 105), (73, 112), (64, 120), (112, 126), (38, 140),
    (65, 144), (43, 160), (121, 168), (110, 180), (18, 210), (169, 224),
    (185, 240), (154, 252), (248, 280), (203, 288), (128, 315), (313, 336),
    (209, 360), (292, 420), (75, 480), (217, 504), (404, 560), (578, 630),
    (505, 672), (281, 720), (472, 840), (553, 1008), (532, 1260),
    (875, 1440), (124, 1680), (281, 2016), (2044, 2520), (2153, 3360),
    (5033, 5040), (7193, 10080),
]
D = sorted(d for d in range(7, L0 + 1) if L0 % d == 0)
assert len(D) == 66, f"expected 66 divisors >=7 of 10080, got {len(D)}"


def main():
    mods = [m for _, m in SYS]
    assert len(SYS) == 65, f"expected 65 classes, got {len(SYS)}"
    assert len(set(mods)) == len(mods), "moduli not distinct"
    assert all(m >= 7 for m in mods), "min modulus violated"
    assert all(L0 % m == 0 for m in mods), "some modulus does not divide 10080"
    assert min(mods) == 7, "minimum modulus is not exactly 7"
    L = 1
    for m in mods:
        L = L * m // gcd(L, m)
    assert L == 10080, f"lcm is {L}, not 10080"

    count = [0] * L0
    for a, m in SYS:
        for x in range(a % m, L0, m):
            count[x] += 1
    uncovered = [x for x in range(L0) if count[x] == 0]
    assert not uncovered, f"{len(uncovered)} residues uncovered, e.g. {uncovered[:10]}"

    s13 = sum(Fraction(1, d) for d in D[:13])
    s14 = sum(Fraction(1, d) for d in D[:14])
    assert s13 == Fraction(1669, 1680) and s13 <= 1, f"top-13 sum = {s13}"
    assert s14 == Fraction(115, 112) and s14 > 1, f"top-14 sum = {s14}"
    total = sum(Fraction(1, d) for d in D)
    assert total == Fraction(29, 20), f"total sum = {total}"

    n_essential = 0
    for a, m in SYS:
        if any(count[x] == 1 for x in range(a % m, L0, m)):
            n_essential += 1
    print(f"classes: {len(SYS)}, distinct moduli: yes, min: 7, lcm: 10080")
    print(f"covered: {L0}/{L0}")
    print(f"top-13 reciprocal sum: {s13} = {float(s13):.6f} <= 1  =>  k<=13 impossible")
    print(f"top-14 reciprocal sum: {s14} = {float(s14):.6f} > 1")
    print(f"total reciprocal sum over D: {total} = 1.45")
    print(f"classes with a private residue: {n_essential}/65 (informational)")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
