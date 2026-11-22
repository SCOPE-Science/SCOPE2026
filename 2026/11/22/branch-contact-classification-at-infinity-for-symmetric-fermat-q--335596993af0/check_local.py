#!/usr/bin/env python3
"""Exact finite consistency checks for the symmetric Fermat quotient plane model.

Requires Python 3 and SymPy. These checks are illustrative; the infinite family
is proved algebraically in RESULT.md rather than inferred from sample degrees.
"""
import sympy as sp

u, v, w = sp.symbols("u v w")


def newton_power_sum(n, e1, e2, e3):
    p = [sp.Integer(3), e1, e1**2 - 2*e2,
         e1**3 - 3*e1*e2 + 3*e3]
    for _ in range(4, n+1):
        p.append(sp.expand(e1*p[-1] - e2*p[-2] + e3*p[-3]))
    return sp.expand(p[n])


def check(n):
    assert n >= 5 and sp.gcd(n, 6) == 1
    d = (n-1)//2
    polynomial = sp.Poly(newton_power_sum(n, 1, u, v), u, v)
    homogeneous_top = sum(co * u**i * v**j
                          for (i,j),co in polynomial.terms() if i+j == d)
    assert sp.expand(homogeneous_top - n*(-1)**(d-1)*u**(d-1)*(v-u)) == 0

    # In chart V=1, local coordinates at [0:1:0] are (u,w).
    local = sp.Poly(sum(co*u**i*w**(d-i-j)
                        for (i,j),co in polynomial.terms()), u, w)
    multiplicity = min(i+j for (i,j),co in local.terms())
    tangent = sp.expand(sum(co*u**i*w**j for (i,j),co in local.terms()
                             if i+j == multiplicity))
    ell = (n-5)//6 if n%6 == 5 else (n-1)//6
    expected_tangent = w**ell*((ell+1)*w-u) if n%6==5 else w**ell
    assert sp.expand(tangent / sp.LC(sp.Poly(tangent, u, w)) -
                     expected_tangent / sp.LC(sp.Poly(expected_tangent, u, w))) == 0 or \
           sp.simplify(tangent / expected_tangent).is_number

    # The generic orbit parameter is lambda = e3^2/e2^3 at e1=0.
    boundary = sp.Poly(newton_power_sum(n, 0, 1, v) / v, v)
    assert all(exp[0]%2 == 0 for exp,co in boundary.terms())
    q = sp.Poly(sum(co*v**(exp[0]//2) for exp,co in boundary.terms()), v)
    generic_branches = ell if n%6==5 else ell-1
    assert q.degree() == generic_branches
    assert q.eval(0) != 0
    assert sp.gcd(q, q.diff()).degree() == 0
    c = 1 if n%6==5 else 2
    delta = 3*generic_branches*(generic_branches-1)//2+c*generic_branches
    genus = (n-1)*(n-5)//12
    assert delta == (d-1)*(d-2)//2-genus
    print(f"n={n} degree={d} generic_branches={generic_branches} "
          f"distinguished_contact={c} delta={delta} genus={genus} PASS")


if __name__ == "__main__":
    for n in [5,7,11,13,17,19,23,25,29,31]:
        check(n)
    print("ALL EXACT SAMPLE CHECKS PASSED")
