#!/usr/bin/env python3
"""Symbolic verification of the algebra used in the gradient spectrum proof.

Requires SymPy. This checks algebraic equalities, not literature priority.
"""
import sympy as sp

d,a=sp.symbols('d a',positive=True)
alpha=(1-a)*(1+2*a/d)
beta=a*(d-2+4*a)/(2*d)
gamma=-2*a*a/d
L=alpha+2*(d-1)*beta+d*(d-1)*gamma/2
T=alpha+(d-2)*beta
p=lambda x:(1-x)*(T-x)-a*a*(d-2)/2
checks={
  'alpha_order': p(alpha)-a*a*(d-2)*(d*(3*a-2)+4*a*a-6*a+2)/d**2,
  'L_order':p(L)-a*a*(d-2)*(d*(a-1)-3*a+1)*(d*(2*a-1)-6*a+4)/(2*d),
  'L_minus_alpha':L-alpha-a*(d-1)*(d*(1-a)+4*a-2)/d,
  'mu_product':T-a*a*(d-2)/2-p(0),
  'upper_growth':sp.limit(T/d,d,sp.oo)-a/2,
  'lower_growth':sp.limit(p(0)/T,d,sp.oo)-(1-a),
}
for name,res in checks.items():
    assert sp.simplify(res)==0,(name,res)
print('ORTHANT_GRADIENT_SYMBOLIC_IDENTITIES_PASS',len(checks))
