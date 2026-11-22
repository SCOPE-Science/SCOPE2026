#!/usr/bin/env python3
"""Exact symbolic checks for the cat-driven Möbius Lyapunov expansion.

Requires Python 3 with SymPy. Finite Fourier checks corroborate but do not
replace the infinite no-four-wave-resonance lemma in RESULT.md.
"""
from itertools import combinations_with_replacement, product
import sympy as s

e, x = s.symbols('e x', real=True, positive=True)
q = (1-e)/(1+e)
J = (1-e*e)/(1+2*e*s.cos(2*s.pi*x)+e*e)
a3 = s.factor(s.diff(J,x,2).subs(x,0)/6)
ell2 = s.factor(s.diff(s.log(J),x,2).subs(x,0)/2)
ell4 = s.factor(s.diff(s.log(J),x,4).subs(x,0)/24)
U2 = 1/(2*(1-q*q))
U4 = s.Rational(3,4)/(1-q*q)**2-s.Rational(3,8)/(1-q**4)
Uv = a3*q/(1-q*q)*U4
assert s.simplify(a3-4*s.pi**2*e*(1-e)/(3*(1+e)**3)) == 0
assert s.simplify(ell2*U2-s.pi**2/2) == 0
assert s.simplify(2*ell2*Uv+ell4*U4-s.pi**4*(e*e-e+1)/(16*e)) == 0
A = s.Matrix([[2,1],[1,1]])
Ai = A.inv()
K = [tuple(Ai**j*s.Matrix([1,0])) for j in range(1,15)]
assert K[:3] == [(1,-1),(2,-3),(5,-8)]
relations = 0
for indices in combinations_with_replacement(range(14), 4):
    for signs in product((-1,1),repeat=4):
        if sum(sign*K[j][0] for sign,j in zip(signs,indices)) == 0 and \
           sum(sign*K[j][1] for sign,j in zip(signs,indices)) == 0:
            signed_count = {}
            for sign,j in zip(signs,indices):
                signed_count[j] = signed_count.get(j,0)+sign
            assert all(v == 0 for v in signed_count.values()), (indices,signs)
            relations += 1
assert relations > 0
print('PASS: exact quadratic and quartic coefficients, first 14 modes,',relations,'trivial signed four-wave zero sums')
