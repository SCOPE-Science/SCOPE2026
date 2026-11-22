#!/usr/bin/env python3
"""Exact finite checks for a Cayley--Chebyshev stable pencil.

Requires Python 3 and SymPy. This is a finite regression check,
not a substitute for the all-degree proof in RESULT.md.
"""
from sympy import Poly, symbols, chebyshevt, chebyshevu, discriminant, gcd, factor, degree, expand

x, lam = symbols("x lam")

def expected_exponents(n):
    if n % 2 == 0:
        k = n // 2
        return {0: 2 * k + 3, 2: k, -2: k + 3}
    k = (n - 1) // 2
    return {0: 2 * k + 4, 2: k + 2, -2: k + 2}

def node_counts(n):
    if n % 2 == 0:
        k = n // 2
        return {0: n + 1, 2: k, -2: k + 1}
    k = (n - 1) // 2
    return {0: n + 1, 2: k + 1, -2: k + 1}

def test_degree(n):
    T = chebyshevt(n, x)
    U = chebyshevu(n - 1, x)
    F = expand((x*x - 1) * ((T + lam)**2 - 1))
    assert expand(F.subs(lam, 0) - (x*x - 1)**2 * U**2) == 0
    D = factor(discriminant(F, x))
    ex = expected_exponents(n)
    E = lam**ex[0] * (lam - 2)**ex[2] * (lam + 2)**ex[-2]
    quotient = factor(D / E)
    assert not quotient.has(lam) and quotient != 0, (n, quotient)
    for val, count in node_counts(n).items():
        G = Poly(F.subs(lam, val), x)
        multiple = gcd(G, G.diff())
        assert multiple.degree() == count, (n, val, multiple.degree(), count)
        assert gcd(multiple, multiple.diff()).degree() == 0, (n, val)
    assert gcd(Poly(F.subs(lam, 3), x), Poly(F.subs(lam, 3), x).diff()).degree() == 0
    print(f"n={n}: discriminant exponents {ex}; double roots {node_counts(n)}; generic fiber squarefree")

for n in range(2, 9):
    test_degree(n)
print("PASS: seven exact finite degree checks; universal results require the written proof")
