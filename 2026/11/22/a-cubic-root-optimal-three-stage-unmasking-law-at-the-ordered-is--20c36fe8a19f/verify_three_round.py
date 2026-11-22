"""Reproduce path-KL and the three-round strong-order asymptotics with stdlib only.
This checker supplies finite enumerations and numerical tests, not a substitute for the analytic limit proof.
"""
from itertools import product
from math import log, log1p, exp, expm1, ceil, isclose

LN2=log(2)

def binary_entropy(x):
    if x <= 0 or x >= 1: return 0.0
    return -x*log(x)-(1-x)*log1p(-x)

def a(k, r):
    if k == 0: return 0.
    return binary_entropy(-expm1(k*log1p(-r))/2)

def F(p,r,cutoff=38.):
    if p == 0: return LN2
    if p == 1: return 2*a(1,r)-a(2,r)
    # This truncation has a bounded geometric-negative-binomial tail.
    n=int(ceil(cutoff/p))
    v=p
    sum1=sum2=0.
    multiplier=1-p
    for k in range(1,n+1):
        aa=a(k,r)
        sum1+=v*aa
        if k>=2:sum2+=((k-1)*p/multiplier)*v*aa
        v*=multiplier
    return 2*sum1-sum2

def B_three(p,q,r):
    s=p+(1-p)*q
    return p*LN2+(1-p)*q*F(p,r)+(1-p)*(1-q)*F(s,r)-a(1,r)

def direct_finite(L,r,p,q):
    lam=1-r
    masks=list(product(range(3),repeat=L))
    states=list(product((-1,1),repeat=L))
    path=entropy=0.
    H_true=LN2+(L-1)*a(1,r)
    weights=(p,(1-p)*q,(1-p)*(1-q))
    for times in masks:
        w=1.
        for t in times:w*=weights[t]
        if w<1e-300:continue
        # Conditional site entropies computed independently from Markov bridge entropy
        for i,t in enumerate(times):
            k=next((i-j for j in range(i-1,-1,-1) if times[j]<t),None)
            ell=next((j-i for j in range(i+1,L) if times[j]<t),None)
            if k is None and ell is None: h=LN2
            elif k is None:h=a(ell,r)
            elif ell is None:h=a(k,r)
            else:h=a(k,r)+a(ell,r)-a(k+ell,r)
            entropy+=w*h
        for x in states:
            px=.5
            for i in range(1,L):px*=(1+lam*x[i-1]*x[i])/2
            den=1.
            for i,t in enumerate(times):
                le=next((j for j in range(i-1,-1,-1) if times[j]<t),None)
                ri=next((j for j in range(i+1,L) if times[j]<t),None)
                if le is None and ri is None:cond=.5
                elif le is None:cond=(1+lam**(ri-i)*x[ri]*x[i])/2
                elif ri is None:cond=(1+lam**(i-le)*x[le]*x[i])/2
                else:
                    k=i-le;ell=ri-i
                    cond=(1+lam**k*x[i]*x[le])*(1+lam**ell*x[i]*x[ri])/(2*(1+lam**(k+ell)*x[le]*x[ri]))
                den*=cond
            path+=w*px*log(px/den)
    return path,entropy-H_true

def checks():
    total=0
    for L in (3,4,5,6):
        for r,p,q in ((.2,.17,.42),(.53,.23,.51),(.08,.49,.27)):
            v,w=direct_finite(L,r,p,q)
            assert abs(v-w)<3e-12,(L,r,p,q,v,w)
            assert v>=-1e-12
            total+=1
    # A purely probabilistic bound on finite-L boundary discrepancy. The bulk
    # limit follows from the geometric nearest-visible-neighbor distribution.
    for r in (.01,.001,.0001,.00001):
        C=(2*LN2)**(-2/3);D=(2*LN2)**(-1/3);V=3*(LN2/4)**(1/3)
        p=C*r**(2/3);q=D*r**(1/3)
        value=B_three(p,q,r)
        assert 0<value<.12 and value/r**(2/3)<V*1.5
        total+=1
    for r in (1e-4,1e-5,1e-6):
        p=(2*LN2)**(-2/3)*r**(2/3)
        q=(2*LN2)**(-1/3)*r**(1/3)
        assert abs(F(p,r)/(r/(2*p))-1)<.12
        assert abs(F(q,r)/(r/(2*q))-1)<.11
        total+=2
    # Confirm that the predicted constants solve their strictly convex
    # algebraic stationary equations and balance all 3 leading contributions.
    C=(2*LN2)**(-2/3);D=(2*LN2)**(-1/3)
    assert abs(LN2-D/(2*C*C))<1e-13
    assert abs(1/(2*C)-1/(2*D*D))<1e-13
    assert abs(C*LN2-D/(2*C))<1e-13
    assert abs(D/(2*C)-1/(2*D))<1e-13
    total+=4
    print('PASS:',total,'independent finite-path and asymptotic numerical checks')

if __name__=='__main__':checks()
