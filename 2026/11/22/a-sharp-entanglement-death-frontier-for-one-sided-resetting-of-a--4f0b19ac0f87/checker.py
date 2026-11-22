"""Reproduce the one-sided quantum-reset concurrence threshold.

Dependencies: Python 3.10+, numpy, sympy. Run: python checker.py
This file is scientific verification code, not a simulation proof of universal claims.
"""
import itertools
import math
import numpy as np
import sympy as sp

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1., -1.]).astype(complex)
SY = np.kron(Y, Y)


def reset(m):
    z = np.zeros((4, 4), dtype=complex)
    z[:2, :2] = m[:2, :2] + m[2:, 2:]
    return z


def generator(m, j, h, rate):
    ham = j*np.kron(X, X) + h*(np.kron(Z, I2)+np.kron(I2, Z))
    return -1j*(ham@m-m@ham) + rate*(reset(m)-m)


def formula(j, h, rate):
    q = rate**2+4*j**2+8*h**2
    m = np.zeros((4, 4), dtype=complex)
    m[0, 0]=(rate**2+2*j**2+16*h**2)/(2*q)
    m[1, 1]=(rate**2+2*j**2)/(2*q)
    m[2, 2]=m[3, 3]=j*j/q
    m[0, 3]=j*(2*h+0.5j*rate)/q
    m[3, 0]=m[0, 3].conjugate()
    m[1, 2]=0.5j*j*rate/q
    m[2, 1]=m[1, 2].conjugate()
    return m


def concurrence(m):
    eig = np.linalg.eigvals(m @ SY @ m.conj() @ SY)
    nums = sorted((math.sqrt(max(0., float(v.real))) for v in eig), reverse=True)
    return max(0., nums[0]-sum(nums[1:]))


def theoretical_concurrence(j, h, rate):
    q=rate**2+4*j**2+8*h**2
    return max(0., j*(math.sqrt(rate**2+16*h**2)-math.sqrt(2*rate**2+4*j**2))/q)


def independent_stationary(j, h, rate):
    # Assemble the full 16x16 complex Lindbladian on matrix units independently
    basis=[]
    for a in range(4):
        for b in range(4):
            e=np.zeros((4, 4),complex);e[a,b]=1
            basis.append(e)
    liouv=np.stack([generator(e,j,h,rate).reshape(16) for e in basis],axis=1)
    # Exactly one zero mode and all others damped for positive parameters
    singular=np.linalg.svd(liouv,compute_uv=False)
    assert singular[-1] < 1e-9 and singular[-2]>1e-5, singular
    rhs=np.zeros(16,complex);rhs[0]=1.
    a=liouv.copy()
    a[0,:]=[np.trace(e) for e in basis]
    x=np.linalg.solve(a,rhs)
    return sum((coeff*e for coeff,e in zip(x,basis)),np.zeros((4,4),complex))


def symbolic_checks():
    j,h,r=sp.symbols('J h r',positive=True,real=True)
    eye=sp.eye(2)
    xx=sp.Matrix([[0,1],[1,0]])
    zz=sp.diag(1,-1)
    ham=j*sp.kronecker_product(xx,xx)+h*(sp.kronecker_product(zz,eye)+sp.kronecker_product(eye,zz))
    q=r*r+4*j*j+8*h*h
    m=sp.zeros(4)
    m[0,0]=(r*r+2*j*j+16*h*h)/(2*q)
    m[1,1]=(r*r+2*j*j)/(2*q)
    m[2,2]=m[3,3]=j*j/q
    m[0,3]=j*(2*h+sp.I*r/2)/q; m[3,0]=sp.conjugate(m[0,3])
    m[1,2]=sp.I*j*r/(2*q);m[2,1]=sp.conjugate(m[1,2])
    z=sp.zeros(4)
    for a in range(2):
        for b in range(2): z[a,b]=m[a,b]+m[a+2,b+2]
    residual=-sp.I*(ham*m-m*ham)+r*(z-m)
    assert all(sp.cancel(t)==0 for t in residual)
    assert sp.cancel(sp.trace(m)-1)==0
    # Two strict positive full-rank principal block determinants
    d1=sp.factor(m[0,0]*m[3,3]-m[0,3]*m[3,0])
    d2=sp.factor(m[1,1]*m[2,2]-m[1,2]*m[2,1])
    assert sp.cancel(d1-j*j*(r*r+4*j*j+16*h*h)/(4*q*q))==0
    assert sp.cancel(d2-j*j*(r*r+4*j*j)/(4*q*q))==0
    # Partial-transpose X-state branch signs
    p1=sp.factor(m[0,3]*m[3,0]-m[1,1]*m[2,2])
    p2=sp.factor(m[1,2]*m[2,1]-m[0,0]*m[3,3])
    assert sp.cancel(p1-j*j*(16*h*h-4*j*j-r*r)/(4*q*q))==0
    assert sp.cancel(p2+j*j*(r*r+4*j*j+32*h*h)/(4*q*q))==0
    return 7


def main():
    counts=symbolic_checks()
    for j,h,rate in itertools.product((0.5,1.,2.),(0.2,0.5,1.,2.3),(0.1,0.5,1.,2.,4.,8.)):
        m=formula(j,h,rate)
        exact=independent_stationary(j,h,rate)
        assert np.max(np.abs(exact-m))<2e-10
        assert np.max(np.abs(generator(m,j,h,rate)))<1e-10
        assert abs(np.trace(m)-1)<1e-10
        assert min(np.linalg.eigvalsh(m))>1e-12
        assert abs(concurrence(m)-theoretical_concurrence(j,h,rate))<1e-9
        positive=(h>j/2 and rate<2*math.sqrt(max(0,4*h*h-j*j)))
        assert (concurrence(m)>1e-9)==positive
        counts+=6
    j=h=1.
    critical=2*math.sqrt(3)
    assert theoretical_concurrence(j,h,critical)<1e-14
    assert theoretical_concurrence(j,h,critical-0.1)>0
    assert theoretical_concurrence(j,h,critical+0.1)==0
    print('PASS:',counts+3,'symbolic/numerical assertions; exact threshold at J=h=1:',critical)

if __name__=='__main__':main()
