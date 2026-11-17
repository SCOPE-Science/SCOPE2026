"""Exact rational checks for Gini and oscillation operator coefficients.

Requires Python 3 standard library only. The input is a square matrix with
constant row sums. Cuts suffice for the Gini seminorm by layer cake.
"""
from fractions import Fraction as Q
from itertools import combinations


def gini(x):
    n = len(x)
    return sum(abs(x[i] - x[j]) for i in range(n) for j in range(i + 1, n))


def oscillation(x):
    return max(x) - min(x)


def gini_operator_norm(a):
    n = len(a)
    assert len(a) == n and all(len(row) == n for row in a)
    assert len({sum(row) for row in a}) == 1
    return max(
        gini([sum(a[i][j] for j in cut) for i in range(n)]) / Q(k * (n-k))
        for k in range(1, n)
        for cut in combinations(range(n), k)
    )


def dobrushin(a):
    n = len(a)
    return max(
        sum(abs(a[i][j] - a[t][j]) for j in range(n)) / Q(2)
        for i in range(n) for t in range(i + 1, n)
    )


def rankone(n, direction):
    k = n // 2
    ell = n - k
    if direction == 'gini_over_dobrushin':
        u = [Q(ell, n)] * k + [-Q(k, n)] * ell
        v = [Q(1), Q(-1)] + [Q(0)] * (n-2)
    elif direction == 'dobrushin_over_gini':
        u = [Q(1) - Q(1, n)] + [-Q(1, n)] * (n-1)
        v = [Q(1, k)] * k + [-Q(1, ell)] * ell
    else:
        raise ValueError(direction)
    eps = Q(1, 4*n)
    p = [[Q(1, n) + eps*u[i]*v[j] for j in range(n)] for i in range(n)]
    assert all(sum(row) == 1 for row in p)
    assert all(sum(p[i][j] for i in range(n)) == 1 for j in range(n))
    assert min(min(row) for row in p) > 0
    return p


def validate_rankone():
    cases = 0
    for n in range(2, 12):
        c = Q((n*n)//4, n-1)
        eps = Q(1, 4*n)
        a = rankone(n, 'gini_over_dobrushin')
        b = rankone(n, 'dobrushin_over_gini')
        assert dobrushin(a) == dobrushin(b) == eps
        assert gini_operator_norm(a) == eps * c
        assert gini_operator_norm(b) == eps / c
        cases += 2
    print('EXACT_POSITIVE_BISTOCHASTIC_TWO_SIDED_SHARPNESS_PASSED', cases)


def validate_symmetry_examples():
    bplus = [[2,-1,-1,0],[-1,1,0,0],[-1,0,1,0],[0,0,0,0]]
    bminus = [[1,0,0,-1],[0,1,-1,0],[0,-1,2,-1],[-1,0,-1,2]]
    for b, g, d in [(bplus, Q(10,3), Q(3)), (bminus, Q(7,2), Q(4))]:
        assert gini_operator_norm([[Q(x) for x in row] for row in b]) == g
        assert dobrushin([[Q(x) for x in row] for row in b]) == d
        assert all(sum(row) == 0 for row in b)
        eps = Q(1,32)
        p = [[Q(1,4)+eps*b[i][j] for j in range(4)] for i in range(4)]
        assert all(p[i][j] == p[j][i] for i in range(4) for j in range(4))
        assert all(sum(row) == 1 for row in p)
        assert min(min(row) for row in p)>0
        assert gini_operator_norm(p)==eps*g
        assert dobrushin(p)==eps*d
    print('EXACT_SYMMETRIC_POSITIVE_SEMIDEFINITE_EXAMPLES_PASSED', 2)


def validate_norm_geometry():
    cases=0
    for n in range(2, 10):
        K=(n*n)//4
        # The Gini/oscillation bounds are attained by singleton and half-size cuts.
        for k in range(1, n):
            z=[1]*k+[0]*(n-k)
            assert gini(z)==k*(n-k)
            assert Q(n-1)<=Q(gini(z),oscillation(z))<=K
            cases+=1
        assert gini([1]+[0]*(n-1))==n-1
        assert gini([1]*(n//2)+[0]*(n-n//2))==K
    print('EXACT_GINI_OSCILLATION_EXTREME_CUTS_PASSED', cases)

if __name__ == '__main__':
    validate_norm_geometry()
    validate_rankone()
    validate_symmetry_examples()
    print('ALL_GINI_DOBRUSHIN_COMPARISON_CHECKS_PASSED')
