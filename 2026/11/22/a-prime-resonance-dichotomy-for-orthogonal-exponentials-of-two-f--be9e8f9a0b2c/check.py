"""Exact finite checks for the two-prime arithmetic-progression convolution theorem.

This script provides finite sanity checks only; the argument for all primes and
all coprime steps is in RESULT.md. Requires Python 3.10+; standard library only.
"""
from fractions import Fraction
from math import gcd, lcm
from itertools import combinations


def is_zero(t, p, q, a, b):
    z1, z2 = t * p * a, t * q * b
    return ((z1.denominator == 1 and z1.numerator % p != 0) or
            (z2.denominator == 1 and z2.numerator % q != 0))


def expected(p, q, a, b):
    return p*q if (b % p == 0 or a % q == 0) else q


def explicit_family(p, q, a, b):
    if b % p == 0:
        return [Fraction(i, p) + Fraction(j, q*b)
                for i in range(p) for j in range(q)]
    if a % q == 0:
        return [Fraction(i, q) + Fraction(j, p*a)
                for i in range(q) for j in range(p)]
    return [Fraction(j, q*b) for j in range(q)]


def graph_clique_number(adj):
    best = 0
    def visit(n, remain):
        nonlocal best
        best = max(best, n)
        if n + remain.bit_count() <= best:
            return
        while remain:
            bit = remain & -remain
            remain -= bit
            v = bit.bit_length() - 1
            visit(n + 1, remain & adj[v])
    visit(0, (1 << len(adj)) - 1)
    return best


def graph_clique_test(p, q, a, b):
    H = lcm(p*a, q*b)
    # Fourier-zero membership for t/H (modulo integers).
    Z = {t for t in range(1, H)
         if is_zero(Fraction(t, H), p, q, a, b)}
    adj = [0]*H
    for i in range(H):
        for j in range(i+1, H):
            if (j-i) in Z:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    return graph_clique_number(adj)


def run():
    witness_cases = graph_cases = 0
    for p in (2,3,5,7):
        for q in (3,5,7,11):
            if p >= q:
                continue
            for a in range(1,21):
                for b in range(1,21):
                    if gcd(a,b) != 1:
                        continue
                    W = explicit_family(p,q,a,b)
                    assert len(W) == expected(p,q,a,b)
                    assert len(set(W)) == len(W)
                    assert all(is_zero(x-y,p,q,a,b)
                               for x,y in combinations(W,2))
                    witness_cases += 1
    for p,q in ((2,3),(2,5),(3,5)):
        for a in range(1,9):
            for b in range(1,9):
                if gcd(a,b) != 1 or lcm(p*a,q*b) > 120:
                    continue
                assert graph_clique_test(p,q,a,b) == expected(p,q,a,b), (p,q,a,b)
                graph_cases += 1
    print(f"exact witness cases: {witness_cases}")
    print(f"complete finite residue-graph cases: {graph_cases}")
    print("PASS")

if __name__ == '__main__':
    run()
