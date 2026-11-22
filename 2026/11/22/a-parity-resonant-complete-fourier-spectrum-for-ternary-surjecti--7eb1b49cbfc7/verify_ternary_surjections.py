"""Exact checks of ternary surjective-word Fourier convolution.

Run with: python3 verify_ternary_surjections.py
Standard library only. Finite checks support, rather than replace, the proof.
"""
from itertools import product
from math import comb


def predicted(n, freq):
    """Unnormalized coefficient as a rational integer."""
    if all(t == 0 for t in freq):
        return 3**n - 3 * 2**n + 3
    if sum(freq) % 3:
        return 0
    z = freq.count(0)
    return 3 * (1 - (-1)**(n-z) * 2**z)


def direct_pair(n, freq, surjections):
    """Represent a+b*omega using omega^2=-1-omega."""
    counts = [0, 0, 0]
    for word in surjections:
        counts[sum(a * b for a, b in zip(word, freq)) % 3] += 1
    return counts[0] - counts[2], counts[1] - counts[2]


def balanced_pm_count(r):
    assert r >= 1
    return (2**r + 2 * (-1)**r) // 3


def predicted_rank(n):
    return 3**(n-1) if n % 2 else 3**(n-1) - (2**n + 2) // 3


def checks():
    tested = 0
    for n in range(3, 8):
        surjections = [a for a in product(range(3), repeat=n)
                       if 0 in a and 1 in a and 2 in a]
        assert len(surjections) == 3**n - 3 * 2**n + 3
        nonzero = 0
        smallest = None
        levels = {}
        for freq in product(range(3), repeat=n):
            got = direct_pair(n, freq, surjections)
            want = predicted(n, freq)
            assert got == (want, 0), (n, freq, got, want)
            if want:
                nonzero += 1
                smallest = abs(want) if smallest is None else min(smallest, abs(want))
            if any(freq):
                z = freq.count(0)
                if sum(freq) % 3 == 0:
                    levels[z] = levels.get(z, 0) + 1
            tested += 1
        assert nonzero == predicted_rank(n), (n, nonzero)
        assert smallest == (3 if n % 2 else 9), (n, smallest)
        for z in range(n):
            r = n - z
            assert levels.get(z, 0) == comb(n, z) * balanced_pm_count(r)
    for n in range(3, 50):
        counts = [comb(n, z) * balanced_pm_count(n-z) for z in range(n)]
        assert sum(counts) + 1 == 3**(n-1)
        vanishing = counts[0] if n % 2 == 0 else 0
        assert 3**(n-1) - vanishing == predicted_rank(n)
    print(f"PASS: {tested} exact character coefficients; ranks, spectral minima, multiplicities and all-length identities tested.")


if __name__ == '__main__':
    checks()
