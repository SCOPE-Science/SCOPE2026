#!/usr/bin/env python3
"""Exact finite sanity checks for the genus-three Dickson-curve examples.

This is not a substitute for the stated proof for all prime powers and genera.
"""
from math import gcd


def dickson(n, x, p):
    if n == 0:
        return 2 % p
    a, b = 2 % p, x % p
    for _ in range(2, n + 1):
        a, b = b, (x * b - a) % p
    return b


def legendre(a, p):
    if a % p == 0:
        return 0
    v = pow(a % p, (p - 1) // 2, p)
    assert v in (1, p - 1)
    return 1 if v == 1 else -1


def permute(mask, perm):
    out = 0
    for i, j in enumerate(perm):
        if mask & (1 << i):
            out |= 1 << j
    return out


def fixed_two_torsion(g, full_branch):
    # Branch-set model: even subsets of 2g+2 points modulo complement.
    b = 2 * g + 2
    perm = list(range(b))
    if not full_branch:
        for j in range(g):
            u, v = 2 + 2 * j, 3 + 2 * j
            perm[u], perm[v] = perm[v], perm[u]
    full = (1 << b) - 1
    classes = set()
    for mask in range(1 << b):
        if mask.bit_count() % 2 == 0:
            classes.add(min(mask, mask ^ full))
    assert len(classes) == 2 ** (2 * g)
    fixed = sum(min(permute(mask, perm), permute(mask, perm) ^ full) == mask for mask in classes)
    return fixed


def valuation2(n):
    a = 0
    while n % 2 == 0:
        a += 1
        n //= 2
    return a


def run_case(p, n):
    assert (p, n) in ((41, 7), (83, 7), (167, 7), (223, 7),
                       (53, 9), (71, 9), (109, 11), (131, 11),
                       (103, 13), (181, 13))
    assert p > 3 and n > 5 and n % 2 and ((p + 1) // 2) % n == 0
    assert (2*n - 1) not in [p**k for k in range(1, 6)]
    assert (4*n - 1) not in [p**k for k in range(1, 6)]
    roots = [x for x in range(p) if dickson(n, x, p) == 0]
    assert len(set(roots)) == len(roots)
    assert dickson(n, -2, p) != 0
    rational_points = 2 + sum(1 + legendre((x + 2) * dickson(n, x, p), p) for x in range(p))
    assert rational_points == p + 1, (p, rational_points)
    g = (n - 1)//2
    full_branch = p % 4 == 3
    assert len(roots) == (n if full_branch else 1), (p, roots)
    if full_branch:
        assert all((-x) % p in roots for x in roots)
    else:
        assert roots == [0]
    fixed = fixed_two_torsion(g, full_branch)
    assert fixed == 2 ** (2*g if full_branch else g), (p, fixed)
    if full_branch:
        factors = [2] * g + [(p + 1)//2] * g
    else:
        factors = [p + 1] * g
    group_order = 1
    for x in factors:
        group_order *= x
    assert group_order == (p + 1)**g
    assert all(gcd(a, p) == 1 for a in factors)
    print(f"q={p} n={n} genus={g} roots={len(roots)} #C(F_q)={rational_points} "
          f"#J(F_q)={group_order} rational_J2={fixed} "
          f"v2(q+1)={valuation2(p+1)} factors={factors}")


def main():
    for p,n in ((41, 7), (83, 7), (167, 7), (223, 7),
                (53, 9), (71, 9), (109, 11), (131, 11),
                (103, 13), (181, 13)):
        run_case(p, n)
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
