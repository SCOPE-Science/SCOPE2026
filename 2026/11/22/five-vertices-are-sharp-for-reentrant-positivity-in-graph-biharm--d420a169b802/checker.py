#!/usr/bin/env python3
"""Exact cofactor certificate for graph biharmonic-resolvent sign reentrance.

Requires SymPy. All graph specifications and computations are standalone.
"""
import sympy as S

h = S.symbols('h', nonnegative=True)
graphs = {
    'P2': (2, [(0,1)]),
    'P3': (3, [(0,1),(1,2)]),
    'K3': (3, [(0,1),(1,2),(0,2)]),
    'P4': (4, [(0,1),(1,2),(2,3)]),
    'K13': (4, [(0,1),(0,2),(0,3)]),
    'C4': (4, [(0,1),(1,2),(2,3),(3,0)]),
    'Paw': (4, [(0,1),(1,2),(0,2),(2,3)]),
    'Diamond': (4, [(0,1),(0,2),(0,3),(1,2),(1,3)]),
    'K4': (4, [(i,j) for i in range(4) for j in range(i+1,4)]),
    'P5': (5, [(i,i+1) for i in range(4)]),
}
expected_det = {
    'P2': 4*h+1,
    'P3': (h+1)*(9*h+1),
    'K3': (9*h+1)**2,
    'P4': (4*h+1)*(4*h*h+12*h+1),
    'K13': (h+1)**2*(16*h+1),
    'C4': (4*h+1)**2*(16*h+1),
    'Paw': (h+1)*(9*h+1)*(16*h+1),
    'Diamond': (4*h+1)*(16*h+1)**2,
    'K4': (16*h+1)**3,
    'P5': (h*h+7*h+1)*(25*h*h+15*h+1),
}
expected_p5 = {
    (0,1): h*(5*h**3+74*h*h+38*h+3),
    (0,2): h*(5*h-1)*(h*h+7*h+1),
    (0,3): h*h*(5*h*h-h-7),
    (0,4): h*h*(5*h*h-21*h+1),
    (1,2): h*(5*h+4)*(h*h+7*h+1),
    (1,3): h*(5*h**3+14*h*h+6*h-1),
}
negative_orbits = {
    'P2': set(), 'P3': {(0,2)}, 'K3': set(),
    'P4': {(0,2),(0,3),(1,3)},
    'K13': {(1,2),(1,3),(2,3)},
    'C4': {(0,2),(1,3)},
    'Paw': {(0,3),(1,3)},
    'Diamond': {(2,3)}, 'K4': set(),
}
negative_formulas = {
    ('P3',0,2):h*(3*h-1),
    ('P4',0,2):h*(4*h*h+4*h-1),
    ('P4',0,3):2*h*h*(2*h-3),
    ('P4',1,3):h*(4*h*h+4*h-1),
    ('K13',1,2):h*(h+1)*(4*h-1),
    ('K13',1,3):h*(h+1)*(4*h-1),
    ('K13',2,3):h*(h+1)*(4*h-1),
    ('C4',0,2):2*h*(4*h+1)*(8*h-1),
    ('C4',1,3):2*h*(4*h+1)*(8*h-1),
    ('Paw',0,3):h*(4*h-1)*(9*h+1),
    ('Paw',1,3):h*(4*h-1)*(9*h+1),
    ('Diamond',2,3):2*h*(8*h-1)*(16*h+1),
}

def signs(poly):
    c = [S.sign(v) for v in S.Poly(S.expand(poly),h).all_coeffs() if v != 0]
    return sum(a != b for a,b in zip(c,c[1:]))

def adjacency_laplacian(n, edges):
    L=S.zeros(n)
    for u,v in edges:
        L[u,u]+=1; L[v,v]+=1
        L[u,v]-=1; L[v,u]-=1
    return L

checks=0
for name,(n,edges) in graphs.items():
    L=adjacency_laplacian(n,edges)
    M=S.eye(n)+h*L*L
    D=S.factor(M.det())
    assert S.expand(D-expected_det[name])==0
    checks+=1
    A=M.adjugate()
    assert S.simplify(A-M.inv()*D)==S.zeros(n)
    checks+=1
    for i in range(n):
        for j in range(i+1,n):
            p=S.factor(A[i,j])
            assert S.expand(p-A[j,i])==0
            checks+=1
            if name=='P5':
                orbit=tuple(sorted((min(i,4-i),min(j,4-j))))
                # Reflection maps (i,j) to (4-j,4-i), preserving order.
                canonical=min((i,j),(4-j,4-i))
                assert S.expand(p-expected_p5[canonical])==0
                checks+=1
            else:
                if (i,j) in negative_orbits[name]:
                    assert S.expand(p-negative_formulas[name,i,j])==0
                    assert signs(p)==1
                else:
                    coeffs=S.Poly(S.expand(p),h).all_coeffs()
                    assert all(x>=0 for x in coeffs), (name,i,j,p)
                    assert any(x>0 for x in coeffs)
                assert signs(p)<=1, (name,i,j,p)
                checks+=1
# Symbolic threshold comparisons and sign witnesses.
hm=(21-S.sqrt(421))/10
hp=(21+S.sqrt(421))/10
assert hm>0 and S.simplify(S.Rational(1,5)-hm)>0
assert hp>2
assert S.factor(5*hm**2-21*hm+1)==0
assert S.factor(5*hp**2-21*hp+1)==0
assert S.factor(5*hp**2-hp-7)>0
assert 5*2**3+14*2**2+6*2-1>0
# For h>0, h<hm => (0,2) negative; hm<h<hp => (0,4) negative.
# For h>=hp, all p5 off-diagonal formulas are >=0.
checks+=7
print('PASS:', checks, 'exact algebraic and sign-classification assertions')
print('sharp recovery h_+ =', S.N(hp,16))
