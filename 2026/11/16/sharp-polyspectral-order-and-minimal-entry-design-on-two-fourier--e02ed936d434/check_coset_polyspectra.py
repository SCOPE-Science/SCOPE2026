"""Exact integer checks of sparse mixed-polyspectral measurement rows.

The mathematical proof for all finite abelian groups is in RESULT.md.
Requires sympy; run: python check_coset_polyspectra.py
"""
from itertools import product
from math import prod
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def check(factors, q, nonsplit=False):
    """H = product C_n; either H x C_q or cyclic extension for 1 factor."""
    H = list(product(*(range(n) for n in factors)))
    if not factors:
        H = [()]
    zero = tuple(0 for _ in factors)
    h_size = len(H)
    if nonsplit:
        assert len(factors) == 1
        n = factors[0]
        def h_elem(h): return (q * h[0]) % (n * q)
        def a_h(h): return (1 + q * h[0]) % (n * q)
        def add(x, y): return (x + y) % (n * q)
    else:
        def h_elem(h): return tuple(h) + (0,)
        def a_h(h): return tuple(h) + (1,)
        def add(x, y): return tuple((x[i] + y[i]) % factors[i]
                                    for i in range(len(factors))) + ((x[-1] + y[-1]) % q,)
    support = [h_elem(h) for h in H] + [a_h(h) for h in H]
    assert len(set(support)) == 2 * h_size
    idx = {s: i for i, s in enumerate(support)}
    rows = []
    def row(inputs):
        out = inputs[0]
        for v in inputs[1:]: out = add(out, v)
        assert out in idx
        r = [0] * (2 * h_size)
        for v in inputs: r[idx[v]] += 1
        r[idx[out]] -= 1
        rows.append(r)
    row([h_elem(zero), h_elem(zero)])
    generators = []
    for j, n in enumerate(factors):
        e = [0] * len(factors); e[j] = 1
        generators.append(tuple(e))
    special = set(generators) | {zero}
    for h in H:
        if h in special: continue
        j = next(i for i, k in enumerate(h) if k)
        p = list(h); p[j] -= 1
        row([h_elem(tuple(p)), h_elem(generators[j])])
    for j, n in enumerate(factors):
        torsion = tuple((n-1) if i == j else 0 for i in range(len(factors)))
        row([h_elem(torsion), h_elem(generators[j])])
    for h in H:
        if h == zero: continue
        j = next(i for i, k in enumerate(h) if k)
        p = list(h); p[j] -= 1
        row([a_h(tuple(p)), h_elem(generators[j])])
    row([a_h(zero)] * q)
    assert len(rows) == len(support) == 2 * h_size
    matrix = Matrix(rows)
    det = matrix.det(method='domain-ge')
    assert abs(det) == h_size*q, (factors, q, det)
    smith = smith_normal_form(matrix, domain=ZZ)
    diagonal = [abs(int(smith[i,i])) for i in range(smith.rows)]
    assert prod(diagonal) == h_size*q
    if nonsplit:
        assert diagonal == [1] * (2*h_size-1) + [h_size*q]
    return diagonal


def main():
    count = 0
    for h in range(1, 9):
        for q in range(3, 10):
            if h == 1:
                check([], q)
            else:
                check([h], q, nonsplit=True)
                check([h], q, nonsplit=False)
            count += 1
    split = [(2,2),(2,3),(3,3),(2,4),(2,2,2),(2,3,3)]
    for H in split:
        for q in range(3, 8):
            check(H, q)
            count += 1
    print(f'CHECK_OK exact_phase_matrices={count} determinant_and_smith_verified=true')


if __name__ == '__main__':
    main()
