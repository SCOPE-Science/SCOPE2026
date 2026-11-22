#!/usr/bin/env python3
"""Standalone exact and numerical checks for normalized Monge vertex norm moments."""
from fractions import Fraction
from math import log, exp, isclose

def vertices(n):
    def block(rows, cols):
        x=[Fraction(0) for _ in range(n*n)]
        for i in rows:
            for j in cols:
                x[n*i+j]=Fraction(1,len(rows)*len(cols))
        return tuple(x)
    result=[]
    for a in range(1,n):
        for b in range(1,n):
            result.append(block(range(a),range(n-b,n)))
            result.append(block(range(n-a,n),range(b)))
    for i in range(n):
        result.append(block([i],range(n)))
    for j in range(n):
        result.append(block(range(n),[j]))
    return result

def exact_checks():
    total=0
    for n in range(2,10):
        v=vertices(n)
        assert len(v)==2*(n*n-n+1)==len(set(v))
        for x in v:
            assert sum(x)==1
            for i in range(n-1):
                for j in range(n-1):
                    assert x[i*n+j]+x[(i+1)*n+j+1]<=x[i*n+j+1]+x[(i+1)*n+j]
            total+=1
        squared=[sum(t*t for t in x) for x in v]
        for s in range(5):
            observed=sum(t**s for t in squared)/len(v)
            H=sum((Fraction(1,k**s) for k in range(1,n)),Fraction(0))
            predicted=(H*H+Fraction(1,n**(s-1)) if s>=1 else H*H+Fraction(n,1))/(n*n-n+1)
            assert observed==predicted, (n,s,observed,predicted)
    return total

def log_window_check():
    n=100000
    h=log(n)
    tol=0.07
    for lam in [-3.0,0.0,3.0]:
        weights=[exp(-(1+lam/h)*log(a)) for a in range(1,n)]
        Z=sum(weights)
        for t in [.25,.5,.75]:
            observed=sum(weights[:int(n**t)])/Z
            expected=t if lam==0 else (1-exp(-lam*t))/(1-exp(-lam))
            assert abs(observed-expected)<tol,(lam,t,observed,expected)
    return True

if __name__=='__main__':
    count=exact_checks()
    log_window_check()
    print('MONGE_VERTEX_MOMENT_TILT_PASS vertices=%d exponents=0..4 critical_windows=-3,0,3'%count)
