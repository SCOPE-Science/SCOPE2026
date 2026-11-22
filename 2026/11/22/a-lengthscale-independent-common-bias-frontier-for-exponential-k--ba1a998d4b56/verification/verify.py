"""Exact and numerical tests of a shared-noise exponential-kernel quadrature formula.

No finite test proves the all-parameter theorem; the proof uses an explicit
tridiagonal precision and a rank-one inverse identity.
"""
from fractions import Fraction as F
from math import exp,tanh
import numpy as np


def mul_K(v,r):
    n=len(v)
    return [sum((r**abs(i-j))*v[j] for j in range(n)) for i in range(n)]


def symbolic_scaled(n,r,t):
    # Use scaled b=lambda*mu, v=lambda*K^{-1}mu.
    q=F(1)-r
    scaled_mu=[F(2)-r**i-r**(n-1-i) for i in range(n)]
    u=q/(F(1)+r)
    b=[F(1)/(F(1)+r)]+[(F(1)-r)/(F(1)+r)]*(n-2)+[F(1)/(F(1)+r)]
    v=[u]+[2*u]*(n-2)+[u]
    assert mul_K(v,r)==scaled_mu
    assert mul_K(b,r)==[F(1)]*n
    S=sum(b)
    T=sum(v)
    d=F(1)+t*S
    w=[(v[i]*d-t*b[i]*T)/d for i in range(n)]
    closed=[u*(1-t*(n-2))/d]+[2*u*(1+t)/d]*(n-2)+[u*(1-t*(n-2))/d]
    assert w==closed
    # (K+tau*11T)*lambda*w=lambda*mu.
    assert [x+t*sum(w) for x in mul_K(w,r)]==scaled_mu
    if n>=3:
        assert (w[0]>0)==(t<F(1,n-2))
        assert (w[0]==0)==(t==F(1,n-2))
        assert all(x>0 for x in w[1:-1])
    else:
        assert all(x>0 for x in w)
    return 1


def run():
    count=0
    for n in range(2,35):
        for r in [F(1,5),F(1,2),F(3,4),F(9,10)]:
            for t in [F(0),F(1,100),F(1,3),F(1),F(9)]:
                count+=symbolic_scaled(n,r,t)
    # Actual continuum beta=exp(-lambda/(n-1)).
    nc=0
    for n in [2,3,4,5,9,17,31]:
        for lam in [0.2,0.8,3.,11.,50.]:
            r=exp(-lam/(n-1))
            u=tanh(lam/(2*(n-1)))/lam
            K=np.fromfunction(lambda i,j: r**np.abs(i-j),(n,n),dtype=float)
            mu=np.array([(2-exp(-lam*i/(n-1))-exp(-lam*(n-1-i)/(n-1)))/lam for i in range(n)])
            for tau in [0., 0.0001, 0.03,0.5,1.,10.]:
                S=(2+(n-2)*(1-r))/(1+r)
                d=1+tau*S
                w=np.array([u*(1-(n-2)*tau)/d]+[2*u*(1+tau)/d]*(n-2)+[u*(1-(n-2)*tau)/d])
                actual=np.linalg.solve(K+tau*np.ones((n,n)),mu)
                assert np.max(np.abs(actual-w)) < 1e-9,(n,lam,tau,actual,w)
                nc+=1
    print('PASS',count,'exact rational tests and',nc,'numerical kernel-system tests')

if __name__=='__main__':run()
