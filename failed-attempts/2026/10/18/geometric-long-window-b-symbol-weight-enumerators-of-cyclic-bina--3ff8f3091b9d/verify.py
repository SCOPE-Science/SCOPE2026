"""Finite verification of long-window weight enumerators of binary Hamming codes.

Uses GF(2^m) parity-check syndromes in integer polynomial representation.
No external packages or files required. Run: python3 verify.py
"""
from collections import Counter


def powers_of_primitive(m, primitive_polynomial):
    n = (1 << m) - 1
    powers = []
    x = 1
    for _ in range(n):
        powers.append(x)
        x <<= 1
        if x & (1 << m):
            x ^= primitive_polynomial
    assert x == 1 and len(set(powers)) == n
    return powers


def prediction(m, b):
    n = (1 << m) - 1
    d = n - m
    t = n - b - m
    c = Counter({0: 1, n: (1 << d) - 1})
    if t > 0:
        c[n] -= n * (1 << (t - 1))
        for j in range(1, t + 1):
            coefficient = 1 if j == 1 else (1 << (j - 2))
            c[b + m + j - 1] += n * coefficient
    assert sum(c.values()) == 1 << d
    assert all(v > 0 for v in c.values())
    return c


def cyclic_weight(w, n, b):
    # Directly count nonzero cyclic windows (not the run-length formula).
    return sum(any(w & (1 << ((i + j) % n)) for j in range(b))
               for i in range(n))


def exhaustive_full(m, primitive_polynomial):
    columns = powers_of_primitive(m, primitive_polynomial)
    n = len(columns)
    lo = (n + 1) // 2
    observed = {b: Counter() for b in range(lo, n + 1)}
    for word in range(1 << n):
        syndrome = 0
        for i, column in enumerate(columns):
            if (word >> i) & 1:
                syndrome ^= column
        if syndrome:
            continue
        for b in observed:
            observed[b][cyclic_weight(word, n, b)] += 1
    for b, hist in observed.items():
        assert hist == prediction(m, b), (m, b, hist, prediction(m, b))
    print(f"FULL_OK m={m} length={n} words={1 << (n-m)} windows={len(observed)}")


def exhaustive_short_support(m, primitive_polynomial):
    # Does not enumerate all codewords. Independently exhausts support words
    # in an anchored arc of length at most floor(n/2), including all
    # nontrivial window weights in the theorem's range.
    columns = powers_of_primitive(m, primitive_polynomial)
    n = len(columns)
    max_length = (n - 1) // 2
    if max_length <= m:
        print(f"SHORT_OK m={m} trivial")
        return
    counts = Counter()
    for length in range(m + 1, max_length + 1):
        anchored = 0
        for interior in range(1 << (length - 2)):
            word = 1 | (interior << 1) | (1 << (length - 1))
            syndrome = 0
            for j in range(length):
                if (word >> j) & 1:
                    syndrome ^= columns[j]
            if syndrome:
                continue
            anchored += 1
            # Verify weight in actual length-n cyclic word, not inferred.
            for b in range((n + 1) // 2, n - length + 1):
                assert cyclic_weight(word, n, b) == b + length - 1
        expect = 1 if length == m + 1 else 1 << (length - m - 2)
        assert anchored == expect, (m, length, anchored, expect)
        counts[length] = anchored
    # Cyclic orbit uniqueness can be checked for m=5 by literal rotation.
    if m == 5:
        seen = set()
        for length in range(m + 1, max_length + 1):
            for interior in range(1 << (length - 2)):
                w = 1 | (interior << 1) | (1 << (length - 1))
                syndrome = 0
                for j in range(length):
                    if w >> j & 1:
                        syndrome ^= columns[j]
                if syndrome:
                    continue
                for offset in range(n):
                    rotated = ((w << offset) | (w >> (n - offset))) & ((1 << n) - 1)
                    assert rotated not in seen
                    seen.add(rotated)
        assert len(seen) == n * sum(counts.values())
    print(f"SHORT_OK m={m} length={n} anchored_length_counts={dict(sorted(counts.items()))} rotation_unique={m == 5}")


if __name__ == '__main__':
    exhaustive_full(3, 0b1011)
    exhaustive_full(4, 0b10011)
    exhaustive_short_support(4, 0b10011)
    exhaustive_short_support(5, 0b100101)
    print('VERIFY_OK cyclic_hamming_long_window')
