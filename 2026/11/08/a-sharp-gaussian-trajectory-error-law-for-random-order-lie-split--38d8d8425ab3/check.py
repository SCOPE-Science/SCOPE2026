"""Checks of symbolic local splitting coefficients and an exact finite-n risk recursion."""
import numpy as np
import sympy as sp
from scipy.linalg import expm

h=sp.Symbol('h')
A=sp.Matrix([[0,1],[0,0]])
B=sp.Matrix([[0,0],[-1,0]])
C=A+B
K=A*B-B*A
assert K==sp.diag(-1,1)

def e2(X):
    return sp.eye(2)+h*X+h**2*X**2/2

for U, sign in [(e2(A)*e2(B),1),(e2(B)*e2(A),-1)]:
    difference=U-e2(C)-sign*h**2*K/2
    assert all(sp.expand(z).coeff(h,k)==0 for z in difference for k in range(3))

# R_k=E(P_k^T P_k), E(P_k)=(mean one-step matrix)^k.
Af=np.array(A,dtype=float)
Bf=np.array(B,dtype=float)
Cf=Af+Bf
U=expm(Cf)
records=[]
for n in [4,8,16,32,64,128,256]:
    step=1.0/n
    Mp=expm(step*Af)@expm(step*Bf)
    Mm=expm(step*Bf)@expm(step*Af)
    av=(Mp+Mm)/2
    R=np.eye(2)
    for _ in range(n):
        R=(Mp.T@R@Mp+Mm.T@R@Mm)/2
    Eprod=np.linalg.matrix_power(av,n)
    sqerr=float(np.trace(R)+np.sum(U*U)-2*np.trace(U.T@Eprod))
    coefficient=n**3*sqerr
    assert sqerr>0
    records.append((n,coefficient))
    if n>=32:
        assert abs(coefficient-0.5)<0.07
assert all(abs(records[i][1]-0.5)<abs(records[i-1][1]-0.5)
           for i in range(1,len(records)))
assert abs(records[-1][1]-0.5)<0.002
print('PASS: symbolic local coefficients, exact oscillator commutator and',
      len(records),'finite-grid second-moment comparisons')
print('scaled squared-error values:',records)
