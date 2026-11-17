"""Numerical cross-check for the square-pentagon four-simplex spectrum.
All mathematical implications are proved in RESULT.md; this file checks finite identities.
Run: python3 verify.py
"""
import itertools
import math
from collections import Counter

S = math.sin(2 * math.pi / 5)
T = math.sin(math.pi / 5)
BULK = 5 * S / 6
VERTICES = [
    (math.cos(j * math.pi / 2), math.sin(j * math.pi / 2), 0., 0.)
    for j in range(4)
] + [
    (0., 0., math.cos(2 * math.pi * k / 5), math.sin(2 * math.pi * k / 5))
    for k in range(5)
]


def det4(m):
    ans = 0.
    for p in itertools.permutations(range(4)):
        crossings = sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
        ans += (-1 if crossings % 2 else 1) * math.prod(m[i][p[i]] for i in range(4))
    return ans


def volume5(indices):
    base = VERTICES[indices[0]]
    edges = [[VERTICES[i][j] - base[j] for j in range(4)] for i in indices[1:]]
    return abs(det4(edges)) / math.factorial(4)


def main():
    predicted = [0., T / 12, (2 * S - T) / 24, S / 12, (S + 2 * T) / 24]
    expected_counts = [46, 20, 20, 20, 20]
    observed = Counter()
    maximizing_sets = []
    for combination in itertools.combinations(range(9), 5):
        value = volume5(combination)
        matches = [i for i, target in enumerate(predicted) if abs(value - target) < 3e-12]
        assert len(matches) == 1, (combination, value, matches)
        typ = matches[0]
        observed[typ] += 1
        if typ == 4:
            maximizing_sets.append(combination)
            assert sum(i < 4 for i in combination) == 2
            square = sorted(i for i in combination if i < 4)
            assert ((square[1] - square[0]) % 4) in (1, 3) or square == [0, 3]
    assert sum(observed.values()) == math.comb(9, 5) == 126
    assert [observed[k] for k in range(5)] == expected_counts
    assert len(maximizing_sets) == 20
    assert abs(BULK - 5/24 * math.sqrt(10+2*math.sqrt(5))) < 3e-14
    predicted_ratios = [0, (math.sqrt(5)-1)/20, (5-math.sqrt(5))/40, 1/10, math.sqrt(5)/20]
    for p, q in zip(predicted, predicted_ratios):
        assert abs(p/BULK-q) < 3e-14
    print('PASS: 126 determinants, multiplicities', [observed[k] for k in range(5)])
    print('PASS: five exact ratios and 20 vertex-supported maximizing simplices')
    print('Sharp fraction:', predicted_ratios[-1])


if __name__ == '__main__':
    main()
