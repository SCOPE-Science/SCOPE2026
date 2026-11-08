"""Independent numerical checks for forbidden-biclique root-polytope circumspheres.
Public reproducibility checker. Requires Python 3, numpy, scipy.
"""
import itertools
import math
import numpy as np
from scipy.optimize import minimize

def prediction(p,q,a,b):
    u=p/(a*(p-a))
    v=q/(b*(q-b))
    d=max(0.,a/p+b/q-1)
    h=u*v/(u+v)
    x=a/p-v*d/(u+v)
    y=b/q-u*d/(u+v)
    center=np.r_[np.full(a,x/a),np.full(p-a,(1-x)/(p-a)),
                 np.full(b,y/b),np.full(q-b,(1-y)/(q-b))]
    radius2=2-1/p-1/q-h*d*d
    return center,radius2, 2*h*d

def test(p,q,a,b):
    # Enumerate edge roots directly, independently optimize a simplex over them.
    E=[]
    names=[]
    for i in range(p):
        for j in range(q):
            if i<a and j<b: continue
            root=np.zeros(p+q)
            root[i]=1
            root[p+j]=1
            E.append(root)
            names.append((i,j))
    V=np.array(E)
    m=len(E)
    initial=np.full(m,1/m)
    result=minimize(lambda w: np.dot(V.T@w,V.T@w),initial,method='SLSQP',
        jac=lambda w: 2*V@(V.T@w),bounds=[(0,None)]*m,
        constraints=[{'type':'eq','fun':lambda w:np.sum(w)-1,'jac':lambda w:np.ones_like(w)}],
        options={'ftol':1e-12,'maxiter':500})
    if not result.success and not (np.linalg.norm(result.jac)<1e-6):
        raise RuntimeError((p,q,a,b,result.message))
    z=V.T@result.x
    center,r2,gap=prediction(p,q,a,b)
    assert np.max(abs(z-center))<1e-5, (p,q,a,b,z,center)
    assert abs(np.dot(z,z)-(2-r2))<1e-5
    ds=np.sum((V-center)**2,axis=1)
    assert abs(max(ds)-r2)<1e-8
    assert all(abs(r2-d)<1e-8 if (i<a or j<b) else abs(r2-d-gap)<1e-8 for (i,j),d in zip(names,ds))
    assert abs(np.sum(center[:p])-1)<1e-12
    assert abs(np.sum(center[p:])-1)<1e-12
    return int(gap>1e-12)

if __name__=='__main__':
    cases=0
    screened=0
    for p in range(2,8):
        for q in range(2,8):
            for a in range(1,p):
                for b in range(1,q):
                    screened+=test(p,q,a,b)
                    cases+=1
    assert cases==sum((p-1)*(q-1) for p in range(2,8) for q in range(2,8))
    c,r2,gap=prediction(4,4,3,3)
    assert abs(r2-4/3)<1e-12 and abs(gap-2/3)<1e-12
    assert abs(prediction(4,4,2,2)[1]-1.5)<1e-12
    print('BICLIQUE_ROOT_MINIMUM_SPHERE_CHECKS_PASSED',cases,'screened_cases',screened)
