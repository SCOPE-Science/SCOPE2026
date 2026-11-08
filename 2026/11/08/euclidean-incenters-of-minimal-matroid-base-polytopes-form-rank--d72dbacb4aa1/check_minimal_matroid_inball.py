"""Finite checks supporting the exact Euclidean inball classification.

Run: python check_minimal_matroid_inball.py
Dependencies: scipy>=1.9, numpy>=1.23. Finite checks do not prove the theorem.
"""
import math
import numpy as np
from scipy.optimize import linprog


def predicted(k, r):
    n = k + r
    h = math.sqrt((n - 1) / n)
    b = math.sqrt(k * r / n)
    M, m = max(k, r), min(k, r)
    rho = 1 / (M * h + b)
    lower = h * rho
    return rho, lower, b, M, m


def solve(k, r):
    n = k + r
    h = math.sqrt((n - 1) / n)
    b = math.sqrt(k * r / n)
    A, bb = [], []
    for i in range(n):
        row = np.zeros(n + 1)
        row[i] = -1
        row[-1] = h
        A.append(row)
        bb.append(0.)
    row = np.zeros(n + 1)
    row[:k] = 1
    row[-1] = b
    A.append(row)
    bb.append(1.)
    eq = np.zeros(n + 1)
    eq[:k] = 1
    eq[k:n] = -1
    c = np.zeros(n + 1)
    c[-1] = -1
    sol = linprog(c, A_ub=A, b_ub=bb,
                  A_eq=[eq], b_eq=[0],
                  bounds=[(None, None)] * n + [(0, None)],
                  method="highs")
    assert sol.success, (k, r, sol.message)
    return sol.x[-1], np.asarray(A), np.asarray(bb)


def test():
    tested = 0
    for k in range(2, 13):
        for r in range(2, 13):
            rho, lower, b, M, m = predicted(k, r)
            numerical, A, rhs = solve(k, r)
            assert abs(numerical - rho) < 1e-8, (k, r, numerical, rho)
            # Equality constraints of the analytic center family.
            for active in range(m):
                yz = np.full(k+r, lower)
                if k >= r:
                    assert k == M
                    yz[k+active] += (M-m) * lower
                else:
                    assert r == M
                    yz[active] += (M-m) * lower
                x = np.concatenate([yz, [rho]])
                assert abs(sum(yz[:k]) - sum(yz[k:])) < 1e-10
                assert max(A @ x - rhs) < 1e-9
                assert abs(sum(yz[:k]) + b*rho - 1.) < 1e-10
                # Every coordinate in the larger group is a contact facet.
                large = yz[:k] if k>=r else yz[k:]
                assert max(abs(large-lower))<1e-10
            tested+=1
    # Independent check that the symmetric center is in every center set.
    for k, r in [(3,3),(3,5),(4,7),(5,4),(9,9)]:
        rho, lower, b, M, m = predicted(k, r)
        s = M*lower
        yz = np.array([s/k]*k+[s/r]*r)
        z = np.concatenate([yz,[rho]])
        _, A, rhs = solve(k,r)
        assert max(A@z-rhs)<1e-9
    print(f"MINIMAL_MATROID_INBALL_FINITE_CHECKS_PASSED shapes={tested}")


if __name__ == '__main__':
    test()
