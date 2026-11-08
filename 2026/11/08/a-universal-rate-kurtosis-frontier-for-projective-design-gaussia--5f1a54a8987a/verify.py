#!/usr/bin/env python3
"""Exact algebraic checks for isotropic random-pair Gaussian-noise sampling.
Requires Python 3 and SymPy. This is not a substitute for the general proof.
"""
import sympy as S

eta, x, y = S.symbols('eta x y', real=True)
b = eta*(2-eta)
rho = 1-b/2
t4 = 1-b+S.Rational(3,8)*b*b
kurt = 3*b/(8-3*b)
assert S.simplify(t4-rho**2-b**2/8) == 0
assert S.simplify(1-t4-b*(8-3*b)/8) == 0
assert S.simplify(kurt-3*(1-rho)/(1+3*rho)) == 0
assert S.simplify((1-rho**2)/(1-t4)-1-b/(8-3*b)) == 0

I = S.eye(3)
v = S.Matrix([x, y, -x-y])
projectors = []
for i,j in [(0,1),(0,2),(1,2)]:
    z=I[:,i]-I[:,j]
    projectors.append(z*z.T/2)
A = [I-eta*P for P in projectors]
norm2 = v.dot(v)
assert S.simplify(sum((T*v).dot(T*v) for T in A)/3-rho*norm2)==0
assert S.simplify(sum(((T*v).dot(T*v))**2 for T in A)/3-t4*norm2**2)==0
# Projection design: the second and fourth moments of angles agree with Haar lines.
z = S.symbols('z',real=True)
assert S.simplify(sum((v.dot(P*v)) for P in projectors)/3-norm2/2)==0
assert S.simplify(sum((v.dot(P*v))**2 for P in projectors)/3-S.Rational(3,8)*norm2**2)==0

# Exact stationary 2nd and 4th moments under covariance calibration.
for et in [S.Rational(1,17),S.Rational(1,4),S.Rational(2,3),S.Integer(1),
           S.Rational(5,4),S.Rational(3,2),S.Rational(39,20)]:
    for s2 in [S.Rational(1,3),S.Integer(1),S.Rational(7,2)]:
        B=et*(2-et)
        R=1-B/2
        Q=(1-R)*s2
        T=1-B+3*B*B/8
        # Covariance QI/(1-R)=s2 I.
        assert S.cancel(Q/(1-R)-s2)==0
        M4=8*s2**2*(1-R**2)/(1-T)
        assert S.cancel(M4-T*M4-8*Q*R*(2*s2)-8*Q**2)==0
        one_dim_fourth=S.Rational(3,8)*M4
        assert S.cancel(one_dim_fourth/(s2**2)-3-3*B/(8-3*B))==0
        assert S.cancel(S.Rational(3,8)*M4-3*s2**2*(8-2*B)/(8-3*B))==0
        assert Q>0 and S.Rational(1,2)<=R<1 and 0<=kurt.subs(eta,et)<=S.Rational(3,5)

assert rho.subs(eta,1)==S.Rational(1,2)
assert kurt.subs(eta,1)==S.Rational(3,5)
assert S.cancel((8*S.Rational(1,1)*(1-rho**2)/(1-t4)).subs(eta,1)-S.Rational(48,5))==0
print('PASS: symbolic pair-projector isotropy, contraction, fourth moments, calibrated stationary moments, and Pareto identities')
print('PASS: 21 exact-rational parameter/covariance/moment regimes')
print('benchmark: eta=1, variance=1 => rho=1/2, E|X|^4=48/5, excess kurtosis=3/5')
