"""Finite-dimensional verification for a boundary-absorbing quantum path.

The exact rational test checks the Lyapunov equation at many sizes and rates.
The independent spectral test computes the time-integral from an eigenbasis.
Requires Python 3, NumPy and SciPy for the spectral test.
"""
from fractions import Fraction as F
import numpy as np
from scipy.linalg import solve_continuous_lyapunov

Z = (F(0), F(0))
ONE = (F(1), F(0))

def add(x,y): return (x[0]+y[0], x[1]+y[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])

def q(i,j,n,k,w):
    if i>j: return conj(q(j,i,n,k,w))
    ell=n-j
    if (j-i)%2==0: return (ell*(F(i+1,1)/k+F(i,1)*k/(w*w)),F(0))
    return (F(0),-ell/w)

def a(i,j,k,w):
    if i==0 and j==0: return (-k/2,F(0))
    if abs(i-j)==1: return (F(0),w/2)
    return Z

count=0
for n in range(1,16):
    for k,w in [(F(1,3),F(2,5)),(F(3,2),F(5,4)),(F(7,3),F(3,2)),(F(4),F(1,7))]:
        for i in range(n):
            for j in range(n):
                val=ONE if i==j else Z
                for t in range(n):
                    val=add(val,add(mul(conj(a(t,i,k,w)),q(t,j,n,k,w)),mul(q(i,t,n,k,w),a(t,j,k,w))))
                assert val==Z,(n,k,w,i,j,val)
                count+=1
        for j in range(n):
            expected=F(n-j,1)*(F(j+1,1)/k+F(j,1)*k/(w*w))
            assert q(j,j,n,k,w)==(expected,F(0))
        average=sum(q(j,j,n,k,w)[0] for j in range(n))/n
        formula=F((n+1)*(n+2),6)/k+F(n*n-1,6)*k/(w*w)
        assert average==formula

# Independently diagonalize the killed generator and integrate the spectral
# expansion: integral exp(conj(lambda_p)+lambda_q)t dt = -1/(... ).
spectral_count=0
for n in (2,3,4,5,7,9):
    for k,w in ((.37,1.4),(1.8,.6),(4.2,3.1)):
        A=np.zeros((n,n),dtype=complex)
        A[0,0]=-k/2
        for j in range(n-1):
            A[j,j+1]=A[j+1,j]=1j*w/2
        L=np.zeros((n,n),dtype=complex)
        for i in range(n):
            for j in range(n):
                a0=min(i,j);b0=max(i,j);ell=n-b0
                z=ell*((a0+1)/k+a0*k/w**2) if (b0-a0)%2==0 else -1j*ell/w
                L[i,j]=z if i<=j else np.conj(z)
        Q=solve_continuous_lyapunov(A.conj().T,-np.eye(n))
        assert np.max(np.abs(L-Q))<5e-8,(n,k,w,np.max(np.abs(L-Q)))
        vals,vec=np.linalg.eig(A)
        coeff=np.linalg.inv(vec)
        gram=vec.conj().T@vec
        for j in range(n):
            z=coeff[:,j]
            direct=0j
            for p in range(n):
                for t in range(n):
                    direct += -np.conj(z[p])*z[t]*gram[p,t]/(np.conj(vals[p])+vals[t])
            assert abs(direct.real-L[j,j].real)<1e-7,(n,k,w,j,direct,L[j,j])
            assert abs(direct.imag)<1e-7
            spectral_count+=1
        assert np.linalg.eigvalsh(L)[0]>0
print('EXACT_LYAPUNOV_ENTRIES_OK',count)
print('INDEPENDENT_SPECTRAL_LIFETIMES_OK',spectral_count)
print('ALL_CHECKS_PASSED')
