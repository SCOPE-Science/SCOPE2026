"""Exact tetrahedral triangulation checks for a one-vertex simplex frustum.
Uses only the Python standard library; finite tests supplement the analytic proof.
"""
from fractions import Fraction as F


def det3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def tetra_moments(v):
    """Volume, first and second unnormalized moments from barycentric integration."""
    rows = [[v[i + 1][j] - v[0][j] for j in range(3)] for i in range(3)]
    vol = abs(det3(rows)) / 6
    sums = [sum(v[k][j] for k in range(4)) for j in range(3)]
    first = [vol * z / 4 for z in sums]
    second = [[vol * (sums[i] * sums[j] + sum(v[k][i] * v[k][j]
                     for k in range(4))) / 20 for j in range(3)] for i in range(3)]
    return vol, first, second


def integrate_frustum(t):
    e = [tuple(F(int(i == j)) for j in range(3)) for i in range(3)]
    q = [tuple(t * z for z in vi) for vi in e]
    # A disjoint-interior decomposition into three tetrahedra.
    tetrahedra = [(q[0], q[1], q[2], e[0]),
                  (e[0], q[1], q[2], e[1]),
                  (e[0], e[1], q[2], e[2])]
    v = F(0); m = [F(0)] * 3; a = [[F(0)] * 3 for _ in range(3)]
    for tet in tetrahedra:
        w, b, c = tetra_moments(tet)
        v += w
        m = [m[i] + b[i] for i in range(3)]
        a = [[a[i][j] + c[i][j] for j in range(3)] for i in range(3)]
    mean = [z / v for z in m]
    cov = [[a[i][j] / v - mean[i] * mean[j] for j in range(3)] for i in range(3)]
    return v, mean, cov


def theorem(t):
    p = sum(t ** i for i in range(5))
    q = 1 + 4*t + 10*t*t + 4*t**3 + t**4
    return F(9, 8000) * p*p*q / (1 + t + t*t)**6


def main():
    count = 0
    params = [F(0), F(1, 100), F(1, 7), F(1, 4), F(1, 3),
              F(1, 2), F(2, 3), F(3, 4), F(9, 10), F(99, 100)]
    previous = None
    for t in params:
        vol, mean, cov = integrate_frustum(t)
        assert vol == (1 - t**3) / 6; count += 1
        expected_mean = (1 - t**4) / (4*(1 - t**3))
        b = (1-t**5) / (20*(1-t**3))
        for i in range(3):
            assert mean[i] == expected_mean; count += 1
            for j in range(3):
                expect = (2 if i == j else 1)*b - expected_mean**2
                assert cov[i][j] == expect; count += 1
        norm = det3(cov) / vol**2
        assert norm == theorem(t); count += 1
        if previous is not None:
            assert norm < previous; count += 1
        previous = norm
    assert theorem(F(0)) == F(9, 8000); count += 1
    # Limiting three-dimensional affine-normalized value, computed from
    # triangular simplex x line interval: (1/108)*(1/12)=1/1296.
    assert theorem(F(1)) == F(1, 1296); count += 1
    print('EXACT_FRUSTUM_TETRAHEDRAL_CHECKS_PASSED', count)

if __name__ == '__main__':
    main()
