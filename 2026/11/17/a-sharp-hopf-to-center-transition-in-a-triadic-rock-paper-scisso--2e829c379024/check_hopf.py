#!/usr/bin/env python3
"""Exact symbolic checks for the higher-order cyclic replicator Hopf theorem.

Requires Python 3 and SymPy. Run: python check_hopf.py
All algebra is over exact rational coefficients and radicals.
"""
import sympy as sp

alpha, beta, a, b = sp.symbols('alpha beta a b', real=True)
X, Y, z, w = sp.symbols('X Y z w')
C, D = b + 1, 3 + 2*alpha - beta
critical_a = (1 + 4*b + beta - 2*alpha)/D

u = sp.Matrix([sp.Rational(1,3)+X/sp.sqrt(2)+Y/sp.sqrt(6),
               sp.Rational(1,3)-X/sp.sqrt(2)+Y/sp.sqrt(6),
               sp.Rational(1,3)-2*Y/sp.sqrt(6)])
A = sp.Matrix([[0,-C,a+1],[a+1,0,-C],[-C,a+1,0]])
B1 = sp.Matrix([[0,-C/2,(a+1)*beta/2],
                [-C/2,-C,0],[(a+1)*beta/2,0,(a+1)*alpha]])
B2 = sp.Matrix([[(a+1)*alpha,(a+1)*beta/2,0],
                [(a+1)*beta/2,0,-C/2],[0,-C/2,-C]])
B3 = sp.Matrix([[-C,0,-C/2],
                [0,(a+1)*alpha,(a+1)*beta/2],
                [-C/2,(a+1)*beta/2,0]])
fitness = A*u + sp.Matrix([(u.T*B*u)[0] for B in (B1,B2,B3)])
mean_fitness = (u.T*fitness)[0]
vector = [sp.expand(u[i]*(fitness[i]-mean_fitness)) for i in range(3)]
F = sp.expand((vector[0]-vector[1])/sp.sqrt(2))
G = sp.expand((vector[0]+vector[1]-2*vector[2])/sp.sqrt(6))

def equal(lhs, rhs):
    assert sp.simplify(sp.expand(lhs-rhs)) == 0, sp.factor(lhs-rhs)

jac = sp.Matrix([[sp.diff(F,X),sp.diff(F,Y)],
                 [sp.diff(G,X),sp.diff(G,Y)]]).subs({X:0,Y:0})
mu = -D*(a-critical_a)/18
Omega = sp.sqrt(3)*(2*a*alpha+a*beta+3*a+2*alpha+6*b+beta+9)/18
for i,j,target in [(0,0,mu),(1,1,mu),(0,1,-Omega),(1,0,Omega)]:
    equal(jac[i,j],target)

omega = sp.sqrt(3)*C*(10*alpha-beta+15)/(9*D)
equal(Omega.subs(a,critical_a),omega)

# Express the full quartic vector field as a polynomial in z=X+iY, w=X-iY.
P = sp.Poly(sp.expand((F+sp.I*G).subs(
    {X:(z+w)/2,Y:(z-w)/(2*sp.I)}, simultaneous=True)),z,w)
Q = C*(sp.sqrt(2)*(8*alpha+beta+15)+sp.I*sp.sqrt(6)*(1-beta))/(6*D)
R = C*((1-beta)/2-sp.I*sp.sqrt(3)*(alpha-beta)/3)/D
S = C*(2*sp.sqrt(2)*(alpha-beta)+sp.I*sp.sqrt(6)*(1-beta))/(4*D)
T = C*(2*sp.sqrt(2)*(alpha-beta)-sp.I*sp.sqrt(6)*(1-beta))/(4*D)
expected = {(1,0):sp.I*omega,(0,2):Q,(2,1):R,(4,0):S,(1,3):T}
assert set(P.monoms()) == set(expected)
for monom,coefficient in expected.items():
    equal(P.coeff_monomial(z**monom[0]*w**monom[1]).subs(a,critical_a),coefficient)

# The real quadratic Hopf correction vanishes, not merely at sampled values.
fxx = sp.diff(F,X,2).subs({X:0,Y:0})
fxy = sp.diff(F,X,Y).subs({X:0,Y:0})
fyy = sp.diff(F,Y,2).subs({X:0,Y:0})
gxx = sp.diff(G,X,2).subs({X:0,Y:0})
gxy = sp.diff(G,X,Y).subs({X:0,Y:0})
gyy = sp.diff(G,Y,2).subs({X:0,Y:0})
quadratic_correction = (fxy*(fxx+fyy)-gxy*(gxx+gyy)
                        -fxx*gxx+fyy*gyy)
equal(quadratic_correction.subs(a,critical_a),0)
lyapunov_radial = C*(1-beta)/(2*D)
equal((sp.diff(F,X,3)+sp.diff(F,X,Y,2)
       +sp.diff(G,X,2,Y)+sp.diff(G,Y,3)).subs(a,critical_a)/16,
      lyapunov_radial)

# Exact reversing involution: (X,Y)->(-X,Y) at beta=1.
endpoint = {beta:sp.Integer(1),a:critical_a.subs(beta,1)}
equal((F.subs(X,-X)-F).subs(endpoint),0)
equal((G.subs(X,-X)+G).subs(endpoint),0)

for aa in (sp.Rational(5,4),sp.Rational(3,2),sp.Integer(2)):
    for be in (sp.Rational(1,3),sp.Rational(1,2),sp.Integer(1)):
        for bb in (sp.Integer(1),sp.Integer(2)):
            if bb <= (2*aa-be-1)/4:
                continue
            subs = {alpha:aa,beta:be,b:bb}
            assert critical_a.subs(subs) > 0
            assert omega.subs(subs) > 0
            ell = lyapunov_radial.subs(subs)
            assert (ell > 0) if be < 1 else (ell == 0)

print('TRIADIC_RPS_HOPF_EXACT_OK jacobian=4 complex_coefficients=5')
print('TRIADIC_RPS_HOPF_EXACT_OK quadratic_correction=0 reversal=2')
print('TRIADIC_RPS_HOPF_EXACT_OK endpoint_and_parameter_samples=18')
