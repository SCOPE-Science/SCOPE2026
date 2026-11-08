#!/usr/bin/env python3
"""Exact finite witnesses for Hankel endpoint generic-degree theorem.

Requires Python 3, SymPy. Finite instances corroborate, not prove, all-rank claims.
"""
import itertools
import math
import sympy as sp


def witness(r, n):
    assert n >= 2*r+1
    samples = [(i + 2, i + 3) for i in range(r)]
    x = [sum(a * z**k for a, z in samples) for k in range(n)]
    unknown = sp.symbols('v0:' + str(n-2*r))
    vals = [sp.Integer(x[i]) if i < r or i >= n-r else unknown[i-r] for i in range(n)]
    minors = [sp.expand(sp.Matrix([[vals[i+j] for j in cols] for i in range(r+1)]).det(method='berkowitz'))
              for cols in itertools.combinations(range(n-r), r+1)]
    basis = sp.groebner(minors, *unknown, order='grevlex', domain=sp.QQ)
    assert basis.is_zero_dimensional
    leads = [sp.Poly(p, *unknown).terms(order='grevlex')[0][0] for p in basis.polys]
    powers = [min(e[j] for e in leads if e[j] > 0 and all(e[k] == 0 for k in range(len(unknown)) if k != j))
              for j in range(len(unknown))]
    count = sum(not any(all(a >= b for a, b in zip(mon, lead)) for lead in leads)
                for mon in itertools.product(*(range(p) for p in powers)))
    expected = math.comb(n-r,r)
    assert count == expected, (r, n, count, expected)
    for j in list(range(r)) + list(range(n-r,n)):
        unit = [int(i == j) for i in range(n)]
        mat = sp.Matrix([[unit[i+k] for k in range(n-r)] for i in range(r+1)])
        assert mat.rank() <= r
    print('HANKEL_ENDPOINT_WITNESS_OK', r, n, count)


if __name__ == '__main__':
    for r, n in [(2,5),(2,6),(2,7),(3,7),(3,8),(3,9),(4,9)]:
        witness(r,n)
    print('ENDPOINT_SEVEN_EXACT_SPECIALIZATIONS_OK')
