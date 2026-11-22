#!/usr/bin/env python3
"""Exact rational polynomial checks for Lie-jet degree growth of gradient ODEs.

Finite checks supplement, and do not replace, the homogeneous-ray proof.
Run: python3 gradient_degree_checker.py
"""
import sympy as sp
x, y = sp.symbols('x y')

def high_part(expr):
    P = sp.Poly(sp.expand(expr), x, y, domain=sp.QQ)
    d = P.total_degree()
    return d, sp.Add(*[co*x**i*y**j for (i,j), co in P.terms() if i+j==d])

def run(V, i, a, max_k, target_d):
    V = sp.expand(V)
    _, Vtop = high_part(V)
    def deriv(p, potential):
        return sp.expand(-sp.diff(potential,x)*sp.diff(p,x) - sp.diff(potential,y)*sp.diff(p,y))
    full = i
    top = i
    checks=0
    for k in range(max_k+1):
        degree, H = high_part(full)
        assert degree == 1+k*(target_d-2), (V,k,degree)
        assert sp.simplify(H-top)==0, ('wrong top',k)
        assert H.subs({x:a[0],y:a[1]})!=0, ('zero along extremal ray',k)
        checks += 3
        full=deriv(full,V)
        top=deriv(top,Vtop)
    print('PASS degree',target_d,'k=0..',max_k,'checks',checks,'potential',str(V))
    return checks

if __name__=='__main__':
    total=0
    total+=run(x**3 + x*y*y + y, x, (1,0), 8,3)
    total+=run((x*x+y*y)**2/sp.Integer(4)+(x*x+y*y)/2, x, (1,0), 7,4)
    total+=run(x**5/sp.Integer(5)+y**5/sp.Integer(5)+x*y, x, (1,0), 6,5)
    # The affine boundary closes in degree <= 1 after adjoining the constant observable.
    for W in [0, x+y, x*x/2+y*y/3+x, x*y+4*x+5*y]:
        f=-sp.diff(W,x); g=-sp.diff(W,y)
        for coordinate in (x,y):
            assert sp.Poly(f*sp.diff(coordinate,x)+g*sp.diff(coordinate,y),x,y).total_degree()<=1
            total += 1
    print('PASS all',total,'exact rational checks')
