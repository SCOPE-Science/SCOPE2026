"""Independent numerical tests for continuous geodesic mean on parallel-arm metric graphs."""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss

def cubic_formula(lengths):
    e=sorted(float(t) for t in lengths)
    assert len(e)>=3 and min(e)>0
    k=len(e)-1
    a=e[0]; bs=e[1:]; B=sum(bs); S2=sum(x*x for x in bs); S3=sum(x*x*x for x in bs)
    T=((2*k*k-3*k+4)/12*a**3+(5-2*k)/4*a*a*B
       +(a/4+B/2)*S2+a/2*B*B-S3/4)
    return T/sum(e)**2

def direct_quadrature(lengths,n=400):
    e=np.array(lengths,dtype=float); L=e.sum()
    v,w=leggauss(n); v=(v+1)/2;w=w/2
    T=0.
    for i,p in enumerate(e):
        X=p*v[:,None]
        for j,q in enumerate(e):
            Y=q*v[None,:]
            if i==j:
                ds=np.abs(X-Y)
                sd=min(e[h] for h in range(len(e)) if h!=i)
                d=np.minimum(ds,p+sd-ds)
            else:
                k=min(e[h] for h in range(len(e)) if h not in (i,j))
                d=np.minimum.reduce(np.broadcast_arrays(X+Y,p+q-X-Y,X+k+q-Y,p-X+k+Y))
            T+=p*q*np.sum(w[:,None]*w[None,:]*d)
    return T/L**2

cases=[[1,1,1],[1,1,2],[1,2,3],[1,1,1,1],[.5,.7,1.1,2.4],[.2,1,2,4,6],[1,1,1,1,1,1],[.11,.2,.5,1,3,9]]
for e in cases:
    formula=cubic_formula(e); direct=direct_quadrature(e)
    print('m',len(e),'lengths',e,'formula',formula,'quadrature',direct,'difference',abs(formula-direct))
    assert abs(formula-direct)<9e-5*sum(e)
for m in range(3,10):
    eq=(2*m-1)/(3*m*m)
    collapsed=(2*m-3)/(4*(m-1)**2)
    target=min(eq,collapsed)
    assert (eq<collapsed if m==3 else collapsed<eq)
    rng=np.random.default_rng(m+127)
    for i in range(2000):
        x=rng.dirichlet(np.ones(m))
        assert cubic_formula(x) >= target-1e-12
print('BANANA_METRIC_MEAN_QUADRATURE_AND_BOUNDARY_TESTS_OK')
