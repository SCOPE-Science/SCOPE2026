"""Exact and floating-point checks for signed-root single-vertex deletion geometry."""
from fractions import Fraction
from math import comb, factorial
from itertools import permutations
from scipy.spatial import ConvexHull
import numpy as np

def root_vertices(n):
    E=np.eye(n)
    return np.array([E[i]-E[j] for i in range(n) for j in range(n) if i!=j])

def gram_det(n):
    m=n-2
    W=np.empty((n,m))
    for ix,j in enumerate(range(2,n)):
        W[:,ix]=0
        W[0,ix]=W[1,ix]=.5
        W[j,ix]=-1
    return np.linalg.det(W.T@W)

def orth_basis(n):
    T=np.eye(n)[:,:n-1]-np.eye(n)[:,[-1]]
    return np.linalg.qr(T)[0]

for n in range(3,8):
    V=root_vertices(n)
    i=[(a,b) for a in range(n) for b in range(n) if a!=b].index((0,1))
    Q=np.delete(V,i,axis=0)
    H=orth_basis(n)
    v=V[i]
    def hull(x):return ConvexHull(x@H)
    original=hull(V)
    deleted=hull(Q)
    ratio=1-deleted.volume/original.volume
    predicted=Fraction(2**(n-3),comb(2*n-2,n-1))
    assert abs(ratio-float(predicted))<2e-10,(n,ratio,predicted)
    assert abs(original.volume-comb(2*n-2,n-1)*np.sqrt(n)/factorial(n-1))<2e-10
    assert abs(gram_det(n)-n/2)<1e-9
    # Exact distance certificate: half of v is the midpoint of any two complementary roots.
    f=v/2
    assert np.dot(v,f)==1 and np.max(Q@v)<=1
    assert abs(np.linalg.norm(v-f)-2**-.5)<1e-10
    print(f'n={n}: volume loss={predicted}, projected gap squared=1/2, facet dimension={n-2}')
# Exact deterministic support loss for several distinct coordinate directions.
for n in range(3,9):
    for shift in range(n):
        values=np.array([((i+shift)*7 % n)+.01*i for i in range(n)],float)
        a=int(np.argmax(values)); b=int(np.argmin(values))
        roots=root_vertices(n)
        i=[(x,y) for x in range(n) for y in range(n) if x!=y].index((0,1))
        other=np.delete(roots,i,axis=0)
        width_full=float(np.max(roots@values)-np.min(roots@values))
        width_other=float(np.max(other@values)-np.min(other@values))
        top_gap=np.sort(values)[-1]-np.sort(values)[-2]
        low_gap=np.sort(values)[1]-np.sort(values)[0]
        predicted=min(top_gap,low_gap) if {a,b}=={0,1} else 0.0
        assert abs(width_full-width_other-predicted)<1e-9
print('ROOT_VERTEX_DELETION_EXACT_NUMERIC_PASS')
