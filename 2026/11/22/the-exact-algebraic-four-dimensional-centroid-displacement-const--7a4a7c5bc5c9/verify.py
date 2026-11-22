"""Exact algebraic checks for the dimension-four centroid displacement constant.

Requires Python 3.10+ and SymPy (tested with the locally installed version).
Run: python verify.py
"""
import sympy as s

r, t, z = s.symbols('r t z')
I = [s.integrate(t**j * (1+(r-1)*t)**2, (t, 0, 1)) for j in range(3)]
assert all(s.cancel(x-y)==0 for x,y in zip(I, [
    (r**2+r+1)/3,
    (3*r**2+2*r+1)/12,
    (6*r**2+3*r+1)/30,
]))
A = r**2+r+1
B = 3*r**2+2*r+1
N = r**4+4*r**3+10*r**2+4*r+1
F = 3*N/(20*A*B)
Q = 7*r**6+48*r**5+53*r**4+24*r**3-3*r**2-8*r-1
assert s.cancel(I[2]/I[1]-I[1]/I[0]-F) == 0
assert s.cancel(s.diff(F, r)+3*Q/(20*A**2*B**2)) == 0
assert Q.subs(r, 0) == -1 and Q.subs(r, 1) == 120
# Exact signs at rational isolating bounds. Uniqueness on (0,infty)
# follows from the one Descartes sign change in Q.
a = s.Rational(4471055651627, 10**13)
b = s.Rational(4471055651628, 10**13)
assert Q.subs(r, a) < 0 and Q.subs(r, b) > 0
# Eliminate the optimal affine slope to characterize the exact constant.
P = 25000*z**6 - 105000*z**5 + 144000*z**4 - 70300*z**3 + 14160*z**2 - 1152*z + 27
R = s.resultant(Q, 20*z*A*B - 3*N, r)
assert s.factor(R/P) in (s.Integer(1769472000), s.Integer(-1769472000))
# Irreducibility over Q, certified by the finite-field reduction mod 113.
assert s.Poly(P, z, modulus=113).degree() == 6
assert s.Poly(P, z, modulus=113).is_irreducible
assert s.Poly(Q, r, modulus=113).degree() == 6
assert s.Poly(Q, r, modulus=113).is_irreducible
rho = s.nsolve(Q, s.Rational(45,100), prec=65)
d4 = s.N(F.subs(r, rho), 50)
assert s.Rational(189345,10**6) < d4 < s.Rational(189346,10**6)
assert abs(s.N(P.subs(z,d4),25)) < s.Rational(1,10**19)
print('D4 maximizing endpoint ratio:', s.N(rho, 30))
print('D4 sharp constant:', d4)
print('All exact identities, isolating signs, and modular irreducibility verified.')
