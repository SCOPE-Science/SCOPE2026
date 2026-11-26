"""Finite corroboration of an exact two-frequency cyclic sampling theorem.

Only Python 3 standard-library modules are used. This is not an all-orders proof.
"""
from itertools import combinations
from cmath import exp
from math import pi, cos, isclose


def expected_sets(n):
    if n % 2 == 0:
        return {
            tuple(sorted((a, (a+n//2) % n, b, (b+n//2) % n)))
            for a, b in combinations(range(n // 2), 2)
        }
    return {
        tuple(sorted(((a+t) % n for t in (0, 1, (n-1)//2, (n+3)//2))))
        for a in range(n)
    }


def main():
    tests = 0
    for n in range(4, 37):
        roots = [exp(2j*pi*k/n) for k in range(n)]
        target = 0.0 if n % 2 == 0 else 2*(cos(pi/n)-cos(2*pi/n))
        minimizers = set()
        best = 100.0
        for sites in combinations(range(n), 4):
            z = sum((roots[k] for k in sites), 0j)
            magnitude = abs(z)
            tests += 1
            if magnitude + 4e-9 < best:
                best, minimizers = magnitude, {sites}
            elif abs(magnitude - best) < 4e-9:
                minimizers.add(sites)
            det = 16 - magnitude*magnitude
            smallest = 4 - magnitude
            largest = 4 + magnitude
            inv_trace = 8/det
            assert det > 0 and smallest > 0
            assert isclose(smallest*largest, det, rel_tol=1e-12, abs_tol=1e-12)
            assert isclose((1/smallest+1/largest), inv_trace,
                           rel_tol=1e-12, abs_tol=1e-12)
            assert magnitude >= target - 4e-9
        predicted = expected_sets(n)
        assert minimizers == predicted, (n, minimizers ^ predicted)
        assert abs(best - target) < 4e-9, (n, best, target)
        expected_number = n if n % 2 else (n//2)*(n//2-1)//2
        assert len(minimizers) == expected_number
    print(f'CHECK_PASS orders=4..36 four_subsets={tests}')


if __name__ == '__main__':
    main()
