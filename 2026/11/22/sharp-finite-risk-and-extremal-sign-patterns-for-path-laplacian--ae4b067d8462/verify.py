"""Standalone exact-arithmetic checks for a path-Laplacian sign-probe theorem.

Python 3.10+, standard library only. Finite checks support but do not replace
analytic proofs for all n or the weak limit.
"""
from fractions import Fraction as Q
from itertools import product


def path_matrix(n):
    H = [[Q(int(i <= j)) - Q(j, n) for i in range(1, n + 1)]
         for j in range(1, n)]
    B = [[sum(H[j][i] * H[j][k] for j in range(n - 1))
          for k in range(n)] for i in range(n)]
    return B


def energy(z):
    n = len(z)
    total = sum(z)
    s = 0
    out = Q(0)
    for j in range(1, n):
        s += z[j - 1]
        out += (s - Q(j * total, n)) ** 2
    return out


def theoretical_max(n):
    if n % 2 == 0:
        return Q(n * (n * n + 2), 12)
    return Q(n**4 - 1, 12 * n)


def verify(n):
    B = path_matrix(n)
    mean = sum(B[i][i] for i in range(n))
    var = 4 * sum(B[i][j]**2 for i in range(n) for j in range(i + 1, n))
    assert mean == Q(n * n - 1, 6)
    assert var == Q((n * n - 1) * (2*n**3 - 6*n*n + 7*n + 9), 90*n)
    for i in range(n):
        assert B[i][i] == Q((2*i - (n - 1))**2, 4*n) + Q(n*n - 1, 12*n)
    vals = {}
    for z in product((-1, 1), repeat=n):
        val = energy(z)
        assert val == sum(B[i][j] * z[i] * z[j] for i in range(n) for j in range(n))
        vals[z] = val
    m = sum(vals.values()) / len(vals)
    v = sum((x - m)**2 for x in vals.values()) / len(vals)
    assert (m, v) == (mean, var)
    peak = max(vals.values())
    assert peak == theoretical_max(n)
    expected = set()
    for k in {n//2, (n+1)//2}:
        expected.add((1,)*k + (-1,)*(n-k))
        expected.add((-1,)*k + (1,)*(n-k))
    assert {z for z in vals if vals[z] == peak} == expected
    assert {z for z in vals if vals[z] == 0} == {(1,)*n, (-1,)*n}
    # Check strict separation of any plus-prefix/minus-middle/plus-suffix design.
    for k in range(1, n):
        r = n-k
        block = Q(2*k*r*(2*k*r+1), 3*n)
        for m in range(k+1):
            ell=k-m
            z=(1,)*m+(-1,)*r+(1,)*ell
            assert energy(z)==block-Q(4*ell*m*r*r, n)
    return len(vals)


if __name__ == '__main__':
    checks=0
    for n in range(2, 12):
        checks+=verify(n)
    print(f'PASS: exact matrix, moments, sign-pattern extrema and gap checks for n=2..11; {checks} sign configurations')
