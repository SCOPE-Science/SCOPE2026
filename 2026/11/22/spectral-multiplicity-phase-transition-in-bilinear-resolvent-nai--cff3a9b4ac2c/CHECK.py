"""Exact finite-matrix checks and density-rank diagnostics for bilinear resolvent dilations.

This script does not establish an infinite-dimensional result; the proof of the
multiplicity theorem uses the integral representations and spectral calculus.
"""
from fractions import Fraction as F
import sympy as s
import numpy as np

def matrix_example(a,b,gamma,ts,vs):
    N=len(ts)
    assert len(vs)==N
    A=s.zeros(N+1)
    A[0,0]=a+sum(v*v/t for v,t in zip(vs,ts))
    B=s.zeros(N+1); B[0,0]=b
    for j,(t,v) in enumerate(zip(ts,vs),1):
        A[j,j]=a+t; A[0,j]=A[j,0]=v
        B[j,j]=b+gamma/t
    I=s.eye(N+1)
    C=A*B+B*A-a*B-b*A+(a*b-gamma)*I
    return A,B,C

def case(n,gamma):
    a=s.Rational(2); b=s.Rational(3)
    ts=list(map(s.Rational,range(1,n)))
    vs=[s.Rational(1,k+2) for k in range(n-1)]
    A,B,C=matrix_example(a,b,gamma,ts,vs); I=s.eye(n)
    assert (A*A.inv()).equals(I) and (B*B.inv()).equals(I)
    K0=a*A.inv()+b*B.inv()-I
    K1=I-a*A.inv(); K2=I-b*B.inv()
    assert (K0+K1+K2).equals(I)
    checks=0
    for m in range(7):
      for k in range(7):
        den=1+a*m+b*k+(a*b-gamma)*m*k
        lhs=(I+m*A+k*B+m*k*C).inv()
        rhs=(K0+K1*(I+m*A).inv()+K2*(I+k*B).inv())/den
        assert (lhs-rhs).equals(s.zeros(n)), (n,gamma,m,k)
        checks+=1
    assert K0.rank()==(n if gamma<a*b else 1)
    assert K1.rank()==n-1 and K2.rank()==n-1
    assert C.rank()==(n if gamma<a*b else n-1)
    ev=np.linalg.eigvalsh(np.array(K0).astype(float))
    if gamma<a*b: assert ev.min()>1e-10
    else: assert abs(ev[0])<1e-10
    return checks, A, B

count=0
for n in (2,3,4,5):
 for gamma in (s.Rational(6),s.Rational(3),s.Rational(1)):
  num,A,B=case(n,gamma); count+=num
  a=2.; b=3.
  if gamma==6:
    arrA=np.array(A).astype(float); arrB=np.array(B).astype(float)
    eigA,UA=np.linalg.eigh(arrA); eigB,UB=np.linalg.eigh(arrB)
    assert abs(eigA.min()-a)<1e-9 and abs(eigB.min()-b)<1e-9
    def rho_rank(eig,U,base,r):
      weights=np.maximum(0,1-base/eig)/eig*np.exp(-r/eig)
      W=(U*weights)@U.T
      ev=np.linalg.eigvalsh(W)
      assert abs(ev[0])<1e-9 and ev[1]>1e-9
      return len(ev)-1
    for r in (0.2,1.,3.):
      assert rho_rank(eigA,UA,a,r)==n-1
      assert rho_rank(eigB,UB,b,r)==n-1
print(f'BILINEAR_DILATION_MATRIX_CHECKS_OK {count} exact inverse identities; 24 positive-rank density probes')
