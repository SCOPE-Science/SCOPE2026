"""Reproducible algebra and independent Liouvillian verification of mixed-noise two-qubit resetting.
Dependencies: Python 3.10+, sympy, numpy. Run: python checker.py
"""
import sympy as sp
import numpy as np
from numpy.linalg import solve, eigvalsh

r,a,b,J=sp.symbols('r a b J',positive=True,real=True)
A=r*(r+2*b)+4*J**2
B=(r+2*a)*(r+2*a+2*b)+4*J**2
p=r*(r+2*b)/A
h=r*(r+2*a+2*b)/B
q=J*r/A
k=J*r/B
z=(p+h)/2
w=(p-h)/2
se=(r+a)/(r+2*a)
so=a/(r+2*a)
F=sp.factor((q+k)**2-so**2+w**2)
G=sp.factor((q-k)**2-se**2+z**2)
P=sp.factor(sp.cancel(F*((r+2*a)*A*B)**2/(4*J**2)))
Q=sp.factor(sp.cancel(-G*((r+2*a)*A*B)**2/(8*J**2)))
assert sp.simplify(F-4*J**2*P/((r+2*a)*A*B)**2)==0
assert sp.simplify(G+8*J**2*Q/((r+2*a)*A*B)**2)==0
assert sp.degree(P,r)==8
assert sp.degree(Q,r)==8
# Every monomial coefficient in Q is strictly positive after collecting in r,a,b,J.
for coeff in sp.Poly(Q,r).all_coeffs():
    terms=sp.Poly(sp.expand(coeff),a,b,J).coeffs()
    assert terms and all(c>0 for c in terms),coeff

# Polynomial P sign structure and the explicit delicate P3/P4 sign implication.
cs=[sp.factor(sp.Poly(P,r).nth(i)) for i in range(9)]
assert all(sp.Poly(-cs[i],a,b,J).coeffs() and all(c>0 for c in sp.Poly(-cs[i],a,b,J).coeffs()) for i in range(3))
assert all(all(c>0 for c in sp.Poly(cs[i],a,b,J).coeffs()) for i in range(5,9))
assert sp.factor(cs[0]+64*a*a*J*J*(a*a+a*b+J*J)**2)==0
assert sp.factor(cs[8]-1)==0
b3=-cs[3]/(16*a)
b4=-cs[4]/4
assert sp.simplify(b4-b3-(a**4-2*a**3*b-10*a*a*b*b-2*a*b**3-(20*a*a+18*a*b)*J*J))==0
# B3(t) strictly positive for t <= a^2/20 by monotonicity in t and positive coefficients at the boundary.
small=sp.expand(b3.subs(J**2,a*a/20))
assert all(c>0 for c in sp.Poly(small,a,b).coeffs())
assert sp.factor(sp.diff(b3,J)/J+6*a*a+4*a*b+16*J*J)==0
# Thus P3>=0 entails J^2>a^2/20 and P4>0, so there is exactly one sign change by Descartes.
assert sp.limit(r*(q+k-sp.sqrt(so*so-w*w)),r,sp.oo)==2*J

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],dtype=complex)
Z=np.array([[1,0],[0,-1]],dtype=complex)
Y=np.array([[0,-1j],[1j,0]],dtype=complex)
XX=np.kron(X,X); X1=np.kron(X,I); Z2=np.kron(I,Z);YY=np.kron(Y,Y)
initial=np.zeros((4,4),dtype=complex);initial[0,0]=1

def independent_stationary(rv,av,bv,jv):
    H=jv*XX
    M=np.zeros((16,16),dtype=complex)
    for i in range(4):
        for j in range(4):
            E=np.zeros((4,4),dtype=complex);E[i,j]=1
            dE=-1j*(H@E-E@H)+av*(X1@E@X1-E)+bv*(Z2@E@Z2-E)
            M[:,4*i+j]=dE.reshape(16)
    return solve(rv*np.eye(16)-M,rv*initial.reshape(16)).reshape((4,4))

def predicted(rv,av,bv,jv):
    den0=rv*(rv+2*bv)+4*jv*jv
    den1=(rv+2*av)*(rv+2*av+2*bv)+4*jv*jv
    pp=rv*(rv+2*bv)/den0
    hh=rv*(rv+2*av+2*bv)/den1
    qq=jv*rv/den0
    kk=jv*rv/den1
    zz=(pp+hh)/2
    ww=(pp-hh)/2
    even=(rv+av)/(rv+2*av)
    odd=av/(rv+2*av)
    rho=np.zeros((4,4),dtype=complex)
    rho[0,0]=(even+zz)/2
    rho[3,3]=(even-zz)/2
    rho[1,1]=(odd-ww)/2
    rho[2,2]=(odd+ww)/2
    rho[0,3]=1j*(qq+kk)/2
    rho[3,0]=np.conjugate(rho[0,3])
    rho[1,2]=1j*(kk-qq)/2
    rho[2,1]=np.conjugate(rho[1,2])
    return rho

def direct_concurrence(rho):
    flip=YY@rho.conjugate()@YY
    vals=np.sort(np.sqrt(np.maximum(np.real(np.linalg.eigvals(rho@flip)),0)))[::-1]
    return max(0.,vals[0]-sum(vals[1:]))

def x_concurrence(rho):
    return 2*max(0.,abs(rho[0,3])-np.sqrt(rho[1,1].real*rho[2,2].real),abs(rho[1,2])-np.sqrt(rho[0,0].real*rho[3,3].real))

rng=np.random.default_rng(804111)
count=0
for sample in range(130):
    av,bv,jv,rv=10**rng.uniform(-1.8,1.8,size=4)
    ro=independent_stationary(rv,av,bv,jv)
    ra=predicted(rv,av,bv,jv)
    assert np.max(abs(ro-ra))<2e-11
    assert abs(np.trace(ro)-1)<1e-11
    assert min(eigvalsh(ro))>-1e-11
    assert abs(direct_concurrence(ro)-x_concurrence(ra))<1e-9
    count+=4

# Sign/uniqueness: numeric root counts for positive parameter samples corroborate, but do not prove, Descartes.
for sample in range(120):
    av,bv,jv=10**rng.uniform(-2,2,size=3)
    c=np.array([float(v.subs({a:av,b:bv,J:jv})) for v in cs])
    roots=np.roots(c[::-1])
    positive=[v.real for v in roots if v.real>0 and abs(v.imag)<2e-5*max(1.,abs(v.real))]
    assert len(positive)==1,(av,bv,jv,roots)
    cross=positive[0]
    low=predicted(cross*.5,av,bv,jv)
    high=predicted(cross*2,av,bv,jv)
    assert direct_concurrence(low)<1e-8
    assert direct_concurrence(high)>0
    count+=3
print('PASS: symbolic coefficient certificate, one-crossing argument, independent 16x16 master equation and direct concurrence; numeric assertions:',count)
