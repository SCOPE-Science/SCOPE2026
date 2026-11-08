#!/usr/bin/env python3
"""Reproducibility checks for the polygon boundary-area-loss formulas.

Standalone: Python >=3.9; numpy/scipy used only for Monte Carlo geometric checks.
The infinite limit is proved analytically in RESULT.md, not by this script.
"""
import itertools
import math
from fractions import Fraction


def polygon_area(vertices):
    return abs(sum(x[0]*y[1]-x[1]*y[0] for x,y in zip(vertices, vertices[1:]+vertices[:1])))/2


def convex_hull(points):
    q=sorted(set(points))
    if len(q)<=1: return q
    def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]
    for p in q:
        while len(lo)>1 and cross(lo[-2],lo[-1],p)<=0: lo.pop()
        lo.append(p)
    hi=[]
    for p in q[::-1]:
        while len(hi)>1 and cross(hi[-2],hi[-1],p)<=0: hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]


def exact_corner_decomposition():
    # All points on the boundary, at least two on each side.
    V=[(Fraction(0),Fraction(0)),(Fraction(3),Fraction(0)),
       (Fraction(3),Fraction(2)),(Fraction(0),Fraction(2))]
    fractions=[(Fraction(1,6),Fraction(5,6)),(Fraction(1,4),Fraction(3,4)),
               (Fraction(1,3),Fraction(2,3)),(Fraction(2,5),Fraction(4,5))]
    edgepoints=[]
    for i,(u,v) in enumerate(fractions):
        a,b=V[i],V[(i+1)%4]
        edgepoints.append([(a[0]+t*(b[0]-a[0]),a[1]+t*(b[1]-a[1])) for t in (u,v)])
    hull=convex_hull([x for L in edgepoints for x in L])
    deficit=polygon_area(V)-polygon_area(hull)
    # Corner triangle cross-products from adjacent nearest sample points.
    area_sum=Fraction(0)
    for i in range(4):
        v=V[i]
        left=edgepoints[(i-1)%4][-1]
        right=edgepoints[i][0]
        area_sum+=abs((left[0]-v[0])*(right[1]-v[1])-(left[1]-v[1])*(right[0]-v[0]))/2
    assert deficit==area_sum
    return deficit


def transitive_pairs(k):
    perms=list(itertools.permutations(range(k)))
    n=0
    for p in perms:
        for q in perms:
            seen={0};todo=[0]
            while todo:
                v=todo.pop()
                for w in (p[v],q[v]):
                    if w not in seen:
                        seen.add(w);todo.append(w)
            if len(seen)==k:n+=1
    return n


def cumulants_from_moments(n):
    kappa=[]
    for k in range(1,n+1):
        target=math.factorial(k)**2
        for j in range(1,k):
            target-=math.comb(k-1,j-1)*kappa[j-1]*math.factorial(k-j)**2
        kappa.append(target)
    return kappa


def quadrature_and_simulation():
    # Optional numerical sanity: direct hull areas versus the local-gap sum.
    import numpy as np
    from scipy.spatial import ConvexHull
    from scipy.integrate import quad
    from scipy.special import exp1
    rng=np.random.default_rng(12011)
    corners=np.array([[0,0],[3,0],[2,2],[0,1]],float)
    E=np.roll(corners,-1,axis=0)-corners
    lengths=np.linalg.norm(E,axis=1)
    P=lengths.sum(); offsets=np.r_[0,np.cumsum(lengths)]
    cross=lambda u,v:u[0]*v[1]-u[1]*v[0]
    A=sum(cross(corners[i],corners[(i+1)%4]) for i in range(4))/2
    sins=np.array([abs(cross(corners[(i-1)%4]-corners[i],corners[(i+1)%4]-corners[i]))/
                  np.linalg.norm(corners[(i-1)%4]-corners[i])/
                  np.linalg.norm(corners[(i+1)%4]-corners[i]) for i in range(4)])
    expected=P*P/2*sins.sum()
    n=800
    arr=[];errors=[]
    for _ in range(360):
        s=np.sort(rng.uniform(0,P,n))
        idx=np.clip(np.searchsorted(offsets,s,side='right')-1,0,3)
        pts=corners[idx]+(s-offsets[idx])[:,None]/lengths[idx,None]*E[idx]
        ar=ConvexHull(pts).volume
        arr.append(n*n*(A-ar))
        if len(set(idx))==4:
            left=[];right=[]
            for i in range(4):
                local=s[idx==i]-offsets[i]
                left.append(local.min())
                right.append(lengths[i]-local.max())
            local_area=.5*sum(sins[i]*right[(i-1)%4]*left[i] for i in range(4))
            errors.append(abs(A-ar-local_area))
    assert max(errors)<1e-9
    assert abs(np.mean(arr)-expected)<30, (np.mean(arr),expected)
    for t in (.1,1,10):
        fun=lambda u:np.exp(-u)/(1+t*u)
        numeric=quad(fun,0,np.inf)[0]
        symbolic=np.exp(1/t)*exp1(1/t)/t
        assert abs(numeric-symbolic)<1e-11
    return float(np.mean(arr)),float(expected),max(errors)



def fluctuation_shape_checks():
    import numpy as np
    rng=np.random.default_rng(20261101)
    tested=0
    for m in range(3,10):
        for _ in range(300):
            theta=2*np.pi*rng.dirichlet(np.ones(m))
            if max(theta)>=np.pi: continue
            v=np.sin(theta)
            r=3*sum(v*v)/sum(v)**2
            assert 3/m-1e-12<=r<1.5+1e-12
            tested+=1
        if m>=5:
            x=np.pi/(m-2)
            v=np.sin([x]*(m-1)+[np.pi-x])
            assert abs(3*sum(v*v)/sum(v)**2-3/m)<1e-12
    for x in (0.2,0.7,1.1):
        v=np.sin([x,x,np.pi-x,np.pi-x])
        assert abs(3*sum(v*v)/sum(v)**2-3/4)<1e-12
    return tested

if __name__=='__main__':
    d=exact_corner_decomposition()
    c=cumulants_from_moments(4)
    assert c==[1,3,26,426],c
    assert [transitive_pairs(k) for k in range(1,5)]==c
    mean,theory,err=quadrature_and_simulation()
    shape_count=fluctuation_shape_checks()
    print(f'CHECK_OK exact_corner_deficit={d} cumulants={c} MonteCarlo_N800_mean={mean:.3f} predicted={theory:.3f} exact_decomposition_maxerr={err:.3g} fluctuation_shape_checks={shape_count}')
