"""Exact and numerical consistency tests for cyclic sparse-relocation Fourier zeros.

Run with the Python standard library: python CHECK.py.
Finite tests supplement, but do not prove, the unrestricted theorem.
"""
from itertools import combinations, permutations
from collections import Counter
from math import gcd, pi, cos, sin
from random import Random


def cyclotomic_zero(sites, index, prime, exponent):
    """Independent exact root test by prime-power cyclotomic coefficient equality."""
    modulus = prime**exponent
    if index % modulus == 0:
        return False
    order = modulus // gcd(modulus, index)
    step = order // prime
    coeff = [0] * order
    for site in sites:
        coeff[site % order] += 1
    return all(len({coeff[z + step*t] for t in range(prime)}) == 1
               for z in range(step))


def common_depth(A, B, prime, b):
    answer = 0
    for depth in range(1, b+1):
        modulus = prime**depth
        if Counter(x % modulus for x in A) == Counter(x % modulus for x in B):
            answer = depth
        else:
            break
    return answer


def matching_depth(A, B, prime, b):
    def v_p(z):
        t = 0
        while z and z % prime == 0 and t < b:
            z //= prime
            t += 1
        return b if z == 0 else t
    return max(min(v_p(A[i] - B[perm[i]]) for i in range(len(A)))
               for perm in permutations(range(len(B))))


def run():
    rng = Random(73)
    assertions = 0
    cases = [
        (3, 2, 1, 1, 45), (3, 3, 1, 1, 45),
        (3, 3, 2, 1, 125), (3, 3, 2, 2, 130),
        (5, 2, 1, 1, 80), (5, 2, 1, 2, 90),
        (5, 3, 1, 1, 35), (5, 3, 1, 2, 35),
        (7, 2, 1, 1, 36), (7, 2, 1, 2, 36),
        (7, 2, 1, 3, 36),
    ]
    for prime, k, b, moves, repetitions in cases:
        n = prime**k
        shell = prime**b
        period = n // shell
        assert moves < prime and 2*moves < shell and period >= prime
        for repetition in range(repetitions):
            old = [v + shell * rng.randrange(period) for v in range(shell)]
            A = tuple(sorted(rng.sample(range(shell), moves)))
            B = tuple(sorted(rng.sample([v for v in range(shell) if v not in A], moves)))
            new = []
            for v in B:
                possible = [v + shell*t for t in range(period) if v + shell*t != old[v]]
                new.append(rng.choice(possible))
            sites = (set(old) - {old[v] for v in A}) | set(new)
            assert len(sites) == shell
            v = common_depth(A, B, prime, b)
            assert v == matching_depth(A, B, prime, b)
            assertions += 2
            predicted = {index for index in range(1, n)
                         if index % period == 0 and (index//period) % prime**(b-v) == 0}
            observed = {index for index in range(1, n)
                        if cyclotomic_zero(sites, index, prime, k)}
            assert predicted == observed, (prime, k, b, moves, A, B, v, observed, predicted)
            assert len(observed) == prime**v-1
            assertions += n+1
            if repetition % 6 == 0:
                for index in range(1, n):
                    real = sum(cos(2*pi*index*x/n) for x in sites)
                    imag = sum(sin(2*pi*index*x/n) for x in sites)
                    is_zero = (real*real + imag*imag) < 1e-14
                    assert is_zero == (index in observed), (n, index, real, imag)
                    assertions += 1
    # Show the restriction moves < prime matters: two full prime cycles can cancel
    # separately despite having different reduced residue distributions.
    p, k, b = 3, 3, 2
    shell, n = p**b, p**k
    A = set(range(0, shell, p))
    B = set(range(1, shell, p))
    old = set(range(shell))
    moved = (old - A) | {u+shell for u in B}
    assert len(A) == p and len(B) == p and len(moved) == shell
    assert common_depth(A, B, p, b) == 0
    assert cyclotomic_zero(moved, n//shell, p, k)
    assertions += 3
    print(f"CHECK_OK checks={assertions}")


if __name__ == "__main__":
    run()
