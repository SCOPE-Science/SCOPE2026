"""Numerical independent finite cross-check of the cycle cosmological inradius.
Usage: python3 CHECK.py (requires numpy, scipy). The proof is in RESULT.md.
"""
from math import sqrt
import numpy as np
from scipy.optimize import linprog


def cycle_vertices(n):
    d = 2*n
    pts = []
    for e in range(n):
        v,w=e,(e+1)%n
        for sy,su,sw in [(1,1,-1),(1,-1,1),(-1,1,1)]:
            a=np.zeros(d)
            a[v]=su; a[w]=sw; a[n+e]=sy
            pts.append(a)
    return np.array(pts)


def facets(n):
    d=2*n
    normals=[]; labels=[]
    # Connected paths with a proper vertex interval.
    for k in range(1,n):
        for first in range(n):
            V={(first+j)%n for j in range(k)}
            E={(first+j)%n for j in range(k-1)}
            a=np.zeros(d)
            for v in V:a[v]=1
            for e in range(n):
                if e not in E:
                    a[n+e]=int(e in V)+int(((e+1)%n) in V)
            normals.append(a); labels.append(('path',k,first))
    # The full graph, and each full-spanning tree obtained by deleting one cycle edge.
    a=np.zeros(d);a[:n]=1
    normals.append(a); labels.append(('scattering',n,0))
    for e in range(n):
        b=a.copy(); b[n+e]=2
        normals.append(b); labels.append(('spanning_path',n,e))
    return np.array(normals),labels


def formula(n):
    if n<=11:
        r=2*sqrt(2*n)/(n*(1+sqrt(6*n-9)))
        a=2/(n*(1+sqrt(6*n-9)))
        tag={'path_1','scattering'}
    else:
        r=1/sqrt(n*(n-2))
        c3=sqrt(3*(1-3/(2*n)))
        c4=sqrt(4*(1-4/(2*n)))
        a=(2/n)*(1-c3/c4)
        tag={'path_1','path_2'}
    return r,a,tag


for n in list(range(3,16))+[20,24]:
    points=cycle_vertices(n)
    N,labels=facets(n)
    assert N.shape==(n*n+1,2*n)
    assert np.allclose(points.sum(axis=1),1)
    values=N@points.T
    assert min(values.ravel())>=-1e-12
    assert np.linalg.matrix_rank(points[1:]-points[0],tol=1e-10)==2*n-1
    # Solve a full-coordinate Chebyshev LP, with NO symmetry constraints on center.
    unit=N/np.linalg.norm(N-(N.sum(axis=1)/float(2*n))[:,None],axis=1)[:,None]
    A=np.column_stack([-unit,np.ones(len(unit))])
    equality=np.zeros(2*n+1);equality[:2*n]=1
    obj=np.zeros(2*n+1);obj[-1]=-1
    lp=linprog(obj,A_ub=A,b_ub=np.zeros(len(N)),A_eq=[equality],b_eq=[1],
               bounds=[(None,None)]*(2*n)+[(0,None)],method='highs')
    assert lp.success,(n,lp.message)
    r,a,expected=formula(n)
    assert abs(lp.x[-1]-r)<2e-8,(n,lp.x[-1],r)
    center=np.array([a]*n+[1/n-a]*n)
    slack=unit@center-r
    assert min(slack)>-1e-9
    actual={('path_'+str(k) if t=='path' else t) for i,(t,k,_) in enumerate(labels) if abs(slack[i])<2e-8}
    assert actual==expected,(n,actual,expected)
    print(f'n={n:2} facets={len(N):4} radius={r:.12f} active={sorted(actual)}')
print('CYCLE_COSMO_INBALL_INDEPENDENT_LP_PASS')
