#!/usr/bin/env python3
"""Exact algebraic checks for a three-node Fourier Gram minimax theorem."""
import sympy as s

u=s.symbols('u',real=True)
r=s.sqrt(3)
I=s.I
omega=(-1+I*r)/2
F=s.Matrix([[omega**(j*k)/r for k in range(3)] for j in range(3)])
epsilon=s.Matrix([0,u,1])
dF=s.Matrix([[I*j*epsilon[k]*F[j,k] for k in range(3)] for j in range(3)])
H=s.simplify(F.conjugate().T*(dF*F.conjugate().T+F*dF.conjugate().T)*F)
P=s.diag(1,(1+I*r)/2,omega)
B=s.Matrix([[0,u,1],[u,0,1-u],[1,1-u,0]])
Htarget=B/r

def ck(test, message):
    if not test: raise AssertionError(message)

def zero(M):
    return all(s.simplify(s.expand_complex(v))==0 for v in M)

ck(zero(F*F.conjugate().T-s.eye(3)), 'DFT normalization')
ck(zero(P.conjugate().T*H*P-Htarget), 'node derivative and phase gauge')
d=s.Matrix([s.Rational(1,3)-u,s.Rational(1,3),u-s.Rational(2,3)])
S=B+s.diag(*d)
ck(s.simplify(sum(d))==0,'zero-sum weight variation')
ck(zero(S*s.ones(3,1)-s.Rational(4,3)*s.ones(3,1)), 'balanced eigenvector')
l=s.symbols('lambda')
char=s.factor(S.charpoly(l).as_expr())
ck(s.simplify(char-(l-s.Rational(4,3))*(l*l+s.Rational(4,3)*l-3*u*u+3*u-s.Rational(5,9)))==0,'characteristic polynomial')
for v in [s.Rational(1,4),s.Rational(1,2),s.Rational(3,4)]:
    Sv=S.subs(u,v)
    eigen=[x for e,m in Sv.eigenvals().items() for x in [e]*m]
    ck(any(s.simplify(x-s.Rational(4,3))==0 for x in eigen), 'Perron eigenvalue')
    ck(all(abs(float(x))<=s.Rational(4,3)+1e-9 for x in eigen), 'feasible spectral upper bound')
# Midpoint example, exact characteristic polynomial and Frobenius comparison
mid=B.subs(u,s.Rational(1,2))
ck(s.simplify(mid.charpoly(l).as_expr()-(l+1)*(l*l-l-s.Rational(1,2)))==0, 'unweighted eigenvalues')
midopt=S.subs(u,s.Rational(1,2))
ck(s.simplify(sum(x*x for x in mid)/3-1)==0, 'unweighted Frobenius norm')
ck(s.simplify(sum(x*x for x in midopt)/3-s.Rational(19,18))==0, 'weighted Frobenius norm')
ck(s.simplify(s.factor((u-s.Rational(1,2))**2)-(u**2-u+s.Rational(1,4)))==0,'centering')
roots=s.solve(27*u*(1-u)-5,u)
ck(len(roots)==2 and all(s.simplify(roots[i]-(9+(-1 if i==0 else 1)*s.sqrt(21))/18)==0 for i in range(2)),'sharp transition')
# Separate sharp spectral half-spread: symmetric endpoint loading at u=1/2
spreadopt=mid+s.diag(s.Rational(1,4),-s.Rational(1,2),s.Rational(1,4))
ck(s.simplify(spreadopt.charpoly(l).as_expr()-(l-s.Rational(3,2))*(l+s.Rational(3,4))**2)==0,'spectral spread optimizer spectrum')
ck(s.simplify(sum(x*x for x in spreadopt)/3-s.Rational(9,8))==0,'spread optimizer Frobenius norm')
a=s.symbols('a',real=True)
sym=mid+s.diag(a,-2*a,a)
ck(s.simplify(sym.charpoly(l).as_expr()- (l-(a-1))*(l*l+(a-1)*l+(-2*a*(a+1)-s.Rational(1,2))))==0,'symmetric reduction characteristic')
ck(s.simplify((1+3*a)**2+2-(3-3*a)**2)==s.simplify(24*a-6),'spectral crossing at a=1/4')
# Two-state DFT: diagonal loading preserves or increases spectral norm
h,d2=s.symbols('h d2',real=True)
T=s.Matrix([[d2,h],[h,-d2]])
ck(s.factor(T.charpoly(l).as_expr())==l*l-h*h-d2*d2,'2-point spectral law')
# Direct positive-t small-step numerical check (supplementary, not the infinite proof)
import numpy as np
for rate in [0.00001,0.0001,0.001]:
    idx=np.arange(3)
    nodes=2*np.pi*idx/3+rate*np.array([0,.5,1.0])
    AA=np.exp(1j*np.outer(idx,nodes))
    z=(np.array([s.Rational(-1,6),s.Rational(1,3),s.Rational(-1,6)],dtype=float) /(3*np.sqrt(3)))
    v=np.ones(3)/3+rate*z
    gram=AA@np.diag(v)@AA.conj().T
    norm=np.linalg.norm(gram-np.eye(3),2)
    ck(abs(norm/rate-4/(3*np.sqrt(3)))<0.002,'finite-step asymptotic')
print('VERIFY_OK symbolic_spectrum_phase_window_minimality')
