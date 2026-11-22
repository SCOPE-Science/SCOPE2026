"""Standalone numerical and exact checks for coordinatewise robustness of orthogonal ReLU projection."""
import itertools
import numpy as np
from fractions import Fraction

def lipschitz(U):
    n=U.shape[0]
    values=[]
    for mask in itertools.product((0,1),repeat=n):
        P=U.T @ np.diag(mask) @ U
        values.append((np.abs(P).sum(axis=1).max(),mask))
    return max(values, key=lambda v:v[0])

def certify_hadamard_blocks(n):
    U=np.eye(n)
    H=np.array([[1.,1.],[1.,-1.]])/np.sqrt(2)
    for j in range(0,n-1,2):
        U[j:j+2,j:j+2]=H
    L,_=lipschitz(U)
    assert abs(L-1)<1e-12, (n,L)
    return L

for n in range(1,9):
    certify_hadamard_blocks(n)

# A flat 3-support row yields a 4/3 lower bound from its complement.
u=np.array([1.,1.,1.])/np.sqrt(3)
v=np.array([1.,-1.,0.])/np.sqrt(2)
w=np.cross(u,v)
U=np.array([u,v,w]); assert np.allclose(U@U.T,np.eye(3))
P=np.eye(3)-np.outer(u,u)
assert np.allclose(np.abs(P).sum(axis=1),np.array([4/3]*3))
P_exact = [[Fraction(1 if i==j else 0,1)-Fraction(1,3) for j in range(3)] for i in range(3)]
assert [sum(abs(v) for v in row) for row in P_exact] == [Fraction(4,3)]*3
L,mask=lipschitz(U)
assert L>=4/3-1e-12

# A non-flat 2-support row has expansive singleton projection.
for t in [0.01,0.2,0.44,0.65,1.0]:
    if abs(t-1/np.sqrt(2))<1e-12: continue
    u=np.array([np.cos(t),np.sin(t)])
    U=np.array([[u[0],u[1]],[-u[1],u[0]]])
    L,mask=lipschitz(U)
    assert L>1+1e-5,(t,L)

# A genuine 45-degree pair is nonexpansive; its scalar output is nonlinear.
H=np.array([[1.,1.],[1.,-1.]])/np.sqrt(2)
assert abs(lipschitz(H)[0]-1)<1e-12
assert not np.allclose(H.T@np.maximum(H@np.array([1.,0.]),0),
                       H.T@np.maximum(H@np.array([-1.,0.]),0)*(-1))

# Random rotations in dimensions >=2 are expansive except for exceptional angles.
rng=np.random.default_rng(129)
tests=0
for n in range(2,8):
 for _ in range(90):
    A=rng.normal(size=(n,n)); Q,R=np.linalg.qr(A); Q=Q@np.diag(np.sign(np.diag(R)))
    L,_=lipschitz(Q)
    assert L>1+1e-8,(n,L)
    tests+=1
print('PASS: 8 exact block-case dimensions, flat support certificate, 5 rotated pairs, 540 random rotations; all masks enumerated for n<=8; no infinite inference from trials.')
