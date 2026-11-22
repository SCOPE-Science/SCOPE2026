"""Deterministic independent checks of an ellipsoid's paired width/area law.
Only test cases; analytic proof of all dimensions is in RESULT.md.
"""
from itertools import permutations
import numpy as np
import sympy as sp

rng=np.random.default_rng(271828)
for lamb in [np.array([9.,4.,1.]),np.array([7.,3.,.2]),np.array([1.9,1.3,.8])]:
    d=np.prod(lamb)
    v=np.column_stack([lamb,d/lamb])
    J=abs(np.linalg.det(np.column_stack([v[0]-v[2],v[1]-v[2]])))
    V=np.prod([lamb[i]-lamb[j] for i in range(3) for j in range(i+1,3)])
    assert abs(J-V)<1e-10
    n=300000
    z=rng.normal(size=(n,3))
    p=z*z/np.sum(z*z,axis=1,keepdims=True)
    pairs=p@v
    inverse=np.linalg.solve(np.column_stack([v[0]-v[2],v[1]-v[2]]),(pairs-v[2]).T).T
    pback=np.column_stack([inverse[:,0],inverse[:,1],1-inverse.sum(axis=1)])
    assert np.max(np.abs(p-pback))<1e-12
    # Independent support / centering / moment verification.
    x,y=pairs.T
    predicted=-2*d/45*sum((lamb[i]-lamb[j])**2/(lamb[i]*lamb[j]) for i in range(3) for j in range(i+1,3))
    observed=np.cov(x,y,bias=True)[0,1]
    assert abs(observed-predicted) < 0.035*abs(predicted), (observed,predicted)
    assert all(np.linalg.det(np.array([[v[j,0]-v[i,0], v[j,1]-v[i,1]],[v[k,0]-v[i,0],v[k,1]-v[i,1]]]))!=0 for i,j,k in [(0,1,2)])
    print('lambda',lamb,'Jacobian',J,'observed covariance',round(observed,5),'proved covariance',round(predicted,5),'max inversion error',np.max(abs(p-pback)))

l1,l2,l3=sp.symbols('L_1 L_2 L_3',positive=True)
L=[l1,l2,l3]
D=sp.prod(L)
v=[sp.Matrix([z,D/z]) for z in L]
J=sp.det(sp.Matrix.hstack(v[0]-v[2],v[1]-v[2]))
assert sp.simplify(J+(l1-l2)*(l1-l3)*(l2-l3))==0
A=sp.expand(sum(L)*sum(1/z for z in L))
assert sp.simplify(A-9-sum((L[i]-L[j])**2/(L[i]*L[j]) for i in range(3) for j in range(i+1,3)))==0
print('Exact Vandermonde Jacobian and covariance-defect polynomial identities: PASS')
