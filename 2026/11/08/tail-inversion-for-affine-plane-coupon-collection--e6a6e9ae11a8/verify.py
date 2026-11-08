"""Exact finite checks for the affine-plane coupon-collection tail theorem.

Only the Python standard library is required.  The infinite all-orders claim
is proved by incidence counting in RESULT.md; these are finite cross-checks.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial


def field_multiply(a, b, q):
    if q != 4:
        return (a * b) % q
    # GF(4) = F_2[z]/(z^2+z+1), with 2 representing z.
    product = 0
    for i in range(2):
        for j in range(2):
            if ((a >> i) & 1) and ((b >> j) & 1):
                product ^= 1 << (i + j)
    if product & 4:
        product ^= 7
    return product


def field_add(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def affine_lines(q):
    pts = [(x, y) for x in range(q) for y in range(q)]
    lines = []
    for a in range(q):
        lines.append(frozenset(i for i, (x, y) in enumerate(pts) if x == a))
    for slope in range(q):
        for shift in range(q):
            lines.append(frozenset(i for i, (x, y) in enumerate(pts)
                if y == field_add(field_multiply(slope, x, q), shift, q)))
    assert len(lines) == q * (q + 1)
    assert len(set(lines)) == len(lines)
    assert all(len(line) == q for line in lines)
    assert all(sum(i in line for line in lines) == q + 1 for i in range(q * q))
    assert all(sum(i in line and j in line for line in lines) == 1
               for i, j in combinations(range(q * q), 2))
    return lines


def signed_meeting_counts(lines, n):
    # Exhaust ALL point subsets, not a random sample or partial enumeration.
    masks = [sum(1 << i for i in line) for line in lines]
    counts = [0] * (len(lines) + 1)
    for subset in range(1, 1 << n):
        hits = sum(bool(subset & line) for line in masks)
        counts[hits] += 1 if subset.bit_count() % 2 else -1
    return counts


def tail_from_coefficients(counts, draws, t):
    assert t >= 1
    return sum(c * F(draws - hit, draws) ** t
               for hit, c in enumerate(counts) if c)


def full_tail(n, k, t):
    assert t >= 1
    return sum((-1) ** (s + 1) * comb(n, s) *
               F(comb(n - s, k), comb(n, k)) ** t
               for s in range(1, n + 1))


def dynamic_tail(blocks, n, steps):
    # Independent implementation: count sequences of sampled blocks by
    # forward dynamic programming on the union of all previously seen points.
    counts = {0: 1}
    full = (1 << n) - 1
    for _ in range(steps):
        updated = {}
        for state, ways in counts.items():
            for block in blocks:
                nxt = state | block
                updated[nxt] = updated.get(nxt, 0) + ways
        counts = updated
    return F(sum(v for state, v in counts.items() if state != full),
             len(blocks) ** steps)


def run():
    assertions = 0
    for q in (3, 4, 5):
        lines = affine_lines(q)
        assertions += 5
        n = q * q
        noncollinear = 0
        for triple in combinations(range(n), 3):
            misses = sum(all(i not in line for i in triple) for line in lines)
            collinear = any(all(i in line for i in triple) for line in lines)
            expected = q * q - 2 * q - 1 if collinear else q * (q - 2)
            assert misses == expected
            assertions += 1
            if not collinear:
                noncollinear += 1
        assert noncollinear == q ** 3 * (q - 1) ** 2 * (q + 1) // 6
        assertions += 1

    lines = affine_lines(3)
    coefficients = signed_meeting_counts(lines, 9)
    assert [(i, c) for i, c in enumerate(coefficients) if c] == [
        (4, 9), (7, -36), (9, 72), (10, -42), (11, -12), (12, 10)]
    assertions += 1
    ag_blocks = [sum(1 << i for i in line) for line in lines]
    full_blocks = [sum(1 << i for i in subset)
                   for subset in combinations(range(9), 3)]
    for t in range(1, 7):
        assert tail_from_coefficients(coefficients, 12, t) == dynamic_tail(ag_blocks, 9, t)
        assert full_tail(9, 3, t) == dynamic_tail(full_blocks, 9, t)
        assertions += 2
    assert tail_from_coefficients(coefficients, 12, 3) - full_tail(9, 3, 3) == -F(13, 1176)
    assert tail_from_coefficients(coefficients, 12, 4) - full_tail(9, 3, 4) == F(1, 336)
    assertions += 2
    mean_ag = sum(c * F(12, hit) for hit, c in enumerate(coefficients) if hit)
    mean_full = sum((-1) ** (s + 1) * comb(9, s) /
                    (1 - F(comb(9 - s, 3), comb(9, 3)))
                    for s in range(1, 10))
    assert mean_ag == F(3001, 385)
    assert mean_full == F(3352087, 429940)
    assert mean_ag - mean_full == -F(1239, 675620)
    assertions += 3
    for t in range(1, 31):
        difference = tail_from_coefficients(coefficients, 12, t) - full_tail(9, 3, t)
        scaled = difference * 4 ** t
        closed = (72 - 84 * F(20, 21) ** t - 42 * F(2, 3) ** t
                  + 126 * F(10, 21) ** t - 12 * F(1, 3) ** t
                  - 126 * F(4, 21) ** t + 84 * F(1, 21) ** t)
        assert scaled == closed
        assert difference == 0 if t <= 2 else difference < 0 if t == 3 else difference > 0
        assertions += 2
    for q in range(3, 13):
        n = q * q
        num = F(factorial(q), q ** q * (q + 1) ** (q - 1))
        den = F(1)
        for j in range(1, q):
            den *= F(comb(n - j * q, q), comb(n, q))
        assert num > den
        assert q * q > 2 * (q + 1)
        assertions += 2
    print(f"PASS: {assertions} independent finite assertions; affine q=3,4,5 triple checks, ")
    print("q=3 complete point-subset census and independent exact union-state DP; ")
    print("exact tail crossover and known expectation; early-cover tests q=3,...,12.")


if __name__ == "__main__":
    run()
