"""Independent active-pattern KKT checks for mass-weighted path-TV denoising.

Run: python check.py
Requires Python 3 and NumPy. This is a finite consistency test, not an
infinite-dimensional or all-data proof.
"""
from itertools import product
from fractions import Fraction as F
import numpy as np


def solve_path(y, masses, penalties, lam):
    n = len(y)
    if lam == 0:
        return np.asarray(y, dtype=float)
    y, masses, penalties = [np.asarray(v, dtype=float) for v in (y, masses, penalties)]
    for pattern in product((-1, 0, 1), repeat=n - 1):
        x = np.zeros(n)
        starts = [0] + [j + 1 for j, s in enumerate(pattern) if s != 0]
        ends = starts[1:] + [n]
        for left, right in zip(starts, ends):
            u_l = penalties[left - 1] * pattern[left - 1] if left else 0.0
            u_r = penalties[right - 1] * pattern[right - 1] if right < n else 0.0
            w = masses[left:right]
            x[left:right] = (np.dot(w, y[left:right]) + lam * (u_r - u_l)) / sum(w)
        gaps = np.diff(x)
        if any((sg == 1 and val <= 1e-9) or
               (sg == -1 and val >= -1e-9) or
               (sg == 0 and abs(val) > 1e-9)
               for sg, val in zip(pattern, gaps)):
            continue
        flux = np.cumsum(masses * (x - y))[:-1]
        if not all(abs(flux[j]) <= lam * penalties[j] + 1e-8 and
                   (pattern[j] == 0 or abs(flux[j] - lam*penalties[j]*pattern[j]) < 1e-8)
                   for j in range(n - 1)):
            continue
        return x
    raise AssertionError('No KKT pattern found')


def witness_exact(lam):
    if lam <= F(1, 6):
        return [1-lam, 5*lam, 100-4*lam]
    if lam <= F(1, 2):
        return [F(1, 2)+2*lam]*2+[100-4*lam]
    if lam <= F(100, 7):
        return [1+lam, 3*lam, 100-4*lam]
    if lam <= F(98, 3):
        return [1+lam, 50-lam/2, 50-lam/2]
    return [F(101, 3)]*3


def check_exact(lam):
    x = witness_exact(lam)
    y = [F(1), F(0), F(100)]
    a = [F(1), F(4)]
    u = [x[0]-y[0], x[0]+x[1]-y[0]-y[1]]
    for j in range(2):
        gap = x[j+1]-x[j]
        assert abs(u[j]) <= lam*a[j]
        if gap != 0:
            assert u[j] == (1 if gap > 0 else -1)*lam*a[j]


def run():
    exact_grid = [F(1, 12), F(1, 6), F(1, 4), F(1, 2), F(1), F(100, 7), F(20), F(98, 3), F(40)]
    for t in exact_grid:
        check_exact(t)
        numerical = solve_path([1., 0., 100.], [1., 1., 1.], [1., 4.], float(t))
        assert np.max(abs(numerical-np.array(witness_exact(t), dtype=float))) < 2e-8

    rng = np.random.default_rng(1729)
    tested = 0
    for n in (3, 4, 5, 6):
        for trial in range(12):
            masses = rng.uniform(.5, 2.0, size=n)
            t = np.concatenate([[0.], np.cumsum(masses)])
            a = t[1:-1]*(t[-1]-t[1:-1])
            # Strictly positive and concave in cumulative-mass coordinates.
            y = rng.normal(0, 4, size=n)
            xs = [solve_path(y, masses, a, lam) for lam in np.linspace(.001, 8., 24)]
            gaps = np.abs(np.diff(np.array(xs), axis=1))
            assert np.max(np.diff(gaps, axis=0)) < 3e-8
            tested += (len(xs)-1)*(n-1)

    # A weight profile with a nonconcave interior point, n=3.
    y = np.array([0., 1., 100.])
    a = np.array([1., 4.])
    x0 = solve_path(y, [1., 1., 1.], a, .001)
    x1 = solve_path(y, [1., 1., 1.], a, .01)
    assert abs(x1[1]-x1[0]) > abs(x0[1]-x0[0])
    print(f'PASS: {tested} concave-profile edge-interval comparisons; '
          f'{len(exact_grid)} exact witness/KKT checks; nonconcave growth witness.')


if __name__ == '__main__':
    run()
