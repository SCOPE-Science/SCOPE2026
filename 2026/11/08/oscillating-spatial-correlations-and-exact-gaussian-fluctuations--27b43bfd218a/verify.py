#!/usr/bin/env python3
"""Exact, reproducible finite-order enumeration of local trimer-covering laws.

No external dependencies. The exhaustive subset recurrence, independently
implemented permutation enumeration, and numerical diagnostics appear below.
"""
from fractions import Fraction
from math import factorial
from itertools import permutations
import random

P = Fraction(31, 630)
JOINT = {
    1: Fraction(1, 80),
    2: Fraction(127, 45360),
    3: Fraction(17, 30240),
    4: Fraction(29, 59400),
    5: Fraction(629, 151200),
    6: Fraction(583747, 194594400),
    7: P * P,
}
COV = {
    1: Fraction(16001, 1587600),
    2: Fraction(601, 1587600),
    3: Fraction(-5903, 3175200),
    4: Fraction(-16879, 8731800),
    5: Fraction(5521, 3175200),
    6: Fraction(788077, 1362160800),
}
VAR = Fraction(8819999, 136216080)
OFFSET = Fraction(-52387, 2702700)
count_checks = 0

def check(condition, description):
    global count_checks
    assert condition, description
    count_checks += 1

def local_order_count(distance):
    """Enumerate all local first-arrival permutations via order-ideal DP.

    dp[mask][(a,b)] is the INTEGER number of orderings of previously
    arrived centers yielding a accepted trimers covering 0, b covering d.
    A center is accepted iff one of its sites has not yet been attempted
    by any earlier center. Prior attempted centers suffice because each
    site's earliest attempt is necessarily accepted.
    """
    start = -4
    end = distance + 2
    centers = list(range(start, end + 1))
    n = len(centers)
    dp = [None] * (1 << n)
    dp[0] = {(0, 0): 1}
    for mask in range((1 << n) - 1):
        if dp[mask] is None:
            continue
        for pos, center in enumerate(centers):
            if mask & (1 << pos):
                continue
            newly_hits_empty_site = any(
                not any(
                    0 <= j - start < n and (mask >> (j - start)) & 1
                    for j in range(site - 2, site + 1)
                )
                for site in (center, center + 1, center + 2)
            )
            delta_a = int(newly_hits_empty_site and -2 <= center <= 0)
            delta_b = int(newly_hits_empty_site and distance - 2 <= center <= distance)
            nxt = mask | (1 << pos)
            if dp[nxt] is None:
                dp[nxt] = {}
            for (a, b), multiplicity in dp[mask].items():
                key = a + delta_a, b + delta_b
                dp[nxt][key] = dp[nxt].get(key, 0) + multiplicity
    final = dp[-1]
    check(sum(final.values()) == factorial(n), f'permutation count d={distance}')
    probabilities = {key: Fraction(val, factorial(n)) for key, val in final.items()}
    return probabilities

def brute_force_joint(distance):
    """Independent direct sequential-deposition simulation of every ordering."""
    centers = list(range(-4, distance + 3))
    successes = 0
    for order in permutations(centers):
        occupied = set()
        deposited = set()
        for center in order:
            sites = (center, center + 1, center + 2)
            if not all(site in occupied for site in sites):
                deposited.add(center)
                occupied.update(sites)
        a = sum(center in deposited for center in (-2, -1, 0))
        b = sum(center in deposited for center in (distance - 2, distance - 1, distance))
        successes += int(a == 3 and b == 3)
    return Fraction(successes, factorial(len(centers)))

def main():
    marginals = {0: Fraction(0), 1: Fraction(173, 315),
                 2: Fraction(253, 630), 3: P}
    total_cov = Fraction(0)
    for d in range(1, 8):
        probs = local_order_count(d)
        check(sum(probs.values()) == 1, f'normalization d={d}')
        for j in range(4):
            check(sum((v for (a, b), v in probs.items() if a == j), Fraction()) == marginals[j], f'first marginal d={d}, j={j}')
            check(sum((v for (a, b), v in probs.items() if b == j), Fraction()) == marginals[j], f'second marginal d={d}, j={j}')
        joint = probs.get((3, 3), Fraction(0))
        check(joint == JOINT[d], f'joint probability d={d}: {joint}')
        if d < 7:
            cov = joint - P * P
            check(cov == COV[d], f'covariance d={d}: {cov}')
            check((cov > 0) == (d in (1,2,5,6)), f'covariance sign d={d}')
            total_cov += cov
        else:
            check(joint == P * P, 'independence at lag seven')
    computed_var = P * (1-P) + 2 * total_cov
    check(computed_var == VAR and VAR > 0, f'CLT variance {computed_var}')
    check(-2 * sum((d * COV[d] for d in range(1, 7)), Fraction()) == OFFSET, 'finite size correction')
    for d in (1, 2):
        check(brute_force_joint(d) == JOINT[d], f'independent exhaustive sequence d={d}')
    print(f'PASS {count_checks} exact checks; p={P}; asymptotic_variance={VAR}; finite_size_offset={OFFSET}')
    for d in range(1,7):
        print(f'lag={d} joint={JOINT[d]} covariance={COV[d]}')

if __name__ == '__main__':
    main()
