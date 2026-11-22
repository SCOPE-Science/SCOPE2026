"""Independent finite checks for a weight-three cyclic deletion-shadow spectrum.
Run with Python 3: python verify.py. No external packages are required.
"""
from collections import Counter
from itertools import combinations
from math import comb


def canonical(s):
    return min(s[j:] + s[:j] for j in range(len(s))) if s else ""


def shadow(s):
    return {canonical(s[:j] + s[j + 1:]) for j in range(len(s))}


def from_gaps(a, b, c):
    return "1" + "0" * a + "1" + "0" * b + "1" + "0" * c


def gap_prediction(a, b, c):
    gaps = (a, b, c)
    N = sum(gaps)
    if N == 0:
        return 1
    zero_run_choices = sum(g > 0 for g in gaps)
    if a == b == c and a > 0:
        zero_run_choices -= 2
    elif len(set(gaps)) == 2 and gaps.count(max(gaps)) == 2 and max(gaps) - min(gaps) == 1:
        zero_run_choices -= 1
    one_choices = len({min(g, N - g) for g in gaps})
    return zero_run_choices + one_choices


def expected_spectrum(n):
    N = n - 3
    if N < 0:
        return Counter()
    d = Counter()
    if N == 0:
        d[1] += 1
    if N >= 1:
        d[2] += 1
    if N >= 3 and N % 3 == 0:
        d[2] += 1
    if N == 2:
        d[3] += 1
    if N >= 2:
        d[4] += N - 1 - (1 if N == 2 else 0)
    if N >= 5 and N % 3 == 2:
        d[4] += 1
    doubled = 0
    exceptional = 0
    for a in range(1, N + 1):
        b = N - 2 * a
        if b >= 1 and b != a:
            doubled += 1
            exceptional += int(b == a - 1)
    d[5] += doubled - exceptional
    all_positive_ordered = comb(N - 1, 2) if N >= 3 else 0
    all_equal = int(N >= 3 and N % 3 == 0)
    d[6] += (all_positive_ordered - all_equal - 3 * doubled) // 3
    return Counter({x: y for x, y in d.items() if y})


def brute_n(n):
    observed = Counter()
    reps = set()
    for ones in combinations(range(n), 3):
        s = "".join("1" if i in ones else "0" for i in range(n))
        reps.add(canonical(s))
    for s in reps:
        observed[len(shadow(s))] += 1
    return observed


# Compare two different encodings: direct bit-position deletion and cyclic gap vectors.
checked_gap_orbits = 0
for N in range(0, 25):
    reps = set()
    for a in range(N + 1):
        for b in range(N - a + 1):
            c = N - a - b
            reps.add(min((a, b, c), (b, c, a), (c, a, b)))
    for a, b, c in reps:
        checked_gap_orbits += 1
        actual = len(shadow(from_gaps(a, b, c)))
        assert actual == gap_prediction(a, b, c), (N, (a, b, c), actual)
    assert Counter(gap_prediction(*triple) for triple in reps) == expected_spectrum(N + 3)

checked_length = 0
for n in range(3, 19):
    assert brute_n(n) == expected_spectrum(n), (n, brute_n(n), expected_spectrum(n))
    checked_length += 1

# Exact algebraic coefficient comparisons for the six rational generating functions.
# A power series is represented by coefficient lists; these operations use integer arithmetic.
LIMIT = 58

def mul(a, b):
    c = [0] * LIMIT
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b[:LIMIT - i]):
                c[i + j] += x * y
    return c

def inv_of_one_minus(k):
    return [int(i % k == 0) for i in range(LIMIT)]

def shift(a, k):
    return [0] * k + a[:LIMIT - k]

def linear(*pairs):
    return [sum(mult * a[i] for mult, a in pairs) for i in range(LIMIT)]

v1 = inv_of_one_minus(1)
v2 = inv_of_one_minus(2)
v3 = inv_of_one_minus(3)
v1sq = mul(v1, v1)
v1cube = mul(v1sq, v1)
v12 = mul(v1, v2)
vals = {
    1: shift([1] + [0] * (LIMIT - 1), 3),
    2: linear((1, shift(v1, 4)), (1, shift(v3, 6))),
    3: shift([1] + [0] * (LIMIT - 1), 5),
    4: linear((1, shift(v1sq, 5)), (-1, shift([1] + [0] * (LIMIT - 1), 5)), (1, shift(v3, 8))),
    5: linear((1, shift(v12, 6)), (-1, shift(v3, 6)), (-1, shift(v3, 8))),
}
c6_num = linear((1, shift(v1cube, 6)), (-3, shift(v12, 6)), (2, shift(v3, 6)))
assert all(v % 3 == 0 for v in c6_num)
vals[6] = [v // 3 for v in c6_num]
for n in range(3, LIMIT):
    exp = expected_spectrum(n)
    for k in range(1, 7):
        assert vals[k][n] == exp.get(k, 0), (n, k, vals[k][n], exp.get(k, 0))

print(f"VERIFY_OK gap_orbits={checked_gap_orbits} direct_length=3..18 rational_coefficients=3..{LIMIT-1}")
