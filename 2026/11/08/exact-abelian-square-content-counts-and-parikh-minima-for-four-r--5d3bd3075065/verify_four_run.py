"""Standalone finite checks for a symbolic classification of Abelian squares.

Only Python standard library is required. The infinite theorem rests on
its separately stated proof, not on these finite computations.
"""
from itertools import product


def direct_factors(word):
    """Independently search every even-length factor by its half Parikh sums."""
    prefix = [0]
    for letter in word:
        prefix.append(prefix[-1] + (letter == "a"))
    result = set()
    for half in range(1, len(word) // 2 + 1):
        for start in range(len(word) - 2 * half + 1):
            midpoint = start + half
            end = midpoint + half
            if prefix[midpoint] - prefix[start] == prefix[end] - prefix[midpoint]:
                result.add(word[start:end])
    return result


def classified_factors(p, q, r, s):
    """Build exactly the six structurally allowed families of contents."""
    result = set()
    for t in range(1, max(p, r) // 2 + 1):
        result.add("a" * (2 * t))
    for t in range(1, max(q, s) // 2 + 1):
        result.add("b" * (2 * t))
    if q % 2 == 0:
        for t in range(1, min(p, r) + 1):
            result.add("a" * t + "b" * q + "a" * t)
    if r % 2 == 0:
        for t in range(1, min(q, s) + 1):
            result.add("b" * t + "a" * r + "b" * t)
    if r <= p:
        for j in range(1, min(q, s) + 1):
            if j % 2 == q % 2:
                result.add("a" * r + "b" * q + "a" * r + "b" * j)
    if q <= s:
        for i in range(1, min(p, r) + 1):
            if i % 2 == r % 2:
                result.add("a" * i + "b" * q + "a" * r + "b" * q)
    return result


def same_parity_count(bound, parity):
    return (bound // 2) if parity % 2 == 0 else ((bound + 1) // 2)


def closed_formula(p, q, r, s):
    result = max(p, r) // 2 + max(q, s) // 2
    if q % 2 == 0:
        result += min(p, r)
    if r % 2 == 0:
        result += min(q, s)
    if r <= p:
        result += same_parity_count(min(q, s), q)
    if q <= s:
        result += same_parity_count(min(p, r), r)
    if r <= p and q <= s:
        result -= 1
    return result


def baseline(t):
    return (t + 2) // 4


def check():
    tested = 0
    for p, q, r, s in product(range(1, 10), repeat=4):
        word = "a" * p + "b" * q + "a" * r + "b" * s
        observed = direct_factors(word)
        classified = classified_factors(p, q, r, s)
        theoretical = closed_formula(p, q, r, s)
        assert observed == classified, (p, q, r, s, observed ^ classified)
        assert len(observed) == theoretical, (p, q, r, s, len(observed), theoretical)
        tested += 1
    checked_pairs = 0
    for A in range(4, 23):
        for B in range(4, 23):
            minimum = min(closed_formula(p, q, A - p, B - q)
                          for p in range(1, A) for q in range(1, B))
            assert minimum == baseline(A) + baseline(B), (A, B, minimum)
            checked_pairs += 1
    assert closed_formula(1, 1, 1, 1) == 1
    assert baseline(2) + baseline(2) == 2
    print(f"PASS: {tested} exact content-set classifications (positive runs <=9)")
    print(f"PASS: {checked_pairs} Parikh-pair exhaustive minima (4 <= A,B <=22)")
    print("PASS: boundary case A=B=2 differs from extension of the minimum law")


if __name__ == "__main__":
    check()
