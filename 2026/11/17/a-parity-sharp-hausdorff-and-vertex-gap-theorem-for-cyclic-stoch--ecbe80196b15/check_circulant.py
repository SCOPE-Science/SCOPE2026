"""Exact cyclic-displacement enumeration and independent constrained least-squares checks.

Run with: python check_circulant.py
Requires Python 3; scipy and numpy optional for the independent numerical checks.
"""
from collections import Counter
from itertools import permutations


def displacement_counts(perm):
    n = len(perm)
    v = [0] * n
    for i, j in enumerate(perm):
        v[(j-i) % n] += 1
    return v


def odd_example(n):
    return [(2*i) % n for i in range(n)]


def even_example(n):
    m = n // 2
    return [2*i for i in range(m)] + [2*(i-m)+1 for i in range(m, n)]


def expected_low_levels(n):
    if n == 2:
        return [4]
    if n == 3:
        return [3, 9]
    return [n + (0 if n % 2 else 2), n + 4]


def exact_enumeration():
    counts = {}
    for n in range(2, 9):
        tab = Counter()
        max_histograms = set()
        for p in permutations(range(n)):
            d = displacement_counts(p)
            s = sum(x*x for x in d)
            tab[s] += 1
            if s == expected_low_levels(n)[0]:
                max_histograms.add(tuple(d))
                if n % 2:
                    assert sorted(d) == [1]*n
                elif n >= 4:
                    assert sorted(d) == [0] + [1]*(n-2) + [2]
                    aa = d.index(2)
                    bb = d.index(0)
                    assert (aa-bb) % n == n//2
        assert sorted(tab)[:len(expected_low_levels(n))] == expected_low_levels(n), (n,tab)
        counts[n] = (sum(tab.values()), sorted(tab)[:3], tab[sorted(tab)[0]], len(max_histograms))
    return counts


def construction_checks():
    tests = 0
    for n in range(3, 1001):
        p = odd_example(n) if n % 2 else even_example(n)
        assert sorted(p) == list(range(n))
        d = displacement_counts(p)
        assert sum(x*x for x in d) == n+(0 if n % 2 else 2)
        if n >= 4:
            q = p.copy()
            if n == 4:
                q = [0,3,2,1]
            else:
                q[0], q[1] = q[1], q[0]
            assert sum(x*x for x in displacement_counts(q)) == n+4, (n,q)
        tests += 1
    return tests


def numeric_projection():
    try:
        import numpy as np
        from scipy.optimize import minimize
    except ImportError:
        return 'UNAVAILABLE (numpy/scipy missing)'
    rng = np.random.default_rng(233701)
    tests = 0
    err = 0.0
    for n in range(3, 9):
        shifts = []
        for s in range(n):
            A = np.zeros((n,n))
            A[np.arange(n), (np.arange(n)+s)%n] = 1
            shifts.append(A)
        for case in range(8):
            if case < 4:
                p = rng.permutation(n)
                X = np.zeros((n,n))
                X[np.arange(n),p] = 1
            else:
                X = np.zeros((n,n))
                for _ in range(7):
                    p = rng.permutation(n)
                    X[np.arange(n),p] += 1/7
            c = np.array([np.trace(X @ A.T)/n for A in shifts])
            assert np.all(c >= -1e-15) and abs(sum(c)-1) < 1e-12
            projection = sum(c[s]*shifts[s] for s in range(n))
            objective = lambda w: np.sum((X - sum(w[s]*shifts[s] for s in range(n)))**2)
            res = minimize(objective, np.ones(n)/n, method='SLSQP',
                           bounds=[(0,1)]*n, constraints={'type':'eq','fun':lambda w:sum(w)-1},
                           options={'ftol':1e-12, 'maxiter':200})
            assert res.success, (n,case,res.message)
            local_err = max(abs(objective(res.x)-np.sum((X-projection)**2)),
                            np.max(abs(res.x-c)))
            err=max(err,local_err)
            assert local_err < 5e-6, (n,case,local_err)
            tests += 1
    return (tests,err)


if __name__=='__main__':
    census=exact_enumeration()
    construct=construction_checks()
    numeric=numeric_projection()
    print('CIRCULANT_BIRKHOFF_PASS exact_orders=2..8 stats='+repr(census))
    print('CONSTRUCTIONS_3_TO_1000='+str(construct)+' independent_SLSQP='+repr(numeric))
