"""Standalone checks for the Euclidean incenter theorem of K_{2,q} symmetric edge polytopes.
Uses standard-library rational arithmetic and NumPy/SciPy when installed.
This script is numerical corroboration; the dimension-uniform argument is in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import comb, sqrt
import numpy as np
from scipy.optimize import linprog
from scipy.spatial import ConvexHull

checks=0
for q in range(3,71):
    n=q+2
    h=np.zeros(n); h[0]=.5; h[1]=-.5
    W=[]
    for j in range(q):
        w=np.zeros(n); w[0]=.5; w[1]=.5; w[j+2]=-1
        W.append(w)
    W=np.column_stack(W)
    G=W.T@W
    assert np.allclose(G,np.eye(q)+.5*np.ones((q,q)))
    assert np.allclose(G@ (np.eye(q)-np.ones((q,q))/(q+2)),np.eye(q))
    # Exactly certify the rank-one inverse identity over rational numbers.
    constant=-Fraction(1,q+2)+Fraction(1,2)-Fraction(q,2*(q+2))
    assert constant==0
    checks+=3
    d=q%2
    Q=Fraction(q,1)-Fraction(d*d,q+2)
    radius=1/sqrt(float(Q))
    assert radius<1/sqrt(2)
    checks+=1
    for s in range(-q,q+1,2):
        nn=Fraction(q,1)-Fraction(s*s,q+2)
        assert nn<=Q
        if abs(s)>d: assert nn<Q
        checks+=2
    if q%2==0:
        sm=(1-sqrt(1-4/(q*(q+2))))/2
        for s in range(2,q+1,2):
            normal=sqrt(q-s*s/(q+2))
            assert sm*s+radius*normal<=1+2e-12
            checks+=1
        assert abs((sm*2+radius*sqrt(q-4/(q+2)))-1)<2e-12
        checks+=1
    else:
        assert 2*comb(q,(q-1)//2)>=2*q
        checks+=1

# Independently construct facets from the original edge roots and solve the
# Chebyshev-center LP in the intrinsic sum-zero subspace, for moderate q.
for q in range(3,7):
    n=q+2
    vertices=[]
    for i in (0,1):
        for j in range(2,n):
            v=np.zeros(n);v[i]=1;v[j]=-1
            vertices.extend([v,-v])
    vertices=np.array(vertices)
    # Orthonormal basis of the hyperplane sum(x)=0, independent of W.
    B=np.zeros((n,n-1))
    for k in range(1,n):
        B[:k,k-1]=1/sqrt(k*(k+1))
        B[k,k-1]=-k/sqrt(k*(k+1))
    assert np.allclose(B.T@B,np.eye(n-1))
    projected=vertices@B
    hull=ConvexHull(projected)
    # Duplicate coplanar triangulations of nonsimplicial facets are reduced.
    eqs={tuple(np.round(e/np.linalg.norm(e[:-1]),9)) for e in hull.equations}
    assert len(eqs)==2+2**q,(q,len(eqs))
    normals=[]; offsets=[]
    for e in eqs:
        a=np.array(e[:-1],dtype=float)
        b=float(e[-1])
        normals.append(a); offsets.append(-b)
    normals=np.array(normals)
    offsets=np.array(offsets)
    opt=linprog(np.r_[np.zeros(n-1),-1.],A_ub=np.c_[normals,np.ones(len(normals))],b_ub=offsets,bounds=[(None,None)]*(n-1)+[(0,None)],method='highs')
    assert opt.success,opt.message
    expected=1/sqrt(q-(q%2)**2/(q+2))
    assert abs(opt.x[-1]-expected)<1e-7,(q,opt.x[-1],expected)
    assert np.max(normals@np.zeros(n-1)+expected-offsets)<1e-7
    # Check the complete facet distance multiset at origin.
    obs=sorted(offsets)
    target=sorted([1/sqrt(2)]*2 + [1/sqrt(q-s*s/(q+2)) for s in range(-q,q+1,2) for _ in range(comb(q,(q+s)//2))])
    assert np.allclose(obs,target,atol=1e-7), (q,obs,target)
    checks+=5
# Verify the center-set dimensions and all extreme corners independently.
for q in range(3,13):
    eps=np.array(list(product([-1.,1.],repeat=q)))
    sums=eps.sum(axis=1)
    norms=np.sqrt(q-sums**2/(q+2))
    radius=1/sqrt(q-(q%2)**2/(q+2))
    balanced=eps[np.abs(sums)==q%2]
    rank=np.linalg.matrix_rank(balanced)
    assert rank==(q if q%2 else q-1)
    checks+=1
    tm=1-sqrt(2)*radius
    sm=(1-sqrt(1-4/(q*(q+2))))/2 if q%2==0 else 0.
    for sign_s in (-1,1):
        ss=sign_s*sm
        assert np.max(ss*sums+radius*norms-1)<2e-11
        checks+=1
    if q%2==0:
        assert np.max((sm+1e-4)*sums+radius*norms-1)>1e-6
        checks+=1
    assert tm>0 and tm<1
    checks+=1
print('PASS',checks,'dimension-free-formula, full-center-boundary and independent vertex-hull/LP checks')
