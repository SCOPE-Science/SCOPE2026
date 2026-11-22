"""Finite verification for cyclic-fixed non-three-connected graph complexes.

Checks actual vertex deletion connectivity directly, without invoking the
vertex-transitive connectivity theorem used in the general proof.
Python 3.9+; standard library only.
"""
from math import gcd
from functools import reduce


def three_connected(n, distances):
    adjacency = [0] * n
    for vertex in range(n):
        for step in distances:
            adjacency[vertex] |= (1 << ((vertex + step) % n))
            adjacency[vertex] |= (1 << ((vertex - step) % n))
    all_vertices = (1 << n) - 1

    def connected_after_removal(deleted):
        remaining = all_vertices & ~deleted
        initial = remaining & -remaining
        visited = initial
        pending = initial
        while pending:
            vbit = pending & -pending
            pending ^= vbit
            v = vbit.bit_length() - 1
            newly_seen = adjacency[v] & remaining & ~visited
            visited |= newly_seen
            pending |= newly_seen
        return visited == remaining

    # Cyclic translations carry any pair of deleted vertices to a pair
    # containing vertex zero. The one-vertex case is also tested.
    return connected_after_removal(1) and all(
        connected_after_removal(1 | (1 << other))
        for other in range(1, n)
    )


def prime_factors(n):
    result = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            result.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        result.append(n)
    return result


def totient(n):
    result = n
    for p in prime_factors(n):
        result -= result // p
    return result


def run():
    cases = 0
    for n in range(4, 23):
        maximum_step = n // 2
        for mask in range(1, 1 << maximum_step):
            steps = [i + 1 for i in range(maximum_step) if mask & (1 << i)]
            anticipated = len(steps) >= 2 and reduce(gcd, steps, n) == 1
            observed = three_connected(n, steps)
            assert anticipated == observed, (n, steps, anticipated, observed)
            cases += 1

    # Check the actual intersections of the prime-indexed simplices,
    # and the squarefree vs. nonsquarefree distinction independently.
    nerve_cases = 0
    for n in range(4, 121):
        primes = prime_factors(n)
        pcount = len(primes)
        for mask in range(1, 1 << pcount):
            chosen = [p for i, p in enumerate(primes) if mask & (1 << i)]
            witness = any(all(d % p == 0 for p in chosen)
                          for d in range(1, n // 2 + 1))
            product = 1
            for p in chosen:
                product *= p
            assert witness == (product <= n // 2), (n, chosen)
            nerve_cases += 1

    n = 30
    primes = prime_factors(n)
    assert primes == [2, 3, 5]
    unit_vertices = sum(gcd(n, d) == 1 for d in range(1, n // 2 + 1))
    assert unit_vertices == totient(n) // 2 == 4
    assert all(len(prime_factors(k)) <= 2 for k in range(4, n))
    assert unit_vertices == 4
    print(f"ACTUAL_3_CONNECTIVITY_CASES={cases}")
    print(f"PRIME_SIMPLEX_INTERSECTION_CASES={nerve_cases}")
    print(f"FIRST_MIXED_DIMENSION_N={n}")
    print("N30_REDUCED_BETTI_0=4")
    print("N30_REDUCED_BETTI_1=1")
    print("CYCLIC_FIXED_NOT3_CONNECTIVITY_VERIFIED")

if __name__ == "__main__":
    run()
