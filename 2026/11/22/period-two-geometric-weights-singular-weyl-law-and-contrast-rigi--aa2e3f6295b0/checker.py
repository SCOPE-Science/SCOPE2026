"""Finite-matrix and Bloch-formula checks for the two-periodic weighted Cesàro theorem.

Requires numpy, scipy, sympy. This is corroboration, not a proof of the infinite-rank law.
"""
from fractions import Fraction
from math import pi, sqrt, factorial
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh_tridiagonal
from sympy import Matrix, Rational

checks = 0

def verified(condition, message):
    global checks
    assert condition, message
    checks += 1

def coeff(q, a):
    def f(t):
        d = sqrt(1 + q*q - 2*q*np.cos(t))
        return sqrt(2 + q*(a*a + a**-2) + 2*d) / d
    return quad(f, 0, 2*pi, epsabs=3e-12, epsrel=3e-12, limit=300)[0]/(4*pi)

def finite_coeff(N,q,a):
    i=np.arange(1,N+1, dtype=float)
    d=np.where((i.astype(int)%2)==1,a*a,1.0)
    b=-i[:-1]*np.sqrt(q*d[1:]/d[:-1])
    diag=i*i
    diag[:-1]+=b*b
    off=b*i[1:]
    return diag,off

# Exact finite inverse identities for rational sqrt(q) and ratio a.
for r,a in [(Rational(1,2),Rational(1,1)),(Rational(1,3),Rational(2,1)),(Rational(2,3),Rational(3,2))]:
    for N in range(2,9):
        w=[(r*r)**(j+1) * (a*a if j%2==0 else 1) for j in range(N)]
        W=[w0**Rational(1,2) for w0 in w]
        A=Matrix(N,N,lambda i,j: (W[i]/W[j])/(i+1) if j<=i else 0)
        B=Matrix(N,N,lambda i,j: (i+1) if i==j else (-i*W[i]/W[i-1] if i==j+1 else 0))
        verified(A*B==Matrix.eye(N) and B*A==Matrix.eye(N), f'exact inverse r={r},a={a},N={N}')
        verified(A.det()==Rational(1, factorial(N)), 'determinant')

# Identity for Bloch nuclear norm and parity corner splitting.
for q,a in [(0.04,1.0),(0.25,1.0),(0.25,2.0),(0.25,4.0),(0.64,0.5)]:
    for theta in np.linspace(0,2*pi,73):
        z=np.exp(1j*theta); den=1-q*z
        F=np.array([[1, a*sqrt(q)*z],[sqrt(q)/a,1]],dtype=complex)/den
        nuc=np.linalg.svd(F,compute_uv=False).sum()
        d=abs(den)
        formula=sqrt(2+q*(a*a+a**-2)+2*d)/d
        verified(abs(nuc-formula)<5e-13,'nuclear norm')
    F=np.array([[1,-a*sqrt(q)],[sqrt(q)/a,1]],dtype=float)/(1+q)
    s=np.linalg.svd(F,compute_uv=False)
    verified(abs((s[0]-s[1])-sqrt(q)*abs(a-1/a)/(1+q))<5e-13,'Bloch crossing')

# Compare the parity-neutral coefficient to the ordinary geometric kernel.
for q in (0.01,0.25,0.64):
    base=quad(lambda t: 1/abs(1-sqrt(q)*np.exp(1j*t)),0,2*pi,epsabs=1e-12)[0]/(2*pi)
    verified(abs(coeff(q,1)-base)<1e-11,'unmodulated match')
    vals=[coeff(q,a) for a in (1,2,4)]
    verified(vals[0]<vals[1]<vals[2],'strict contrast monotonicity')
    verified(abs(coeff(q,2)-coeff(q,0.5))<1e-11,'parity inversion')

# A finite-section spectral test using the *exact* inverse-bidiagonal representation.
# For fixed rank small relative to the section length, n*s_n should approach the theorem constant.
for q,a in [(0.25,1.0),(0.25,2.0),(0.25,4.0),(0.64,2.0)]:
    N=6500
    diag,off=finite_coeff(N,q,a)
    eigen=eigh_tridiagonal(diag,off,select='i',select_range=(0,200),eigvals_only=True,check_finite=False)
    target=coeff(q,a)
    for rank in [50,100,200]:
        approx=rank/sqrt(eigen[rank-1])
        verified(abs(approx-target)<0.025,'finite-section large-rank check')
print(f'PASS: {checks} exact/symbolic/numerical assertions; finite-rank tests are not proof')
