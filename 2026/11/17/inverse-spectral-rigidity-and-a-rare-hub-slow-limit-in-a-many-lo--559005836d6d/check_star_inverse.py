#!/usr/bin/env python3
"""Reproduce determinant identities, inverse spectral polynomial, and slow limit."""
import numpy as np
import sympy as s
from scipy.linalg import expm

def matrix(a, eps):
    a=np.asarray(a,dtype=float); r=len(a); A=np.mean(a)
    M=np.zeros((r+1,r+1));M[0,0]=(1-eps)*A
    M[0,1:]=-(1-eps)*a/r;M[1:,0]=-eps*a
    M[np.arange(1,r+1),np.arange(1,r+1)]=eps*a
    return M

def inverse(eig,eps,r):
    roots=np.asarray(eig)/eps
    coef=np.poly(roots)  # highest power first, monic
    c=eps*coef
    for j in range(r+1):
        k=r-j
        c[j]/=1-(1-eps)*k/r
    return np.roots(c),c

alpha=[s.Rational(1,5),s.Rational(2,3),s.Rational(9,10),s.Rational(1,3)]
eps=s.Rational(3,10)
r=len(alpha);A=sum(alpha)/r;z=s.symbols('z'); t=s.symbols('t')
L=s.zeros(r+1)
L[0,0]=(1-eps)*A
for i,a in enumerate(alpha,1):
    L[0,i]=-(1-eps)*a/r;L[i,0]=-eps*a;L[i,i]=eps*a
P=s.prod(z-a for a in alpha)
R=s.expand(P-(1-eps)*z*s.diff(P,z)/r)
assert s.simplify(L.charpoly(t).as_expr().subs(t,eps*z)-eps**r*z*R)==0
print('SYMBOLIC_DETERMINANT_OK',str(s.factor(R)))
for al in [[.2,.75],[.14,.31,.52],[.18,.39,.66,.88],[.2,.2,.7,.9]]:
 for e in [.025,.15,.4,.8]:
    # similarity S L S^{-1} with S=diag(sqrt(c)); eigen real. Direct eigvals more robust here.
    vals=np.sort(np.real(np.linalg.eigvals(matrix(al,e))))[1:]
    rec,_=inverse(vals,e,len(al))
    assert np.max(np.abs(np.sort(np.real(rec))-np.sort(al))) <3e-6,(al,e,rec)
print('FINITE_SPECTRAL_INVERSION_OK')

al=np.array([.2,.53,.87,.94]); r=len(al);A=al.mean(); Q=-np.diag(al)+np.outer(al,al)/al.sum()
assert np.max(np.abs(Q-Q.T))<1e-14 and np.max(np.abs(Q.sum(axis=1)))<1e-14
mu=np.sort(np.linalg.eigvalsh(-Q))[1:]
assert np.all(mu>np.sort(al)[:-1]) and np.all(mu<np.sort(al)[1:])
print('SLOW_INTERLACING_OK',mu)
init=np.array([.1,.8,.3,.95]);hub=.73
for e in [.04,.02,.01,.005]:
    Pfull=np.eye(r+1)-matrix(al,e)
    x=np.array([hub,*init]); nmax=int(round(3/e)); checkpoints=[int(round(t/e)) for t in [0,.5,1,2,3]]
    dif=[]; qerr=[]
    for n in range(nmax+1):
        if n in checkpoints:
            pred=expm((e*n)*Q)@init
            dif.append(float(np.max(np.abs(x[1:]-pred))))
        x=Pfull@x
    print('SLOW_LIMIT_TEST',e,'max_at_sampled_times',max(dif))
    assert max(dif) <= 8*e
print('RARE_HUB_INVERSE_AND_SLOW_LIMIT_OK')
