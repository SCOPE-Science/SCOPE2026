#!/usr/bin/env python3
"""Exact finite checks of Jacobi coefficient/orthogonality identities.

Finite checks are corroboration only; see RESULT.md for the all-degree proof.
Uses only the Python standard library.
"""
from math import comb
from fractions import Fraction as Q


def jacobi_shifted(m, a, b):
    """Coefficients of P_m^(a,b)(2x-1), ascending degree."""
    c = [0] * (m + 1)
    for j in range(m + 1):
        coeff = comb(m + a, j) * comb(m + b, m - j)
        for k in range(m - j + 1):
            c[j + k] += coeff * comb(m - j, k) * (-1)**(m - j - k)
    return [Q(v) for v in c]


def dot_weight(p, q, weight):
    out = Q(0)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            s = i + j
            if weight == "left":  # x^2
                moment = Q(1, s + 3)
            else:  # (1-x)^2
                moment = Q(1, s + 1) - 2*Q(1, s + 2) + Q(1, s + 3)
            out += a*b*moment
    return out


def main():
    ident = 0
    orth = 0
    for n in range(1, 45):
        a = jacobi_shifted(n-1, 2, 0)
        b = jacobi_shifted(n-1, 0, 2)
        # If J[(1-t)P_m^(2,0)] = x P_m^(0,2)/(n(n+1)),
        # then coefficients of the two degree-(n-1) polynomials agree:
        # integral_0^x(x-t) sum a_k t^k = x^2 sum a_k/((k+1)(k+2)) x^k.
        lhs = [coef/Q(k+1)/Q(k+2) for k,coef in enumerate(a)]
        rhs = [coef/Q(n*(n+1)) for coef in b]
        assert lhs == rhs, (n, lhs, rhs)
        ident += 1
    for i in range(14):
        for j in range(14):
            for typ,a,b in (("left",0,2),("right",2,0)):
                ip = dot_weight(jacobi_shifted(i,a,b),jacobi_shifted(j,a,b),typ)
                expect = Q(1,2*i+3) if i == j else Q(0)
                assert ip == expect, (i,j,typ,ip,expect)
                orth += 1
    assert sum(Q(1,n*(n+1)) for n in range(1,60)) == Q(59,60)
    print('REAL_CESARO_JACOBI_EXACT_OK', ident, 'polynomial-integral identities;', orth, 'weighted orthogonality identities')


if __name__ == '__main__':
    main()
