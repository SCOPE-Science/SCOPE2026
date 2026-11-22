"""Symbolic algebraic and finite-matrix checks for a two-stage Radau pressure operator.

Run: python checker.py
Dependencies: sympy, numpy
Finite checks supplement the unrestricted-dimension proof, not replace it.
"""
from itertools import product
import numpy as np
import sympy as sp

A = sp.Matrix([[sp.Rational(5,12), -sp.Rational(1,12)],
               [sp.Rational(3,4), sp.Rational(1,4)]])
B = A.inv()
C = B * B
D = sp.diag(9,1)
S = sp.diag(3,1)
a,b,r = sp.symbols('a b r', positive=True, real=True)
assert B == sp.Matrix([[sp.Rational(3,2),sp.Rational(1,2)],
                       [-sp.Rational(9,2),sp.Rational(5,2)]])
assert C == sp.Matrix([[0,2],[-18,4]])
assert sp.simplify((D*B+B.T*D)/2 - sp.diag(sp.Rational(27,2),sp.Rational(5,2))) == sp.zeros(2)
assert sp.simplify((D*C+C.T*D)/2 - sp.diag(0,4)) == sp.zeros(2)
N = a*B+b*C
H = (N+N.T)/2
assert sp.simplify(H.det() + (a*a+104*a*b+256*b*b)/4) == 0
Q = S*N*S.inv()
Hs = (Q+Q.T)/2
T = (Q-Q.T)/2
assert sp.simplify(Hs-sp.diag(sp.Rational(3,2)*a,sp.Rational(5,2)*a+4*b)) == sp.zeros(2)
assert sp.simplify(T-sp.Matrix([[0,sp.Rational(3,2)*a+6*b],[-sp.Rational(3,2)*a-6*b,0]])) == sp.zeros(2)
k2 = 3*(r+4)**2/(r*(5*r+8))
assert sp.simplify(sp.diff(k2,r) + 96*(r+4)*(r+1)/(r*r*(5*r+8)**2)) == 0
assert sp.simplify((sp.Rational(3,2)*(r+4))**2 / ((sp.Rational(3,2)*r)*(sp.Rational(5,2)*r+4))-k2) == 0

cases = 0
rng = np.random.default_rng(1129)
Bf = np.array(B,float); Cf=np.array(C,float)
for n in (1,2,3,5):
    for ia in range(5):
        Z = rng.integers(-3,4,size=(n,n)).astype(float)
        Y = rng.integers(-3,4,size=(n,n)).astype(float)
        P = Z.T @ Z + np.eye(n)*(1.0+0.3*ia)
        Qp = Y.T @ Y + np.eye(n)*(1.2+0.2*ia)
        for alpha,beta in product((0.01,0.6,3.0),(0.05,1.5)):
            L = alpha*np.kron(Bf,P)+beta*np.kron(Cf,Qp)
            Weight=np.kron(np.diag([9.,1.]), np.eye(n))
            Hweighted=(Weight@L+L.T@Weight)/2
            Htarget=np.block([[13.5*alpha*P, np.zeros((n,n))],[np.zeros((n,n)),2.5*alpha*P+4*beta*Qp]])
            assert np.allclose(Hweighted,Htarget, atol=3e-11)
            eigw=np.linalg.eigvalsh(Hweighted-1.5*alpha*np.linalg.eigvalsh(P)[0]*Weight)
            assert eigw.min()>-2e-10
            Si=np.kron(np.diag([3.,1.]), np.eye(n))
            Nt=Si@L@np.linalg.inv(Si)
            Ht=(Nt+Nt.T)/2
            St=(Nt-Nt.T)/2
            d,U=np.linalg.eigh(Ht)
            assert d.min()>0
            invroot=(U/d**0.5)@U.T
            herm_skew = 1j*invroot@St@invroot
            computed=np.linalg.norm(herm_skew,2)
            generalized_mu=np.linalg.eigvalsh(np.linalg.solve(np.linalg.cholesky(P), Qp)@np.linalg.inv(np.linalg.cholesky(P).T))[-1]
            rr=alpha/(beta*generalized_mu)
            expected=np.sqrt(3*(rr+4)**2/(rr*(5*rr+8)))
            assert abs(computed-expected)<1e-9, (n,alpha,beta,computed,expected)
            # Unweighted Hermitian part has a strictly negative direction.
            He=(L+L.T)/2
            assert np.linalg.eigvalsh(He).min() < -1e-9
            cases+=1
print('PASS: symbolic matrix identities and %d finite SPD matrix cases'%cases)
