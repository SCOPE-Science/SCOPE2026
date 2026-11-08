"""Independent finite-generator and limiting-density checks for the two-hub contact law."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve


def limiting_moments(c):
    a = c*c
    z = quad(lambda u: np.exp(a*u)*u**(a-1), 0, 1, epsabs=2e-12)[0]
    ey = quad(lambda u: np.exp(a*u)*u**a, 0, 1, epsabs=2e-12)[0]/z
    return ey, c*(1+ey), z


def stationary(n,c):
    size=2*(n+1)
    lam=c/np.sqrt(n)
    q=lil_matrix((size,size),dtype=float)
    for y in (0,1):
        for k in range(n+1):
            i=y*(n+1)+k
            arcs=[]
            if k<n: arcs.append((i+1,lam*(1+y)*(n-k)))
            if k: arcs.append((i-1,float(k)))
            if y==0 and k: arcs.append((n+1+k,lam*k))
            if y==1: arcs.append((k,1.))
            for j,r in arcs:
                q[i,j]+=r
                q[i,i]-=r
    qt=q.tocsr().transpose()
    a=qt.tolil();a[0,:]=np.ones(size)
    v=np.zeros(size);v[0]=1
    p=spsolve(a.tocsr(),v)
    assert abs(p.sum()-1)<1e-9
    assert p.min()>-1e-10
    assert max(abs(qt@p))<5e-8
    p=p.reshape(2,n+1)
    return p[1].sum(), np.dot(p.sum(axis=0),np.arange(n+1))/np.sqrt(n)


def verify():
    checks=0
    for c in (0.5,1.0,2.0):
        ey,ex,z=limiting_moments(c)
        a=c*c
        assert 0<ey<1 and c<ex<2*c
        checks+=1
        for u in np.linspace(0.07,0.93,29):
            p0=np.exp(a*u)*u**(a-1)*(1-u)/z
            p1=np.exp(a*u)*u**a/z
            assert abs(p1/(p0+p1)-u)<1e-12
            assert abs(-u*p0+(1-u)*p1)<1e-12
            checks+=2
        vals=[stationary(n,c) for n in (80,320,1280)]
        for hy,hx in vals:
            assert 0<hy<1 and 0<hx<2*c
            checks+=1
        # Large-n errors decrease for these three independent parameter sets.
        assert abs(vals[-1][0]-ey)<abs(vals[0][0]-ey)
        assert abs(vals[-1][1]-ex)<abs(vals[0][1]-ex)
        checks+=2
    ey,ex,z=limiting_moments(1.0)
    assert abs(z-(math.e-1))<1e-11
    assert abs(ey-1/(math.e-1))<1e-11
    assert abs(ex-math.e/(math.e-1))<1e-11
    checks+=3
    print(f"PASS: {checks} finite-generator, transport, and limiting-moment assertions")


if __name__=='__main__':
    verify()
