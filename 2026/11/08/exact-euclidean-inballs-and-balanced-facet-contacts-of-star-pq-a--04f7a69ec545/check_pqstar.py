"""Numerical checks of the exact inball of a PQ adjacency polytope of a star.
Reconstructs the original vertices and intrinsic Euclidean metric.
Requires numpy and scipy. No external data files.
"""
from itertools import product
from math import comb, floor, sqrt
import numpy as np
from scipy.linalg import null_space
from scipy.optimize import linprog
from scipy.spatial import ConvexHull


def polytope_data(m):
    n=m+1
    verts=[]
    for i,j in [(0,0)]+[(k,k) for k in range(1,n)]+[(0,k) for k in range(1,n)]+[(k,0) for k in range(1,n)]:
        p=np.zeros(2*n)
        p[i]=p[n+j]=1
        verts.append(p)
    verts=np.asarray(verts)
    C=np.zeros((2,2*n))
    C[0,:n]=1
    C[1,n:]=1
    Q=null_space(C)
    z=(verts-verts[0])@Q
    return verts,Q,z


def predicted(m):
    n=m+1
    a=sqrt(m/n)
    b=sqrt((m+2*(m*m//4))/n)
    r=1/(m*a+b)
    t=a*r
    cc=np.r_[1-m*t,np.full(m,t),1-m*t,np.full(m,t)]
    h=2*m+(comb(m,m//2) if m%2==0 else 2*comb(m,m//2))
    return r,t,cc,h


def direct_lp(m):
    # Construct *all* advertised inequalities and project normals to the true affine space.
    verts,Q,z=polytope_data(m)
    n=m+1
    A=[]; B=[]; tags=[]
    for block in range(2):
      for i in range(1,n):
        a=np.zeros(2*n)
        a[block*n+i]=-1
        A.append(a);B.append(0.);tags.append(('lower',block,i))
    for S in product((0,1),repeat=m):
        a=np.zeros(2*n)
        for i,which in enumerate(S,1):
            a[i if which else n+i]=1
        A.append(a);B.append(1.);tags.append(('upper',S))
    AA=np.asarray(A); BB=np.array(B)
    assert np.max(AA@verts.T-BB[:,None])<1e-10
    aq=AA@Q
    nr=np.linalg.norm(aq,axis=1)
    offs=BB-AA@verts[0]
    # Maximize radius, center represented in orthonormal intrinsic coordinates.
    rs=linprog(np.r_[np.zeros(2*m),-1.], A_ub=np.c_[aq,nr], b_ub=offs,
               bounds=[(None,None)]*(2*m)+[(0,None)], method='highs')
    assert rs.success,rs.message
    r,t,c,h=predicted(m)
    cc=Q.T@(c-verts[0])
    sl=offs-aq@cc-r*nr
    assert min(sl)>-2e-9, (m,min(sl))
    assert abs(rs.x[-1]-r)<3e-9, (m,rs.x[-1],r)
    tangent=sum(abs(x)<2e-9 for x in sl)
    assert tangent==h,(m,tangent,h)
    if m<=4:
        hull=ConvexHull(z)
        # facet hyperplanes normalized to Euclidean unit normals
        eq=hull.equations
        # Qhull can repeat triangulated facets; they should imply same Chebyshev optimum.
        res=linprog(np.r_[np.zeros(2*m),-1.],A_ub=np.c_[eq[:,:-1],np.linalg.norm(eq[:,:-1],axis=1)],b_ub=-eq[:,-1],bounds=[(None,None)]*(2*m)+[(0,None)],method='highs')
        assert res.success
        assert abs(res.x[-1]-r)<3e-8,(m,res.x[-1],r)
        # every inequality listed is facet-bearing: one generic interior point for each facet can be constructed.
    return len(verts),len(tags),h,round(r,10)


def main():
    for m in range(1,13):
        print('m=',m,'results=',direct_lp(m))
    print('PQ_STAR_INTRINSIC_INBALL_LP_CHECKS_PASSED 12')

if __name__=='__main__': main()
