"""Exact algebra checks for a two-state Markov-sampled scalar quadratic SGD theorem.

Requires Python 3.10+ and SymPy. Run: python verify.py
This script checks algebraic identities and rational certificates; the associated
proof supplies the global real-root and spectral arguments.
"""
import sympy as S

h, ell, q = S.symbols('h ell q', real=True)
A = (1 - h*(1 + S.sqrt(q)))**2
B = (1 - h*(1 - S.sqrt(q)))**2
Pmark = S.Matrix([[(1 + ell)/2,(1 - ell)/2],
                  [(1 - ell)/2,(1 + ell)/2]])
T = Pmark * S.diag(A,B)
G = ell*(1-q)**2*h**3-4*ell*(1-q)*h**2 + (ell*(5-3*q)-(1+q))*h+2*(1-ell)
P = (27*q**3-18*q**2-q)*ell**3 \
    + (27*q**3-57*q**2+21*q+1)*ell**2 \
    + (9*q**3-56*q**2+41*q-2)*ell+(1+q)**3
assert S.simplify(S.det(S.eye(2)-T)-h*G)==0
assert S.simplify(S.det(T)-ell*A*B)==0
assert S.factor(S.discriminant(G,h)-4*ell*(1-q)**2*P)==0
assert S.factor(S.discriminant(P,ell)+256*q*(q-1)**3*(27*q*q-10*q-1)**3)==0
assert S.factor(P.subs(ell,-1)+4*(q-1)**2*(2*q-1))==0
assert S.factor(P.subs(ell,0)-(1+q)**3)==0
qstar = (5+2*S.sqrt(13))/27
ellstar = (-17+4*S.sqrt(13))/3
hstar = 4/(3*(1-qstar))
for j in range(3):
    assert S.simplify(S.diff(G,h,j).subs({q:qstar,ell:ellstar,h:hstar}))==0
assert 0 < float(qstar) < .5
assert -1 < float(ellstar) < 0
assert S.simplify(P.subs({q:S.Rational(1,2),ell:-S.Rational(19,20)}))==-S.Rational(733,64000)
qw=S.Rational(49,100)
ellw=-S.Rational(19,20)
Gw=S.factor(G.subs({q:qw,ell:ellw}))
assert S.simplify(Gw+S.Rational(3,200000)*(16473*h**3-129200*h**2+322900*h-260000))==0
expect={1:S.Rational(149481,200000),2:-S.Rational(147,6250),
        3:S.Rational(83961,200000),4:-S.Rational(3501,3125)}
for step,val in expect.items():
    assert S.factor((h*G).subs({h:step,q:qw,ell:ellw})-val)==0
# Isolate all three positive roots via exact rational Sturm sign alternations.
poly=S.Poly(Gw,h)
intervals=[(S.Rational(189,100),S.Rational(190,100)),
           (S.Rational(226,100),S.Rational(227,100)),
           (S.Rational(369,100),S.Rational(370,100))]
for lo,hi in intervals:
    assert poly.eval(lo)*poly.eval(hi)<0
assert S.count_roots(poly,0,S.oo)==3
print('PASS: transfer determinant and spectral polynomial identities')
print('PASS: both discriminants and the exact cusp triple-root certificate')
print('PASS: sharp phase witness and three disjoint isolating intervals')
print('PASS: four rational stability/instability witnesses at steps 1,2,3,4')
print('CHECKS: 16 exact identity/root-group assertions, plus 4 witness evaluations')
