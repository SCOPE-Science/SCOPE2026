"""Reproduce the Euclidean permutahedron/multipermutahedron projection results.

Requires Python 3.10+. Optional independent numerical check needs NumPy and SciPy.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial, sqrt
from random import Random


def exact_projection(n, k):
    assert n >= 3 and 1 <= k < n
    x = tuple(Q(i) for i in range(1, n + 1))
    lower = Q(k + 1, 2)
    upper = Q(n + k + 1, 2)
    mass = sum(x)
    def clip(t):
        return min(upper, max(lower, t))
    breaks = sorted(set([lower - t for t in x] + [upper - t for t in x]))
    shift = None
    for a, b in zip(breaks, breaks[1:]):
        va = sum(clip(t + a) for t in x)
        vb = sum(clip(t + b) for t in x)
        if va <= mass <= vb and va < vb:
            shift = a + (mass - va) * (b - a) / (vb - va)
            break
    assert shift is not None
    y = tuple(clip(t + shift) for t in x)
    residual = tuple(t - yi for t, yi in zip(x, y))
    assert sum(y) == mass
    assert all(lower <= yi <= upper for yi in y)
    assert all(residual[i] <= residual[i + 1] for i in range(n-1))
    r = sum(t + shift < lower for t in x)
    s = sum(t + shift > upper for t in x)
    m = n-r-s
    assert m > 0
    assert residual[r:n-s] == (-shift,) * m
    return shift, sum(t * t for t in residual), r, s, y, residual


def check_exact():
    cases = 0
    for n in range(3, 26):
        for k in range(1, n):
            lam, d2, r, s, y, residual = exact_projection(n, k)
            lower, upper = Q(k + 1, 2), Q(n + k + 1, 2)
            assert d2 == sum((Q(i)-yi)**2 for i, yi in enumerate(y, 1))
            assert d2 == exact_projection(n, n-k)[1]
            for i in range(n):
                for j in range(i+1,n):
                    assert residual[i] <= residual[j]
            # Q is the convex hull of k lower and n-k upper entries.
            # The Euclidean projection certificate is a linear normal inequality.
            test = [lower] * k + [upper] * (n-k)
            rng = Random(100000 + 29*n + k)
            for _ in range(30):
                rng.shuffle(test)
                assert sum(residual[i] * (test[i]-y[i]) for i in range(n)) <= 0
            cases += 1
    return cases


def check_farthest_faces():
    # Enumerate every vertex and its residual, then group equal residuals.
    total = 0
    for n in range(3, 8):
        for k in range(1, n):
            _, _, r, s, y, q = exact_projection(n, k)
            groups = {}
            for z in permutations(range(1,n+1)):
                # Coordinates from x are carried under the same permutation.
                res = tuple(q[t-1] for t in z)
                groups[res] = groups.get(res, 0) + 1
            m = n-r-s
            assert len(groups) == factorial(n)//factorial(m), (n,k,m,len(groups))
            assert set(groups.values()) == {factorial(m)}
            total += 1
    return total


def check_asymptotic():
    errors = []
    for n in (200, 400, 800):
        for alpha in (0.10, 0.20, 0.25, 0.30, 0.40, 0.50):
            k = round(alpha*n)
            d2 = float(exact_projection(n,k)[1]) / n**3
            beta = min(alpha, 1-alpha)
            if beta <= .25:
                formula = (1-sqrt(beta))**3 * (1+3*sqrt(beta))/12
            else:
                formula = 7/96-beta*(1-beta)/4
            errors.append(abs(d2-formula))
            assert abs(d2-formula) < 2e-5
    return max(errors)


def check_independent_qp():
    import numpy as np
    from scipy.optimize import minimize
    num = 0
    err = 0.
    for n in range(3, 10):
        for k in range(1,n):
            _, d2, _, _, y, _ = exact_projection(n,k)
            lower, upper = float(Q(k+1,2)),float(Q(n+k+1,2))
            x = np.arange(1.,n+1.)
            objective = lambda z: np.dot(z-x,z-x)
            derivative = lambda z: 2*(z-x)
            result = minimize(objective,np.array([float(t) for t in y]),jac=derivative,
                  constraints=[{'type':'eq','fun':lambda z: sum(z)-n*(n+1)/2,'jac':lambda z: np.ones(n)}],
                  bounds=[(lower,upper)]*n,method='SLSQP',
                  options={'ftol':1e-13,'maxiter':500})
            # QP independently checks optimizer for the same fixed canonical vertex.
            assert result.success, (n,k,result.message)
            gap = abs(objective(result.x)-float(d2))
            err = max(err,gap)
            assert gap < 1e-8, (n,k,gap)
            num += 1
    return num,err


if __name__ == '__main__':
    a = check_exact()
    b = check_farthest_faces()
    c = check_asymptotic()
    d, err = check_independent_qp()
    print(f'PERM_MULTIPERM_PASS exact={a} face_enumeration={b} large_n_max_error={c:.3g} independent_qps={d} max_qp_gap={err:.3g}')
