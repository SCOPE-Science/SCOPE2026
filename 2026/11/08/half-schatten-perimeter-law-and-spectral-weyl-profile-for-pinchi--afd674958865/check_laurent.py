#!/usr/bin/env python3
"""Finite exact and matrix checks for annular Hardy Laurent multipliers."""
from fractions import Fraction as F
from math import sqrt,pi,gamma,log
import numpy as np
from scipy.linalg import eigvalsh
from scipy.integrate import quad

def V(q,n):return 1+q**n
count=0
for q in (F(1,3),F(1,2),F(3,4)):
 for n in range(-30,31):
  for k in range(-3,4):
   for l in range(-3,4):
    # Exact product-difference identity in the commutator numerator.
    lhs=V(q,n+k)*V(q,n-l)-V(q,n)*V(q,n+k-l)
    rhs=q**n*(q**k-1)*(1-q**(-l))
    assert lhs==rhs;(count:=count+1)

# Direct finite matrix commutator: all interior diagonals and cross coefficients.
for q in (.35,.6,.8):
 N=42;lo=-N-7; size=2*N+15
 phi={-2:.35, -1:.4, 0:.1, 1:1., 3:-.23}
 Vn=lambda n:1+q**n
 A=np.zeros((size,size),dtype=complex)
 for n in range(-N-4,N+5):
  for k,ak in phi.items():
   if lo <= n+k < lo+size:
    A[n+k-lo,n-lo]+=ak*sqrt(Vn(n+k)/Vn(n))
 C=A.conj().T@A-A@A.conj().T
 for n in range(-N,N+1):
  for s in range(-6,7):
   if not -N<=n+s<=N:continue
   pred=0.
   for k,ak in phi.items():
    l=k-s
    if l not in phi:continue
    pred+=ak*phi[l]*(q**n*(q**k-1)*(1-q**(-l)))/(Vn(n-l)*sqrt(Vn(n)*Vn(n+s)))
   assert abs(C[n+s-lo,n-lo]-pred)<1e-10,(q,n,s,C[n+s-lo,n-lo],pred)
   count+=1

# Independent finite-volume spectral traces approach the proposed continuum constant.
for a in (.4, 1., 1.65):
 phi={-1:a,1:1.}
 for h in (.12,.065):
  q=np.exp(-2*h); L=8.5; N=int(L/h)
  ns=np.arange(-N,N+1)
  w2=lambda n:(1+q**(n+1))/(1+q**n)
  diag=[]; off=[]
  for n in ns:
   wn=w2(n); wm=w2(n-1)
   diag.append((wn-wm)*(1+a*a/(wn*wm)))
   if n<ns[-1]-1:
    wp=w2(n+1)
    off.append(-a*(wp-wn)/sqrt(wn*wp))
  # Two independent parity Jacobi blocks.
  from scipy.linalg import eigh_tridiagonal
  ev=np.concatenate((eigh_tridiagonal(np.array(diag)[::2],np.array(off)[::2],eigvals_only=True),eigh_tridiagonal(np.array(diag)[1::2],np.array(off)[1::2],eigvals_only=True)))
  assert ev.min()>=-1e-9
  p=1.
  obs=h**(1-2*p)*sum(max(0,x)**p for x in ev)
  pred=2*(1+a*a)
  assert abs(obs/pred-1)<.24
  count+=1
print('ANNULAR_LAURENT_CHECK_OK',count)
