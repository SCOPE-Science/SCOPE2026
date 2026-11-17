"""Exact finite checks for the second Euclidean vertex-radius shell of cycle Lipschitz polytopes.

Run with Python 3: python artifacts/verify.py. Does not prove assertions for all orders.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations


def norm2_of_closed_steps(steps):
    n = len(steps)
    assert sum(steps) == 0
    height = 0
    values = []
    for d in steps:
        values.append(height)
        height += d
    assert height == 0
    return Fraction(n * sum(x*x for x in values) - sum(values)**2, n)


def theoretical(n):
    if n % 2 == 0:
        m = n // 2
        return (Fraction(m*(m*m+2),6),
                Fraction(2*(m-1)**2,m))
    m = (n-1)//2
    return (Fraction(m*(m+1)*(m*m+m+1),3*(2*m+1)),
            Fraction(2*m*(m-1),2*m+1))


def all_steps(n):
    zero_choices = (None,) if n%2 == 0 else range(n)
    for z in zero_choices:
        available = tuple(i for i in range(n) if i != z)
        for plus in combinations(available, len(available)//2):
            steps = [-1]*n
            if z is not None: steps[z] = 0
            for i in plus: steps[i] = 1
            yield steps


def check_gap_algebra():
    checked = 0
    for m in range(2,31):
        even_n = 2*m
        ev_best, _ = theoretical(even_n)
        for r in range(1,m):
            A = (set(range(m))-{m-r})|{m}
            steps = [1 if i in A else -1 for i in range(even_n)]
            expected = Fraction(2*(m-1)*r*(m-r),m)
            assert ev_best-norm2_of_closed_steps(steps) == expected
            checked += 1
        odd_n = 2*m+1
        od_best, _ = theoretical(odd_n)
        for h in range(1,m):
            plus = set(range(m+1))-{h}
            steps = [0 if i == h else 1 if i in plus else -1 for i in range(odd_n)]
            expected = Fraction(2*m*h*(m-h),odd_n)
            assert od_best-norm2_of_closed_steps(steps) == expected
            checked += 1
        for h in range(1,m+1):
            plus = set(range(1,m+2))-{h}
            steps = [0 if i == 0 else 1 if i in plus else -1 for i in range(odd_n)]
            expected = Fraction(2*(m+1-h)*(h*(2*m-1)-m),odd_n)
            assert od_best-norm2_of_closed_steps(steps) == expected
            checked += 1
    return checked


def main():
    total = 0
    for n in range(4,16):
        values = Counter(norm2_of_closed_steps(s) for s in all_steps(n))
        total += sum(values.values())
        ordered = sorted(values, reverse=True)
        maximum, gap = theoretical(n)
        assert len(ordered) >= 2
        assert ordered[0] == maximum
        assert ordered[0]-ordered[1] == gap
        if n%2 == 0:
            assert values[maximum] == n
            assert values[ordered[1]] == (2 if n==4 else 2*n)
        else:
            assert values[maximum] == 2*n
            assert values[ordered[1]] == (2*n if n==5 else 4*n)
    checked = check_gap_algebra()
    print(f'CYCLE_SECOND_RADIAL_SHELL_CHECKS_PASSED exhaustive_vertex_profiles={total} gap_formula_profiles={checked} orders=12')

if __name__ == '__main__':
    main()
