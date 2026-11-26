"""Exact symbolic certificate for the all-contrast stability boundary.

Run with Python 3 and SymPy. Checks algebra, not the real-root topology proof.
"""
import sympy as S

h, c, q, lam, eta, p = S.symbols('h c q lam eta p')
A, B = [(1 - h*(1 + i*c))**2 for i in (1, -1)]
det = S.expand(1 - (1+lam)*(A+B)/2 + lam*A*B)
G = S.cancel(det/h).subs(c**4, q**2).subs(c**2, q)
P = S.factor(S.discriminant(G, h)/(4*lam*(1-q)**2))
assert S.factor(S.discriminant(P, lam)) == S.factor(-256*q*(q-1)**3*(27*q*q-10*q-1)**3)
assert S.factor(P.subs(lam,-1)) == S.factor(-4*(q-1)**2*(2*q-1))
assert S.factor(P.subs(lam,0)) == (1+q)**3

old = (72*p-36)*eta**3 + (84-168*p)*eta**2 + (85*p-61)*eta + 14*(1-p)
assert S.expand(det.subs({h:7*eta/2, c:S.Rational(5,7), lam:2*p-1}) - eta*old) == 0

q0 = (5+2*S.sqrt(13))/27
l0 = (-17+4*S.sqrt(13))/3
assert S.simplify(G.subs({q:q0, lam:l0}) - l0*(1-q0)**2*(h-4/(3*(1-q0)))**3) == 0
q1 = (97+5*S.sqrt(745))/512
l1 = -(1+q1)/(S.Rational(5,16)+3*q1)
assert 0 < q1 < 1 and -1 < l1 < 0
d, s = S.Rational(5,4)/(1-q1), S.Rational(3,2)/(1-q1)
assert S.simplify(G.subs({q:q1, lam:l1}) - l1*(1-q1)**2*(h-s)*(h-d)**2) == 0

observed = [det.subs({h:i,c:S.Rational(7,10),lam:-S.Rational(19,20)}) for i in (1,2,3,4)]
assert observed == list(map(S.Rational, ['149481/200000','-147/6250','83961/200000','-3501/3125']))
print('Exact transfer, cusp, puncture, old-slice equivalence, and rational witness checked.')
