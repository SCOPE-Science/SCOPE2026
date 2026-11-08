"""Numerical and exact checks for the K_{p,q} Laplacian-simplex minimum sphere.
Requires numpy and scipy. Execute: python check_circumball.py
"""
import numpy as np
from scipy.optimize import minimize


def Lpq(p, q):
    n = p+q
    L = np.zeros((n,n))
    for i in range(p):
        for j in range(p,n):
            L[i,i]+=1; L[j,j]+=1
            L[i,j]-=1; L[j,i]-=1
    return L


def theorem(p,q):
    assert 2<=p<=q
    n=p+q
    a0=q*(q-p)*(n+1)/(2*n*n)
    a=min(a0,q/p)
    center=np.array([a]*p+[-p*a/q]*q)
    if a0<=q/p:
        R2=p*q*(n+2)/n+p*q*(q-p)**2*(n+1)**2/(4*n**3)
    else:
        R2=q*q*(p-1)/p
    return center,R2,a0<=q/p


def check(p,q):
    n=p+q
    V=Lpq(p,q)
    c,R2,all_touch=theorem(p,q)
    ds=np.sum((V-c)**2,axis=1)
    assert np.max(np.abs(ds[:p]-R2))<1e-7
    if all_touch:
        assert np.max(np.abs(ds-R2))<1e-7
        weights=np.array([(1+c[0])/n]*p+[(1-p*c[0]/q)/n]*q)
        assert weights.min()>=-1e-10
    else:
        assert np.all(ds[p:]<R2-1e-7)
        weights=np.array([1/p]*p+[0]*q)
        gap=((p*(q-p)*(n+1)-2*n*n)/p)
        assert abs((R2-ds[-1])-gap)<1e-7
    # Contact points have center as convex combination: global exact certificate.
    assert abs(sum(weights)-1)<1e-10
    assert np.max(np.abs(weights@V-c))<1e-9
    # Independent full-dimensional numerical minimax, no group symmetry imposed.
    if n<=18:
        def clearance(z):
            return z[-1]-np.sum((V-z[:-1])**2,axis=1)
        init=np.r_[c,R2+1]
        ans=minimize(lambda z:z[-1],init,method='SLSQP',
            constraints=[{'type':'ineq','fun':clearance},
                         {'type':'eq','fun':lambda z:sum(z[:-1])}],
            options={'ftol':1e-10,'maxiter':250})
        assert ans.success, (p,q,ans.message)
        assert abs(ans.x[-1]-R2)<2e-6*max(1,R2),(p,q,ans.x[-1],R2)
    return all_touch


def main():
    tested=screened=0
    for p in range(2,8):
        for q in range(p, min(30,p+23)):
            if not check(p,q): screened+=1
            tested+=1
    p=3
    for q in (13,14):
        n=p+q
        numerator=p*(q-p)*(n+1)-2*n*n
        assert (numerator<0)==(q==13)
    print('BIPARTITE_LAPLACIAN_CIRCUMBALL_CHECKS_PASSED', tested, screened)

if __name__=='__main__': main()
