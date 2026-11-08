#!/usr/bin/env python3
"""Standalone symbolic and matrix checks for the Bell-reset CHSH phase theorem.
Run: python checker.py (requires sympy, numpy, scipy).
These tests corroborate, but do not replace, the analytic all-parameter proof.
"""
import sympy as sp
import numpy as np
from numpy.linalg import solve, eigvalsh
from scipy.optimize import brentq

x,b=sp.symbols('x b',positive=True)
u=x/(x+b)
v=(x*x+x+2)/((x+1)*(x+2))
P=x**5+2*x**4+(5-8*b)*x**3+(4-4*b*b-16*b)*x**2+(4-8*b*b-16*b)*x-8*b*b
assert sp.simplify((1-u*u-v*v)+x*P/((x+b)**2*(x+1)**2*(x+2)**2))==0
assert sp.simplify((1-2*u*u)-(b*b+2*b*x-x*x)/(x+b)**2)==0
assert sp.simplify(sp.diff(v,x)-2*(x*x-2)/((x+1)**2*(x+2)**2))==0
assert sp.expand(2*(x*x+x+2)**2-((x+1)*(x+2))**2-(x**4-2*x**3-3*x**2-4*x+4))==0
assert sp.factor((x+1)*(x+2)-(x+b))==x*x+2*x+2-b
checks=5
I2=np.eye(2,dtype=complex)
sm=np.array([[0,1],[0,0]],dtype=complex)
Z=np.diag([1,-1]).astype(complex)
minus=[np.kron(sm,I2),np.kron(I2,sm)]
zops=[np.kron(Z,I2),np.kron(I2,Z)]
I4=np.eye(4,dtype=complex)
phi=np.array([1,0,0,1],dtype=complex)/np.sqrt(2)
rho0=np.outer(phi,phi.conj())
vec0=rho0.reshape(16,order='F')

def generator(g,k):
    G=np.zeros((16,16),dtype=complex)
    for A in minus:
        L=np.sqrt(g)*A
        Q=L.conj().T@L
        G+=np.kron(L.conj(),L)-0.5*(np.kron(I4,Q)+np.kron(Q.T,I4))
    for A in zops:
        L=np.sqrt(k)*A
        Q=L.conj().T@L
        G+=np.kron(L.conj(),L)-0.5*(np.kron(I4,Q)+np.kron(Q.T,I4))
    return G

def closed_form(rate,g,k):
    X=rate/g; B=1+4*k/g
    q=X/(2*(X+1)*(X+2))
    c=X/(2*(X+B))
    w=rate/(2*(rate+2*g))
    R=np.zeros((4,4),dtype=complex)
    R[0,0]=1-2*q-w
    R[1,1]=R[2,2]=q
    R[3,3]=w
    R[0,3]=R[3,0]=c
    return R

def chsh_direct(R):
    pauli=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),Z]
    T=np.array([[np.trace(R @ np.kron(A,B)).real for B in pauli] for A in pauli])
    evals=np.sort(eigvalsh(T.T@T))[::-1]
    return 2*np.sqrt(evals[0]+evals[1]),T

def concurrence_direct(R):
    Y=np.array([[0,-1j],[1j,0]],complex)
    flip=np.kron(Y,Y)@R.conj()@np.kron(Y,Y)
    ew=np.linalg.eigvals(R@flip)
    zz=np.sqrt(np.sort(np.clip(ew.real,0,None))[::-1])
    return max(0,float(zz[0]-sum(zz[1:])))

for g in [0.4,1.,2.7]:
  for k in [0.,0.03,0.2,1.,10.]:
    G=generator(g,k)
    for rate in [0.008,0.12,0.6,1.5,4.,25.]:
        R=solve(rate*np.eye(16)-G,rate*vec0).reshape((4,4),order='F')
        F=closed_form(rate,g,k)
        assert np.max(np.abs(R-F))<2e-12
        X=rate/g;B=1+4*k/g
        chi,T=chsh_direct(R)
        expected=2*np.sqrt(float((u*u+sp.Max(u*u,v*v)).subs({x:X,b:B})))
        assert abs(chi-expected)<2e-10
        assert abs(concurrence_direct(R)-max(0, X*(X*X+2*X+2-B)/((X+B)*(X+1)*(X+2))))<2e-10
        assert np.min(eigvalsh(R))>-2e-12
        checks+=4

# Exact rational single-particle generator tests, independently of the closed formula.
for g,k,rate in [(sp.Rational(1),sp.Rational(0),sp.Rational(1,3)),
                 (sp.Rational(3,2),sp.Rational(1,5),sp.Rational(7,4)),
                 (sp.Rational(2,3),sp.Rational(5,4),sp.Rational(11,7))]:
    N=sp.zeros(16,16)
    M=sp.eye(2)
    smS=sp.Matrix([[0,1],[0,0]])
    zS=sp.diag(1,-1)
    ops=[(sp.kronecker_product(smS,M),g),(sp.kronecker_product(M,smS),g),
         (sp.kronecker_product(zS,M),k),(sp.kronecker_product(M,zS),k)]
    for L,c in ops:
        Q=L.T*L
        N+=c*(sp.kronecker_product(L,L)-sp.Rational(1,2)*(sp.kronecker_product(sp.eye(4),Q)+sp.kronecker_product(Q.T,sp.eye(4))))
    v0=sp.zeros(16,1)
    v0[0]=v0[3]=v0[12]=v0[15]=sp.Rational(1,2)
    exact=(rate*sp.eye(16)-N).inv()*(rate*v0)
    X=rate/g;B=1+4*k/g
    Q=X/(2*(X+1)*(X+2));C=X/(2*(X+B));W=rate/(2*(rate+2*g))
    expected=sp.zeros(16,1)
    for ix,val in [(0,1-2*Q-W),(5,Q),(10,Q),(15,W),(3,C),(12,C)]: expected[ix]=val
    assert exact==expected
    checks+=1

# Threshold root uniqueness and branch selection corroboration on a diverse grid.
x0=brentq(lambda y: float(v.subs(x,y)-1/np.sqrt(2)),2.,5.)
b0=x0/(1+np.sqrt(2))
assert 1<b0<1.4
for B in [1,1.01,1.1,1.2,b0,1.4,2,3,10,100,1000,1e6]:
    fun=lambda xx: float(P.subs({x:xx,b:B}))
    xi=brentq(fun,1e-12,max(10000.,20*B+100))
    thresh=min(xi,B*(1+np.sqrt(2)))
    if B<=b0-1e-7: assert abs(thresh-B*(1+np.sqrt(2)))<1e-6
    if B>=b0+1e-7: assert abs(thresh-xi)<1e-6
    for fac in [0.01,0.1,0.3,0.7,0.999,1.001,1.01,1.3,3.,10.]:
        xx=fac*thresh
        uv=float(u.subs({x:xx,b:B}));vv=float(v.subs(x,xx))
        CH=uv*uv+max(uv*uv,vv*vv)
        assert (CH>1)==(fac>1)
        checks+=1
assert abs(x0-3.20425757804585)<1e-10
assert abs(b0-1.327)<0.01
for B in [1e3,1e4,1e6]:
    xi=brentq(lambda xx:float(P.subs({x:xx,b:B})),0.001,20*B)
    assert abs(xi/B**(2/3)-4**(1/3))<0.17
    checks+=1
print(f'PASS: {checks} symbolic, independent Lindbladian, concurrence, CHSH and phase assertions')
print(f'critical x0={x0:.12f}, b0={b0:.12f}')
