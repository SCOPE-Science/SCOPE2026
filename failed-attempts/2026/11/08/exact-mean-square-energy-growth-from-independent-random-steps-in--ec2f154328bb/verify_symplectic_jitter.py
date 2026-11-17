"""Reproduce exact second-moment and small-jitter checks for random-step symplectic Euler.
No external data or dependencies beyond SymPy and NumPy.
"""
from fractions import Fraction
from itertools import product
import math
import numpy as np
import sympy as sp

h, e=sp.symbols('h e',real=True)
lam=sp.Symbol('lam')
def M(z):
    return sp.Matrix([[1-z*z,z],[-z,1]])
def coord(X):
    return sp.Matrix([X[0,0],X[0,1],X[1,1]])
B=(sp.Matrix([[1,0],[0,0]]),sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,0],[0,1]]))
def transfer(z):
    return sp.Matrix.hstack(*(coord(M(z)*F*M(z).T) for F in B))
T=sp.expand((transfer(h+e)+transfer(h-e))/2)
G=sp.Matrix([[1,-h/2],[-h/2,1]])
checks=0
assert sp.simplify(M(h).T*G*M(h)-G)==sp.zeros(2); checks+=1
assert sp.factor(M(h).det())==1;checks+=1
assert sp.simplify(T.charpoly(lam).as_expr().subs(lam,1) + 2*e**2*(h-e)**2*(h+e)**2)==0;checks+=1
S=G.inv()
D=sp.simplify((M(h+e)*S*M(h+e).T+M(h-e)*S*M(h-e).T)/2-S)
assert sp.simplify(sp.trace(G*D)-4*e**2*(h*h+e*e)/(4-h*h))==0;checks+=1
assert sp.factor(sp.trace(G*S))==2;checks+=1
for H in [sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4),sp.Rational(1),sp.Rational(5,4),sp.Rational(3,2),sp.Rational(7,4)]:
    for E in [sp.Rational(1,20),sp.Rational(1,10),sp.Rational(1,8)]:
        if not 0<H-E<H+E<2:continue
        Tf=np.array(T.subs({h:H,e:E}),float)
        rho=max(abs(np.linalg.eigvals(Tf)))
        assert rho>1+1.e-10
        checks+=1
# Exact iid propagation, independently enumerate all sequences.
for H,E in [(sp.Rational(1),sp.Rational(1,4)),(sp.Rational(2,3),sp.Rational(1,6))]:
    for initial in [sp.Matrix([1,0]),sp.Matrix([0,1]),sp.Matrix([2,3])]:
        u=coord(initial*initial.T)
        for k in range(1,8):
            v=sp.zeros(3,1)
            for signs in product([-1,1],repeat=k):
                x=initial
                for sign in signs:
                    x=M(H+sign*E)*x
                v+=coord(x*x.T)/2**k
            target=T.subs({h:H,e:E})**k*u
            assert v==target
            checks+=1
# Independent numerical check of the perturbation coefficient.
for H in [0.3,0.6,1.0,1.25,1.5,1.9]:
    eps=0.001
    eig=np.linalg.eigvals(np.array(T.subs({h:H,e:eps}),float))
    rho=max(abs(eig))
    coeff=2*H*H/(4-H*H)
    assert abs((rho-1)/eps**2-coeff) < 0.006
    checks+=1
H,E=sp.Integer(1),sp.Rational(1,4)
poly=sp.factor(T.subs({h:H,e:E}).charpoly(lam).as_expr());assert sp.simplify(poly- (2048*lam**3-264*lam**2-441*lam-1568)/2048)==0;checks+=1
print(f'PASS {checks} exact/symbolic/numeric checks')
print('Example characteristic polynomial:',poly)
print('Example Perron root:',max(abs(v) for v in np.linalg.eigvals(np.array(T.subs({h:H,e:E}),float))))
print('Exact general sign certificate: det(I-T) = -2 e^2 (h-e)^2 (h+e)^2')
print('Perturbation coefficient: 2 h^2/(4-h^2)')
