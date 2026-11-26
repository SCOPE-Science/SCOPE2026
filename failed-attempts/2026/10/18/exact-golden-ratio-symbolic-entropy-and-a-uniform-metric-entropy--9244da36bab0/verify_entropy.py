"""Reproduce the exact Markov-graph entropy identities for Ji--Ma's auxiliary map.
Python >=3.9 with SymPy and NumPy. Numerical matrix truncation is a check,
not a substitute for the countable-state Perron/Foster proof.
"""
import sympy as S
import numpy as np
r=(3-S.sqrt(5))/2
beta=2+S.sqrt(5)
assert S.simplify(beta*r*(1-r)-1)==0
assert S.simplify(beta-(3+2*r/(1-r)))==0
assert S.simplify(beta*2*r-(2+2*r/(1-r)))==0
assert S.simplify((2*r-1)/(1-r))<0
z=S.symbols('z',positive=True)
H=-(z*S.log(z)+(1-z)*S.log(1-z))
h=S.simplify(H/(1-z))
h_prob= -S.log(1-z)-(z/(1-z))*S.log(z)
assert S.simplify(h-h_prob)==0
assert S.simplify(S.diff(h,z)+S.log(z)/(1-z)**2)==0
assert S.limit(h,z,0,dir='+')==0
assert S.simplify(S.limit(h,z,S.Rational(1,2),dir='-')-S.log(4))==0
D=z**3-2*z**2-z+1
v1=(2*z**3-z**2-2*z+1)/D
v3=(z**2-2*z**3)/D
v4=z**3*(2*z-1)/((z-1)*D)
assert S.simplify(v1-v3-v4-(2*z-1)/(z-1))==0
for n in (10,20,40,80):
    A=np.zeros((n,n),dtype=float)
    for i in range(n):
        cutoff=0 if i<=2 else 1 if i==3 else i-1
        A[i,cutoff:]=1.0
    rho=float(max(abs(np.linalg.eigvals(A))))
    assert rho<float(beta)+1e-8
    assert rho>4.2
    print(f'truncation {n}: Perron root {rho:.12f}; infinite root {float(beta):.12f}')
print('PASS: exact Perron eigenvector, inward drift, acip entropy, and 4 finite cutoff checks')
