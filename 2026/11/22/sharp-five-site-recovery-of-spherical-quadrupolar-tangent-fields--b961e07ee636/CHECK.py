"""Independent checks for single-ring vector spherical-harmonic sampling."""
import numpy as np
import sympy as sp
from scipy.special import lpmv, factorial
h=sp.Symbol('h',real=True)
q=[6*h*h*(1-h*h), (1+h)**2*(2*h-1)**2,
   (1-h)**2*(2*h+1)**2, (1-h*h)*(1+h)**2,
   (1-h*h)*(1-h)**2]
assert sp.simplify(q[0]-q[1]+(h+1)*(10*h**3-6*h**2-3*h+1))==0
assert sp.simplify(q[4]-q[1]+h**2*(h+1)*(5*h-3))==0
assert sp.simplify(q[3]-q[1]+h*(h+1)**2*(5*h-4))==0
assert sp.simplify(q[3]-q[0]-(h-1)*(h+1)*(5*h*h-2*h-1))==0
r=sorted(float(sp.re(x)) for x in sp.nroots(10*h**3-6*h**2-3*h+1) if abs(float(sp.im(x)))<1e-12 and 0<float(sp.re(x))<.5)[0]
print('opt height',r,'squared condition',float(q[3].subs(h,r)/q[0].subs(h,r)))
# Independent direct assembly. Orthonormal scalar harmonics with respect to probability sphere.
def rawcoeff(l,m,h):
    m0=abs(m); norm=np.sqrt((2*l+1)*float(factorial(l-m0))/float(factorial(l+m0)))
    sign=(-1)**m0 if m<0 else 1
    P=float(lpmv(m0,l,h)); Pprev=float(lpmv(m0,l-1,h)) if m0<=l-1 else 0.
    # (1-h²) d P_l^m/dh= -l h P_l^m+(l+m)P_{l-1}^m
    dp=(-l*h*P+(l+m0)*Pprev)/(1-h*h)
    a=-np.sqrt(1-h*h)*dp*norm*sign
    b=m*P/np.sqrt(1-h*h)*norm*sign
    return a,b

def matrix(l, h, M):
    # field component observations E_theta,E_phi; source basis normalized gradients and Hodge gradients.
    T=np.zeros((2*M,2*(2*l+1)),dtype=complex)
    for j in range(M):
        phi=2*np.pi*j/M
        for idx,m in enumerate(range(-l,l+1)):
            a,b=rawcoeff(l,m,h)
            e=np.exp(1j*m*phi)/(np.sqrt(l*(l+1)*M))
            T[2*j,2*idx]=e*a
            T[2*j+1,2*idx]=e*1j*b
            T[2*j,2*idx+1]=e*(-1j*b)
            T[2*j+1,2*idx+1]=e*a
    return T
for x in [-.89,-.5,-.36,-r,-.1,0,.1,r,.36,.5,.89]:
    M=5;T=matrix(2,x,M)
    actual=np.sort(np.linalg.svd(T,compute_uv=False)**2)
    pred=np.sort([5/4*float(z.subs(h,abs(x))) for z in q for j in range(2)])
    assert np.max(np.abs(actual-pred))<2e-12,(x,actual,pred)
    rank=np.linalg.matrix_rank(T,tol=1e-9)
    target=8 if abs(x)<1e-12 else 8 if abs(abs(x)-.5)<1e-12 else 10
    assert rank==target,(x,rank,target)
# Symbolic Jacobi factorization for independent degrees and orders.
for l in range(1,11):
    z=sp.symbols('z')
    for m in range(1,l+1):
        Q=(-1)**m*sp.diff(sp.legendre(l,z),z,m)
        for sign in [-1,1]:
            U=m*(z+sign)*Q-(1-z*z)*sp.diff(Q,z)
            J=(z+sign)*sp.jacobi(l-m,m-sign,m+sign,z)
            ratio=sp.cancel(U/J)
            assert not ratio.has(z), (l,m,sign,ratio)
            assert ratio!=0
for l in range(1,9):
    for x in [-.72,-.31,0,.11,.29,.7]:
        T=matrix(l,x,2*l+1)
        rank=np.linalg.matrix_rank(T,tol=1e-9)
        if x==0: assert rank==2*(2*l+1)-(2 if l%2==0 else 0),(l,x,rank)
        else: assert rank<=2*(2*l+1)
print('All direct Fourier-block, parity, rank, spectral and cubic checks passed.')
