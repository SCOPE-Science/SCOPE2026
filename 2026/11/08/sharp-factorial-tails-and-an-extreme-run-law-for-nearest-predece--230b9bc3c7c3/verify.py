"""Finite exact and simulation diagnostics for nearest-predecessor local runs.

Run with: python3 verify.py
Only the Python standard library is required.
"""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial
from random import Random


def poly_mul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_primitive(a):
    return [Fraction(0)] + [x / (i + 1) for i, x in enumerate(a)]


def integrate_unit(a):
    return sum((x / (i + 1) for i, x in enumerate(a)), Fraction(0))


def h_poly(m):
    # Expected inverse tie-count: E[1 / (1 + Binomial(m,t))].
    return [Fraction(comb(m, i) * (-1) ** i, i + 1) for i in range(m + 1)]


def probability(d, k):
    assert d >= 2 and k >= 1
    first = h_poly(d - 1)
    interior = h_poly(d - 2)
    s = [Fraction(0), Fraction(1)]  # S_1(t)=t
    for _ in range(1, k):
        s = poly_primitive(poly_mul(interior, s))
    return d * (d - 1) ** (k - 1) * integrate_unit(poly_mul(first, s))


def enumerate_probability(d, k):
    # Independent direct enumeration of arrival-time rankings on the full
    # radius-one neighborhood of a prescribed self-avoiding path.
    # A specified path can be chosen in d*(d-1)^(k-1) ways.
    next_id = k + 1
    neighborhoods = []
    for i in range(k):
        nbrs = [i + 1]
        if i > 0:
            nbrs.append(i - 1)
        additional = d - 1 if i == 0 else d - 2
        nbrs.extend(range(next_id, next_id + additional))
        next_id += additional
        neighborhoods.append(nbrs)
    total = Fraction(0)
    for ranks in permutations(range(next_id)):
        if any(ranks[i] <= ranks[i + 1] for i in range(k)):
            continue
        denominator = 1
        for i, nbrs in enumerate(neighborhoods):
            n_earlier = sum(ranks[j] < ranks[i] for j in nbrs)
            denominator *= n_earlier
        total += Fraction(1, denominator)
    return total * Fraction(d * (d - 1) ** (k - 1), factorial(next_id))


def sample_run(d, rng):
    # Direct nearest-earlier-neighbor choices until first nonlocal jump.
    clock = rng.random()
    count = 0
    while count < 100:
        neighbors = [rng.random() for _ in range(d if count == 0 else d - 1)]
        earlier = [u for u in neighbors if u < clock]
        if not earlier:
            return count
        clock = rng.choice(earlier)
        count += 1
    raise AssertionError("Unexpectedly long simulated run")


def main():
    cases = [(3, 1, Fraction(3, 4)),
             (3, 2, Fraction(31, 90)),
             (3, 3, Fraction(31, 252)),
             (4, 1, Fraction(4, 5)),
             (4, 2, Fraction(1471, 3360))]
    for d, k, expected in cases:
        via_polynomial = probability(d, k)
        via_rank_enumeration = enumerate_probability(d, k)
        assert via_polynomial == expected == via_rank_enumeration
        print(f"exact enumeration PASS: degree={d}, run>={k}, P={expected}")
    # All exact probabilities must be decreasing; first-step normalization.
    for d in range(2, 8):
        vals = [probability(d, k) for k in range(1, 12)]
        assert vals[0] == Fraction(d, d + 1)
        assert all(Fraction(0) < vals[i + 1] < vals[i] < 1 for i in range(10))
    print("monotonicity/normalization checks PASS: degrees 2..7, runs 1..11")
    d = 3
    harmonic = Fraction(3, 2)
    b = Fraction(3, 4)
    for k in (10, 20, 30):
        ratio = probability(d, k) / (b * harmonic ** k / factorial(k + 1))
        print(f"finite asymptotic diagnostic: degree={d}, k={k}, ratio={float(ratio):.12f}")
    rng = Random(20261101)
    n = 100000
    counts = [0] * 6
    for _ in range(n):
        length = sample_run(3, rng)
        for k in range(1, 6):
            if length >= k:
                counts[k] += 1
    for k in range(1, 6):
        observed = counts[k] / n
        expected = float(probability(3, k))
        assert abs(observed - expected) < 0.012
        print(f"simulation diagnostic: degree=3, run>={k}, exact={expected:.8f}, observed={observed:.8f}")
    print("ALL CHECKS PASSED")

if __name__ == "__main__":
    main()
