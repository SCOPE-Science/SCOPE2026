"""Exact reproduction of a three-marker Abelian-square Parikh-spectrum theorem.

Python 3 standard library only. Run: python3 reproduce.py
The infinite conclusion additionally uses the mathematical interval proof,
Dirichlet convergence, and Ehrhart's theorem described in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial


def interval(A, g, B):
    lo = (g + 3) // 2
    hi = min((A + B + g + 2) // 2, A + g + 1, B + g + 1)
    return set(range(lo, hi + 1))


def predicted(a, b, c, d):
    return max(a, b, c, d) // 2 + len(interval(a, b, c) | interval(b, c, d))


def direct(word):
    s = set()
    for r in range(1, len(word) // 2 + 1):
        for i in range(len(word) - 2 * r + 1):
            u = word[i:i + r]
            v = word[i + r:i + 2 * r]
            if u.count('1') == v.count('1'):
                s.add((r, u.count('1')))
    return len(s)


def test_all_words():
    tested = 0
    for n in range(3, 33):
        for i, j, k in combinations(range(n), 3):
            word = '0' * i + '1' + '0' * (j - i - 1) + '1' + '0' * (k - j - 1) + '1' + '0' * (n - k - 1)
            a, b, c, d = i, j - i - 1, k - j - 1, n - k - 1
            lhs = direct(word)
            rhs = predicted(a, b, c, d)
            assert lhs == rhs, (word, lhs, rhs)
            tested += 1
    assert tested == 40920
    print('DIRECT_HALF_PARIKH_OK', tested)

# Each constraint is v dot x <= bound, x=(a,b,c,r), d=1-a-b-c.
BASE = [((-1,0,0,0),0), ((0,-1,0,0),0), ((0,0,-1,0),0),
        ((1,1,1,0),1), ((0,0,0,-1),0)]
ONE = [((0,1,0,-2),0), ((-1,-1,-1,2),0),
       ((-1,-1,0,1),0), ((0,-1,-1,1),0)]
TWO = [((0,0,1,-2),0), ((1,0,0,2),1), ((0,-1,-1,1),0),
       ((1,1,0,1),1)]


def solve4(rows):
    matrix = [[F(t) for t in v] + [F(b)] for v, b in rows]
    for col in range(4):
        pivot = next((i for i in range(col, 4) if matrix[i][col]), None)
        if pivot is None:
            return None
        matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
        z = matrix[col][col]
        matrix[col] = [t / z for t in matrix[col]]
        for i in range(4):
            if i != col:
                z = matrix[i][col]
                matrix[i] = [u - z * v for u, v in zip(matrix[i], matrix[col])]
    return tuple(row[4] for row in matrix)


def vertices(inequalities):
    ans = set()
    for rows in combinations(inequalities, 4):
        v = solve4(rows)
        if v is not None and all(sum(F(t) * x for t, x in zip(a, v)) <= b for a, b in inequalities):
            ans.add(v)
    return ans


def lattice_count(N, intersection=False):
    total = 0
    for a in range(N + 1):
        for b in range(N - a + 1):
            for c in range(N - a - b + 1):
                d = N - a - b - c
                lo = (b + 1) // 2
                hi = min((a + b + c) // 2, a + b, b + c)
                if intersection:
                    lo = max(lo, (c + 1) // 2)
                    hi = min(hi, (b + c + d) // 2, c + d)
                total += max(0, hi - lo + 1)
    return total


def ehrhart_volume(inequalities, intersection, vertex_count, expected_counts, expected_volume):
    vs = vertices(inequalities)
    assert len(vs) == vertex_count
    assert all(12 % x.denominator == 0 for v in vs for x in v)
    # 12 times every vertex is integral, so L_P(12k) is a degree-four
    # Ehrhart polynomial in k. Fourth difference gives leading coefficient.
    counts = [lattice_count(12 * k, intersection) for k in range(5)]
    assert counts == expected_counts, counts
    fourth = sum((-1)**(4-k) * comb(4,k) * counts[k] for k in range(5))
    volume = F(fourth, factorial(4) * 12**4)
    assert volume == expected_volume, (volume, expected_volume)
    return volume, fourth


def test_volume():
    v1, d1 = ehrhart_volume(BASE + ONE, False, 7,
        [1,1225,14365,65341,195625], F(1,32))
    v12, d12 = ehrhart_volume(BASE + ONE + TWO, True, 10,
        [1,593,6923,31471,94205], F(13,864))
    # Expected largest of four uniform-simplex coordinates is H_4 / 4.
    harmonic = sum((F(1,j) for j in range(1,5)), F(0))
    E = harmonic / 8 + 6 * (2 * v1 - v12)
    assert E == F(157,288), E
    print('EHRHART_VERTEX_VOLUME_OK', len(vertices(BASE + ONE)),len(vertices(BASE + ONE + TWO)), d1,d12)
    print('DIRICHLET_EXPECTATION_OK', E)

if __name__ == '__main__':
    test_all_words()
    test_volume()
    print('ALL_CHECKS_PASSED')
