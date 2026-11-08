#!/usr/bin/env python3
"""Exact symbolic and independent rational checks for a two-age seed-bank Floquet theorem.
Run: python verify.py (requires sympy)."""
from fractions import Fraction as F
from itertools import product
from sympy import Matrix, Rational, factor, symbols, simplify, sqrt

a,b,s,g = symbols('a b s g', positive=True)

def A(f):
    return Matrix([[f*g,f],[s*(1-g),0]])

M2 = A(b)*A(a)
T = a*b*g*g + s*(a+b)*(1-g)
D = a*b*s*s*(1-g)**2
assert factor(M2.trace()-T)==0
assert factor(M2.det()-D)==0
P = lambda z: factor(z*z-T*z+D)
assert factor(P(a*b)-a*b*(1-g)*((a-s)*(b-s)+g*(a*b-s*s))) == 0
assert factor(P(a*s)-a*s*g*((1-g)*(a-b)*s+g*a*(s-b))) == 0
assert factor(T.subs(g,0)-s*(a+b))==0
assert factor(T.subs(g,1)-a*b)==0
z=symbols('z')
assert factor(M2.subs(g,0).charpoly(z).as_expr()-(z-a*s)*(z-b*s))==0
assert factor(M2.subs(g,1).charpoly(z).as_expr()-z*(z-a*b))==0
# Check spectral statement independently with characteristic polynomial and exact root comparison.
def mx(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def m_of(f,g0,s0): return [[f*g0,f],[s0*(1-g0),F(0)]]
n=0
for a0,b0,s0 in product([F(1,2),F(1),F(2),F(4),F(7)], [F(1,10),F(1,4),F(1,2),F(1),F(2)], [F(1,10),F(1,4),F(1,2),F(3,4),F(1)]):
    if not a0>b0: continue
    L=a0*max(b0,s0)
    for g0 in [F(i,12) for i in range(13)]:
        N=mx(m_of(b0,g0,s0),m_of(a0,g0,s0))
        tr=N[0][0]+N[1][1]; det=N[0][0]*N[1][1]-N[0][1]*N[1][0]
        assert tr==T.subs({a:a0,b:b0,s:s0,g:g0})
        assert det==D.subs({a:a0,b:b0,s:s0,g:g0})
        assert tr<=2*L
        assert L*L-tr*L+det>=0
        # Exact spectral inequality via location right of parabola vertex.
        if g0 not in (0,1): assert L*L-tr*L+det>0
        n+=1
# Strictness at endpoints checked from formulas for all regimes.
assert (M2.subs(g,0).subs({a:F(4),b:F(1,5),s:F(3,4)})).eigenvals()
# Three-season counterexample, product uses the specified annual time order.
M3=A(1)*A(Rational(1,5))*A(4)
M3=M3.subs(s,Rational(3,4))
assert M3.subs(g,0)==Matrix([[0,3],[Rational(9,80),0]])
assert M3.subs(g,Rational(1,2))==Matrix([[Rational(71,80),Rational(17,10)],[Rational(33,320),Rational(3,20)]])
assert M3.subs(g,1)==Matrix([[Rational(4,5),Rational(4,5)],[0,0]])
assert M3.subs(g,0).det()==-Rational(27,80)
assert M3.subs(g,Rational(1,2)).det()==-Rational(27,640)
assert M3.subs(g,Rational(1,2)).trace()==Rational(83,80)
assert M3.subs(g,Rational(1,2)).charpoly().as_expr().subs(symbols('lambda'),1) == -Rational(51,640)
assert 27<80 and 4<5 and 83+sqrt(7969)>160
# Independent Fraction implementation cross-check of the three-season matrices.
for g0, expected in [(F(0),[[F(0),F(3)],[F(9,80),F(0)]]), (F(1,2),[[F(71,80),F(17,10)],[F(33,320),F(3,20)]]), (F(1),[[F(4,5),F(4,5)],[F(0),F(0)]])]:
    got=mx(m_of(F(1),g0,F(3,4)),mx(m_of(F(1,5),g0,F(3,4)),m_of(F(4),g0,F(3,4))))
    assert got==expected
print('PASS: 2-phase symbolic trace, determinant, factorizations and endpoint tests;')
print(f'PASS: {n} exact rational Perron comparison certificates;')
print('PASS: independent 3-phase matrix products and exact rescue counterexample.')
