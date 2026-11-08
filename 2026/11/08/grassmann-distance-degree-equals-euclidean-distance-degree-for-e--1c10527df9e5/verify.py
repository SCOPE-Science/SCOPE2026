#!/usr/bin/env python3
"""Exact symbolic witnesses for projector-data distance on scroll ruling curves.
Requires Python 3 and SymPy.  Run: python verify.py
"""
import sympy as sp

t = sp.Symbol('t')

def witness(u):
    assert len(u) >= 2
    n = [len(x)-1 for x in u]
    assert all(v >= 2 for v in n)
    f = [sum(sp.Integer(a)*t**j for j,a in enumerate(x)) for x in u]
    k = [sum(sp.Integer(a)**2 for a in x) for x in u]
    assert all(a != 0 for a in k)
    s = [sum(t**(2*j) for j in range(x+1)) for x in n]
    L = sp.Poly(1,t)
    for si in s: L=sp.lcm(L,sp.Poly(si,t))
    G = sp.cancel(sum(f[i]**2*sp.cancel(L.as_expr()/s[i])/k[i] for i in range(len(n))))
    assert sp.denom(G) == 1
    H = sp.Poly(sp.diff(G,t)*L.as_expr()-G*sp.diff(L.as_expr(),t),t).clear_denoms()[1]
    cut = sp.Poly(sp.prod(f),t)
    assert sp.gcd(sp.Poly(G,t),L).degree() == 0
    assert H.degree()==2*L.degree()-2
    assert sp.gcd(H,H.diff()).degree() == 0
    assert sp.gcd(H,L).degree() == 0
    assert sp.gcd(H,cut).degree() == 0
    print('SCROLL',tuple(n),'LCM_DEGREE',L.degree(),'GD_CRITICAL_COUNT',H.degree(),'SIMPLE_NONPOLE_NONCUT PASS')
    return H

if __name__=='__main__':
    witness([[1,2,3],[1,2,3,4]])
    witness([[1,2,3],[1,2,3,4,5]])
    witness([[1,2,3,4],[1,2,3,4,5]])
    witness([[1,2,3],[1,3,2]])
    witness([[1,2,3,4],[1,2,3,4,5,6]])
    print('ALL_EXACT_PROJECTOR_CHECKS_PASS')
