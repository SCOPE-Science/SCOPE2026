"""Independent finite-size tests for Poisson-reset W-state depolarization.

Needs numpy and scipy. Numerical checks illustrate, but do not replace,
proofs of the all-size spectral and asymptotic statements.
"""
from math import sqrt
import numpy as np
from scipy.linalg import eigvalsh
from scipy.special import roots_jacobi, roots_legendre
from scipy.optimize import brentq


def depolarized_W(n,u):
    dim=2**n
    psi=np.zeros(dim)
    for i in range(n): psi[1<<i]=1/sqrt(n)
    rho=np.outer(psi,psi)
    for i in range(n):
        out=np.zeros_like(rho)
        for a in range(dim):
            for b in range(dim):
                if ((a^b)>>i)&1: continue
                a0=a&~(1<<i); b0=b&~(1<<i)
                out[a,b]=(rho[a0,b0]+rho[a0|(1<<i),b0|(1<<i)])/2
        rho=u*rho+(1-u)*out
    return rho


def stationary(n, alpha):
    u,w=roots_jacobi(26,0,alpha-1)
    w=w/w.sum()
    return sum(float(wi)*depolarized_W(n,(float(ui)+1)/2) for ui,wi in zip(u,w))


def partial_transpose_first(r):
    m=r.shape[0]//2
    return r.reshape(2,m,2,m).transpose(2,1,0,3).reshape(2*m,2*m)


def abc(n,a):
    m=n-1
    u,w=roots_jacobi(60,0,a-1)
    u=(u+1)/2; w=w/w.sum()
    p=(1-u)/2; q=(1+u)/2
    A=np.dot(w,p*q**m)
    B=np.dot(w,p/n*q**(m-2)*(2*q*q+(m-1)*(p*p+u*u)))
    C=sqrt(m)/n*np.dot(w,u*u*q**(m-1))
    return A,B,C


def abc_tiny_alpha(n,a):
    u,w=roots_legendre(160)
    u=(u+1)/2; w=w/2
    m=n-1; p=(1-u)/2; q=(1+u)/2
    f0=2.**(-n)
    fA=p*q**m
    fB=p/n*q**(m-2)*(2*q*q+(m-1)*(p*p+u*u))
    A=f0+a*np.dot(w*u**(a-1),fA-f0)
    B=f0+a*np.dot(w*u**(a-1),fB-f0)
    C=a*sqrt(m)/n*np.dot(w,u**(a+1)*q**(m-1))
    return A,B,C


def main():
    count=0
    for n in range(3,8):
        for a in (0.16,0.37,0.85,1.2,4.3):
            r=stationary(n,a)
            assert abs(np.trace(r)-1)<2e-12
            assert eigvalsh(r)[0]>-1e-12
            pt=partial_transpose_first(r)
            A,B,C=abc(n,a)
            m=n-1;dim=2**n
            ket0=np.zeros(dim);ket0[0]=1
            ket1=np.zeros(dim)
            for j in range(m):ket1[dim//2+(1<<j)]=1/sqrt(m)
            assert abs(ket0@pt@ket0-A)<5e-12
            assert abs(ket1@pt@ket1-B)<5e-12
            assert abs(ket0@pt@ket1-C)<5e-12
            assert eigvalsh(pt)[0]<=(A+B-np.sqrt((A-B)**2+4*C*C))/2+5e-12
            count+=6
    for n in (12,20,30,50,80,120):
        sc=n**1.5*2.**(-n)
        def minor(c):
            A,B,C=abc_tiny_alpha(n,c*sc)
            return (A*B-C*C)/2.**(-2*n)
        root=brentq(minor,.05,2)
        assert .48<root<1.5
        count+=1
        for c in (.2,.5,1.0):
            A,B,C=abc_tiny_alpha(n,c*sc)
            assert abs(A/2.**(-n)-1)<5
            assert abs(B/2.**(-n)-1)<5
            assert abs(C/2.**(-n)-2*c)<5
            count+=3
        print(f'n={n}: witness root/scaling={root:.9f}')
    print(f'passed {count} independent matrix and quadrature assertions')

if __name__=='__main__':main()
