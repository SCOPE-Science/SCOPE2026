#!/usr/bin/env python3
"""Exact finite checks for restricted binomial gcds. Not an infinite proof."""
from itertools import product
from math import gcd, factorial


def lucas_nonzero(n, k, p):
    while n or k:
        if k % p > n % p:
            return False
        n //= p
        k //= p
    return True


def token_weights(n, m, p):
    weights = []
    power = 1
    while n:
        digit = n % p
        weights.extend([power % m] * digit)
        power = power * p % m
        n //= p
    return weights


def minimal_zero_sum(weights, m):
    if not weights or sum(weights) % m:
        return False
    # If total sum vanishes, a proper zero-sum submultiset exists iff
    # there is one omitting an arbitrarily chosen last token (complements).
    residues = set()
    for v in weights[:-1]:
        residues |= {(r + v) % m for r in residues} | {v % m}
        if 0 in residues:
            return False
    return True


def gcd_positive_by_lucas(m, q, p):
    n = m * q
    return all(not lucas_nonzero(n, m * j, p) for j in range(1, q))


def multiplicative_order(p, m):
    x = p % m
    order = 1
    while x != 1:
        x = x * p % m
        order += 1
    return order


def exact_profile_count(m, p, L):
    h = multiplicative_order(p, m)
    positions = [len(range(r, L, h)) for r in range(h)]
    cells = [(r, d) for r in range(h) for d in range(1, p)]
    answer = 0

    def enumerate_profiles(i, remaining, counts, weights):
        nonlocal answer
        if i == len(cells):
            if not minimal_zero_sum(weights, m):
                return
            total = 1
            for r in range(h):
                E = sum(t for (rr, d), t in zip(cells, counts) if rr == r)
                if E > positions[r]:
                    return
                numerator = factorial(positions[r]) // factorial(positions[r] - E)
                denominator = 1
                for (rr, d), t in zip(cells, counts):
                    if rr == r:
                        denominator *= factorial(t)
                total *= numerator // denominator
            answer += total
            return
        r, d = cells[i]
        for count in range(remaining // d + 1):
            enumerate_profiles(i+1, remaining - d*count, counts+[count],
                               weights+[pow(p,r,m)]*(d*count))

    enumerate_profiles(0, m, [], [])
    return answer - int(p**L > m)


def multiplier_count_sparse(m, p, L):
    """Count q <= p**L, NOT the exact profile's mq < p**L cutoff."""
    bound = m * (p ** L)
    max_exp = 0
    # Correct significant-digit bound: largest possible N may need
    # more than L+2 base-p positions when m >= p**2.
    while p ** max_exp <= bound:
        max_exp += 1
    answer = 0

    def visit(i, remaining, n, weights):
        nonlocal answer
        if i == max_exp:
            if m < n <= bound and n % m == 0 and minimal_zero_sum(weights, m):
                answer += 1
            return
        base = p ** i
        for d in range(min(p-1, remaining) + 1):
            visit(i+1, remaining-d, n+d*base, weights + [base % m]*d)

    visit(0, m, 0, [])
    return answer


def branch0(L):
    return (L**5 + 40*L**4 + 560*L**3 - 640*L**2 + 6144*L - 30720)//30720


def branch2(L):
    return (L**5 + 40*L**4 + 600*L**3 - 640*L**2 + 12944*L - 59520)//30720


def main():
    checks = 0
    for m in range(2, 11):
        for p in (2, 3, 5, 7, 11):
            if gcd(m, p) != 1:
                continue
            for q in range(2, 351):
                n = m*q
                assert minimal_zero_sum(token_weights(n,m,p),m) == gcd_positive_by_lucas(m,q,p)
                checks += 1
    print('DIRECT_LUCAS_VS_MINIMAL_ZERO_SUM', checks)

    word_checks = 0
    for m in range(2,9):
        for w in product(range(1,m),repeat=m):
            if sum(w)%m:
                continue
            good = minimal_zero_sum(w,m)
            assert not good or (len(set(w))==1 and gcd(w[0],m)==1)
            assert not (len(set(w))==1 and gcd(w[0],m)==1) or good
            word_checks += 1
    print('MAXIMAL_LENGTH_CYCLIC_WORDS',word_checks)

    for m,p in [(3,2),(4,3),(5,2),(5,3),(7,2)]:
        for L in range(2,11):
            actual = sum(minimal_zero_sum(token_weights(m*q,m,p),m)
                         for q in range(2,(p**L-1)//m+1))
            assert actual == exact_profile_count(m,p,L),(m,p,L,actual)
        print('EXACT_PROFILE_REPLAY',m,p,'L=2..10')

    for L in range(4,25,4):
        assert exact_profile_count(5,2,L) == branch0(L)
    for L in range(6,27,4):
        assert exact_profile_count(5,2,L) == branch2(L)
    assert branch0(16) != branch2(16)
    print('ORDER_FOUR_BRANCH_POLYNOMIAL_CERTIFICATE_OK')

    for m,p,exponents in [(3,2,[8,10,12,14,16]),
                          (4,3,[6,8,10,12]),
                          (5,2,[8,12,16,20])]:
        for L in exponents:
            count = multiplier_count_sparse(m,p,L)
            print('MULTIPLIER_CUTOFF',m,p,L,count)
    print('VERIFY_OK finite_checks_only=True')

if __name__ == '__main__':
    main()
