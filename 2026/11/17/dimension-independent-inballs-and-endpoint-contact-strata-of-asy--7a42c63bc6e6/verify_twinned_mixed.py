#!/usr/bin/env python3
"""Independent finite-dimensional checks for a cubical / simplicial twinned chain polytope."""
import itertools
import math
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import linprog


def normals(d):
    all_n=[tuple([-1]*d)]
    for i in range(d):
        rem=[j for j in range(d) if j!=i]
        for mask in range(1 << (d-1)):
            v=[0]*d
            v[i]=1
            for k,j in enumerate(rem):
                if mask>>k & 1: v[j]=-1
            all_n.append(tuple(v))
    return sorted(all_n)


def hull_and_lp(d):
    verts=[tuple(q) for q in itertools.product((0.,1.),repeat=d)]
    verts += [tuple(-1. if i==j else 0. for i in range(d)) for j in range(d)]
    h=ConvexHull(np.array(verts))
    exact=normals(d)
    # Qhull uses unit normals and nonunit offsets. Each facet has exact intercept one.
    qh_normals=set()
    for eq in h.equations:
        v=eq[:d]/(-eq[-1])
        z=tuple(int(round(e)) for e in v)
        assert max(abs(v[i]-z[i]) for i in range(d))<1e-7,(d,v)
        qh_normals.add(z)
    assert qh_normals == set(exact), (d,len(qh_normals),len(exact),set(exact)-qh_normals)
    A=np.array(exact,dtype=float)
    lengths=np.linalg.norm(A,axis=1)
    obj=np.array([0.]*d+[-1.])
    lp=linprog(obj,A_ub=np.column_stack([A,lengths]),b_ub=np.ones(len(A)),bounds=[(None,None)]*(d+1),method='highs')
    assert lp.success,lp.message
    assert abs(lp.x[-1]-1/math.sqrt(2))<1e-8, (d,lp.x)
    lower = (0. if d==2 else math.sqrt(1.5)-1.)
    upper = 1.-1/math.sqrt(2)
    tangencies=[]
    for t in [lower,(lower+upper)/2,upper]:
        sd=1.-A.dot(np.full(d,t))-lengths/math.sqrt(2.)
        assert np.min(sd)>-2e-12,(d,t,np.min(sd))
        tangencies.append(int(np.sum(abs(sd)<1e-9)))
    pred= [3 if d==2 else d*(d-1)+d*math.comb(d-1,2),d*(d-1),d*(d-1)+d]
    if d==2:pred=[3,2,4]
    assert tangencies==pred,(d,tangencies,pred)
    return d,len(verts),len(qh_normals),lp.x[-1],tangencies


def analytic(d):
    normals_set=normals(d)
    assert len(normals_set)==1+d*2**(d-1)
    kmin=1
    u=1-1/math.sqrt(2)
    ell=0 if d==2 else math.sqrt(1.5)-1
    assert ell<=u
    for t in [ell,(ell+u)/2,u]:
        for v in normals_set:
            assert 1-t*sum(v)+1e-12 >= math.sqrt(sum(x*x for x in v)/2)
    for t in [ell-0.001,u+0.001]:
        assert any(1-t*sum(v) < math.sqrt(sum(x*x for x in v)/2)-1e-8 for v in normals_set)

if __name__=='__main__':
    for d in range(2,8):
        analytic(d)
        if d<=6:
            print('d, input points, facets, radius, contact shell counts:',hull_and_lp(d))
    print('TWINS_CUBE_SIMPLEX_INBALL_PASS')
