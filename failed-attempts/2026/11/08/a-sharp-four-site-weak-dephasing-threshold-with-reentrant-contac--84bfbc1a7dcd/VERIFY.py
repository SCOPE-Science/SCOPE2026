#!/usr/bin/env python3
"""Exact four-site current differentiation and full Lindblad cross-check.

Run: python VERIFY.py
Dependencies: sympy, numpy, scipy (see requirements.txt).
"""
import sympy as sp
import numpy as np
from scipy.sparse import csc_matrix, eye, kron
from scipy.sparse.linalg import spsolve


def polynomial(x,y):
    return (-48*x*(x+4)**2
       +(x**4+32*x**3-96*x**2+1408*x+8960)*y
       +(50*x**3+1008*x**2+2464*x+21888)*y**2
       +(913*x**2+8016*x+37296)*y**3
       +(7200*x+13824)*y**4+20736*y**5)


def exact_algebra():
    u,z,G,t=sp.symbols('u z G t', real=True)
    h=sp.diag(0,u,2*u,3*u)
    for i in range(3):h[i,i+1]=h[i+1,i]=t
    E=sp.diag(1,0,0,1)
    B=G*sp.diag(1,0,0,-1)/2
    diag=sp.symbols('a0:4', real=True)
    pairs={(i,j):(sp.Symbol(f'r{i}{j}',real=True),sp.Symbol(f'i{i}{j}',real=True)) for i in range(4) for j in range(i+1,4)}
    K=sp.zeros(4)
    for i in range(4):K[i,i]=diag[i]
    for (i,j),(re,im) in pairs.items():K[i,j]=re+sp.I*im;K[j,i]=re-sp.I*im
    off=K-sp.diag(*[K[i,i] for i in range(4)])
    F=-sp.I*(h*K-K*h)-G*(E*K+K*E)/2-z*off+B
    unknown=list(diag)+[a for tup in pairs.values() for a in tup]
    equations=[sp.expand(F[i,i]) for i in range(4)]
    for (i,j) in pairs:
        equations.extend([sp.re(sp.expand_complex(F[i,j])),sp.im(sp.expand_complex(F[i,j]))])
    A,b=sp.linear_eq_to_matrix(equations,unknown)
    A0=A.subs(z,0)
    inverse=A0.inv(method='DM')
    v0=inverse*b
    v1=-inverse*(A.diff(z)*v0)
    idx=unknown.index(pairs[(0,1)][1])
    current0=sp.factor(4*t*v0[idx])
    # Off-diagonal Lindblad decay z=2 gamma, hence d/dgamma=2 d/dz.
    slope0=sp.factor(8*t*v1[idx])
    den1=(G**2+4*t**2+16*u**2)
    den2=(4*G**2*t**2+G**2*u**2+16*t**4+12*t**2*u**2+9*u**4)
    expected_current=16*G*t**4*(G**2+4*t**2+9*u**2)/(den1*den2)
    x=G**2/t**2;y=u**2/t**2
    expected_slope=8*polynomial(x,y)/((x+4+16*y)**2*(4*x+x*y+16+12*y+9*y*y)**2)
    assert sp.cancel(current0-expected_current)==0
    assert sp.cancel(slope0-expected_slope)==0
    # Verify the polynomial in y has strictly positive coefficients for x>0.
    X,Y=sp.symbols('X Y',real=True)
    Q=sp.Poly(polynomial(X,Y),Y)
    assert sp.expand(Q.coeff_monomial(Y**0)+48*X*(X+4)**2)==0
    assert sp.expand(Q.coeff_monomial(Y)- (X**4+32*X*(X**2-3*X+44)+8960))==0
    for k in [2,3,4,5]:
        assert all(c>0 for c in sp.Poly(Q.coeff_monomial(Y**k),X).all_coeffs())
    assert sp.Rational(768,8960)==sp.Rational(3,35)
    return current0,slope0


def full_lindblad(current0,slope0):
    # Completely independent Hilbert-space calculation on the 16-dimensional space.
    n=4;dim=2**n;t=1.;u=1.;G=1.;f=.12
    X=csc_matrix(np.array([[0,1],[1,0]],complex))
    Y=csc_matrix(np.array([[0,-1j],[1j,0]],complex))
    Z=csc_matrix(np.diag([1,-1]).astype(complex))
    I=eye(2,dtype=complex,format='csc')
    def site(k,mat):
        a=mat if k==0 else I
        for j in range(1,n):a=kron(a,mat if j==k else I,format='csc')
        return a
    xx=[site(i,X) for i in range(n)]
    yy=[site(i,Y) for i in range(n)]
    zz=[site(i,Z) for i in range(n)]
    plus=[(xx[i]+1j*yy[i])/2 for i in range(n)]
    minus=[(xx[i]-1j*yy[i])/2 for i in range(n)]
    H=csc_matrix((dim,dim),dtype=complex)
    for i in range(n-1):H+=t/2*(xx[i]@xx[i+1]+yy[i]@yy[i+1])
    for i in range(n):H+=u*i*zz[i]/2
    Ix=t*(xx[0]@yy[1]-yy[0]@xx[1])
    exact0=float(current0.subs({sp.Symbol('G',real=True):G,sp.Symbol('t',real=True):t,sp.Symbol('u',real=True):u}))*f
    exact1=float(slope0.subs({sp.Symbol('G',real=True):G,sp.Symbol('t',real=True):t,sp.Symbol('u',real=True):u}))*f
    def current(gamma):
        jumps=[np.sqrt(G*(1+f)/2)*plus[0],np.sqrt(G*(1-f)/2)*minus[0],
               np.sqrt(G*(1-f)/2)*plus[-1],np.sqrt(G*(1+f)/2)*minus[-1]]
        jumps.extend(np.sqrt(gamma/2)*a for a in zz)
        eyeD=eye(dim,dtype=complex,format='csc')
        L=-1j*(kron(eyeD,H)-kron(H.T,eyeD))
        for a in jumps:
            a2=a.conjugate().T@a
            L+=kron(a.conjugate(),a)-.5*kron(eyeD,a2)-.5*kron(a2.T,eyeD)
        L=L.tolil();ix=[i+i*dim for i in range(dim)]
        L[0,:]=0;L[0,ix]=1
        b=np.zeros(dim*dim,dtype=complex);b[0]=1
        rho=spsolve(L.tocsc(),b).reshape((dim,dim),order='F')
        assert np.max(np.abs(rho-rho.conjugate().T))<1e-10
        return float(np.real(np.trace(Ix@rho)))
    assert abs(current(0)-exact0)<1e-10
    h=1e-5
    assert abs((current(h)-current(0))/h-exact1)<1e-4
    for gam in [0.01,.3,1.0]:
        # Compare a direct 16x16 one-particle correlation solve at nonzero gamma.
        hmat=np.diag(np.arange(4)*u)+np.diag(np.ones(3)*t,1)+np.diag(np.ones(3)*t,-1)
        E=np.diag([1,0,0,1]);inj=G*np.diag([1,0,0,-1])/2
        def F(K):return -1j*(hmat@K-K@hmat)-G/2*(E@K+K@E)-2*gam*(K-np.diag(np.diag(K)))
        mat=np.column_stack([F(np.eye(16,dtype=complex)[j].reshape(4,4)).flatten() for j in range(16)])
        kk=np.linalg.solve(mat,-inj.flatten()).reshape(4,4)
        approx=f*4*t*kk[0,1].imag
        assert abs(current(gam)-approx)<2e-11
    return True

if __name__=='__main__':
    curr,deriv=exact_algebra()
    assert full_lindblad(curr,deriv)
    print('PASS: exact sixteen-equation symbolic identities; polynomial sign; independent full four-spin Lindblad checks')
