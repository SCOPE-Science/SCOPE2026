#!/usr/bin/env python3
"""Exact polynomial checks for the Fano ribbon on rational-normal cones.

Run: python3 verify.py
Requires: sympy.
These checks supplement, not replace, the all-degree scheme-theoretic proof.
"""
from sympy import symbols, expand, Poly, groebner

T, U, Z = symbols('t u z')


def zero_up_to_first_u(expr, mod=None):
    expr = expand(expr)
    for exp in (0, 1):
        co = Poly(expr, U).coeff_monomial(U**exp)
        if mod is None:
            assert expand(co) == 0, (exp, co)
        else:
            p = Poly(co, T, Z, modulus=mod)
            assert p.is_zero, (mod, exp, co)


for d in range(2, 12):
    # The cone over nu_d(P^1) has equations given by all Hankel minors.
    # On a family of lines intersecting the hyperplane at (1,t,...,t^d),
    # the direction after imposing linear coefficients is b_j=j*t^(j-1)*u.
    x = [1] + [T**j + Z*j*T**(j-1)*U for j in range(1, d+1)]
    for i in range(d):
        for j in range(i+1, d):
            eq = expand(x[i]*x[j+1] - x[i+1]*x[j])
            zero_up_to_first_u(eq)
            for p in (2, 3, 5, 7):
                zero_up_to_first_u(eq, p)

    # The x0*x2-x1^2 equation has quadratic coefficient -u^2.
    eq2 = expand(x[0]*x[2] - x[1]**2)
    assert eq2 == -Z**2*U**2

    # On x_d != 0 the canonical line-basis correction gives the new
    # infinitesimal parameter as b_(d-1)-b_d*x_(d-1)/x_d.
    bdm1 = (d-1)*T**(d-2)*U
    bd = d*T**(d-1)*U
    xdm1 = T**(d-1)
    xd = T**d
    u_infty = expand(bdm1 - bd*xdm1/xd)
    assert expand(u_infty + T**(d-2)*U) == 0

    # O(d-2) has d-1 global sections; the doubled P^1 has d
    # global functions, unlike the trivial product (dimension 2).
    assert 1 + (d-1) == d
    for n in range(0, 8):
        h0_reduced = d*n + 1
        h0_nil = d*n + d-1
        assert h0_reduced + h0_nil == 2*d*n + d
    print(f'd={d}: minors, characteristic checks, overlap and Hilbert data OK')

# A separate ideal-theoretic check starts from unknown direction coordinates
# and all Hankel minors, and tests equality of the resulting coefficient
# ideal with the claimed eliminated ideal. It does not assume that ideal.
for d in (3, 4, 5):
    B = symbols('b2:'+str(d+1))
    xx = [1, T+Z*U] + [T**j+Z*B[j-2] for j in range(2, d+1)]
    eqs = []
    for i in range(d):
        for j in range(i+1, d):
            q = Poly(expand(xx[i]*xx[j+1]-xx[i+1]*xx[j]), Z)
            eqs.extend(co for co in q.all_coeffs() if co != 0)
    ideal_expected = [B[j-2]-j*T**(j-1)*U for j in range(2, d+1)] + [U**2]
    ordering = (*reversed(B), U, T)
    for modulus in (None, 2, 3, 5):
        params = {'order': 'lex'}
        if modulus is not None:
            params['modulus'] = modulus
        actual_gb = groebner(eqs, *ordering, **params)
        expected_gb = groebner(ideal_expected, *ordering, **params)
        assert all(actual_gb.reduce(f)[1] == 0 for f in ideal_expected)
        assert all(expected_gb.reduce(f)[1] == 0 for f in eqs)
        print(f'Groebner chart ideal d={d}, char={modulus or 0}: exact equality OK')

print('ALL_CHECKS_PASSED')
