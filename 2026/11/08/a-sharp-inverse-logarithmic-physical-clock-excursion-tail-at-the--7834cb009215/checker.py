"""Exact finite checks supporting the Fibonacci-level excursion theorem.

Run: python3 checker.py
Only Python's standard library is needed. Finite checks are not a proof.
"""
from fractions import Fraction
from math import comb, sqrt, log


def first_passage_at(n):
    # A path that first hits zero at n cannot visit level greater than n.
    states = {1: Fraction(1)}
    landed = Fraction(0)
    for t in range(1, n + 1):
        new, landed = {}, Fraction(0)
        for x, prob in states.items():
            for y in range(max(0, x - 1), n + 1):
                k = y - x + 1
                if k < 0:
                    continue
                mass = prob / (2 ** (k + 1))
                if y == 0:
                    landed += mass
                else:
                    new[y] = new.get(y, Fraction(0)) + mass
        states = new
    return landed


def linear_solve(a, b):
    """Elementary exact Gaussian elimination, for a finite height cutoff."""
    n = len(b)
    rows = [list(a[i]) + [b[i]] for i in range(n)]
    for i in range(n):
        pivot = next(j for j in range(i, n) if rows[j][i])
        rows[i], rows[pivot] = rows[pivot], rows[i]
        s = rows[i][i]
        rows[i] = [v / s for v in rows[i]]
        for j in range(n):
            if j != i:
                v = rows[j][i]
                rows[j] = [rows[j][k] - v * rows[i][k] for k in range(n + 1)]
    return [row[-1] for row in rows]


def reach_height(h):
    # h is the absorbing upper barrier; overshoots count as successes.
    a = [[Fraction(int(x == y)) for y in range(1, h)]
         for x in range(1, h)]
    b = [Fraction(1, 2 ** (h - x + 1)) for x in range(1, h)]
    for x in range(1, h):
        for y in range(1, h):
            k = y - x + 1
            if k >= 0:
                a[x - 1][y - 1] -= Fraction(1, 2 ** (k + 1))
    return linear_solve(a, b)[0]


def main():
    count = 0
    for n in range(1, 19):
        actual = first_passage_at(n)
        catalan = Fraction(2 * comb(2 * n - 2, n - 1), n * 4 ** n)
        assert actual == catalan, (n, actual, catalan)
        count += 1
    for h in range(2, 16):
        actual = reach_height(h)
        assert actual == Fraction(1, h + 1), (h, actual)
        count += 1
    # Asymptotic comparison for the *exact* central-binomial tail.
    for n in [1000, 5000, 10000, 40000]:
        # Use a stable factorial-free recurrence for probability.
        p = 1.0
        for k in range(1, n + 1):
            p *= (2*k-1)/(2*k)
        assert abs((n**0.5)*p - 1/sqrt(3.141592653589793)) < 0.001
        count += 1
    # Fibonacci roof bounds on the induced levels j=4,...,50.
    seq = [1,2]
    for k in range(2,55):
        seq.append(seq[-1] + seq[-2])
    phi = (1+sqrt(5))/2
    for j in range(4,51):
        roof = seq[j-1]
        assert 0.4 * phi**j < roof < phi**j
        count += 1
    print(f'PASS: {count} supporting finite exact/numeric checks')


if __name__ == '__main__':
    main()
