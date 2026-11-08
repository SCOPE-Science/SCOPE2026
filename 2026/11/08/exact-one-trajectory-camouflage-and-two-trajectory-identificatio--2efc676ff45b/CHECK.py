"""Exact rational checks for the conserved-product ecological example.

Requires Python >=3.8, standard library only. The general theorem is analytic;
these checks are finite supporting calculations, not a substitute for proof.
"""
from fractions import Fraction as F


def determinant(a):
    n = len(a)
    assert all(len(row) == n for row in a)
    a = [[F(x) for x in row] for row in a]
    ans = F(1)
    for i in range(n):
        j = next((j for j in range(i, n) if a[j][i]), None)
        if j is None:
            return F(0)
        if j != i:
            a[i], a[j] = a[j], a[i]
            ans = -ans
        d = a[i][i]
        ans *= d
        for j in range(i + 1, n):
            m = a[j][i] / d
            for k in range(i + 1, n):
                a[j][k] -= m * a[i][k]
            a[j][i] = F(0)
    return ans


def point(q, p, u):
    # lambda=2, r=b=theta=1, x(0)=1/2, y(0)=1.
    # s=e^(-2t)=u^p, g=1+q=6/p, e^(-gt)=u^3.
    g = 1 + q
    assert g == F(6, p)
    h = g * 2 - 1
    x = g / (1 + h * u**3)
    y = F(2) / (1 + u**p)
    z = q / y
    return x, y, z


def verify_point(q, p, u):
    x, y, z = point(q, p, u)
    g, h = 1 + q, 2 * (1 + q) - 1
    # u'=-(2/p)u; use exact differentiations of rational parametrizations.
    dxdt = F(6, p) * g * h * u**3 / (1 + h*u**3)**2
    dydt = F(4)*u**p / (1 + u**p)**2
    dzdt = -q * dydt / y**2
    assert dxdt == x * (1 - x + y*z)
    assert dydt == y * (2 - y)
    assert dzdt == z * (y - 2)
    assert y*z == q
    return [F(1), x, y, z, y*z]


def main():
    q0, q1 = F(1, 2), F(2)
    u0 = [F(1, k) for k in (1, 2, 3, 4)]
    rows0 = [verify_point(q0, 4, u) for u in u0]
    rows1 = [verify_point(q1, 2, F(1, 2))]
    det4 = determinant([row[:4] for row in rows0])
    det5 = determinant(rows0 + rows1)
    assert det4 == F(185495875, 789933095424), det4
    assert det5 == F(185495875, 526622063616), det5
    assert all(row[-1] == q0*row[0] for row in rows0)
    assert all(row[-1] == q1*row[0] for row in rows1)
    assert (1+q1)-(1+q0) == F(3, 2)
    assert ((1+q1) - (1+q0)) / 1 == F(3, 2)
    print('PASS: five exact ODE evaluation points, two rational minors,')
    print('      single-leaf dependence and two-leaf rank, exact intervention offset.')
    print('det4=', det4, '; det5=', det5)


if __name__ == '__main__':
    main()
