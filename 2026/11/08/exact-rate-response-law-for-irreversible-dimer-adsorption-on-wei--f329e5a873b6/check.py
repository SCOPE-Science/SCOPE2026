#!/usr/bin/env python3
"""Independent finite-state and generating-series checks for weighted-fan dimer adsorption."""
from fractions import Fraction
from functools import lru_cache
from math import isclose

def formula(m, lam):
    beta=2*(1+lam)
    q=[Fraction(1)]
    for j in range(1,m+1):
        q.append(sum(q[k]*q[j-1-k] for k in range(j))/(beta*j-1))
    return q

def finite_graph(m, lam):
    n=2*m
    # vertex 0 hub, vertices 1..n path
    E=[(0,i,lam) for i in range(1,n+1)] + [(i,i+1,Fraction(1)) for i in range(1,n)]
    @lru_cache(None)
    def p(mask):
        if mask&1: return Fraction(0)
        a=[(u,v,w) for u,v,w in E if not ((mask>>u)&1) and not ((mask>>v)&1)]
        if not a: return Fraction(1)
        t=sum((w for u,v,w in a),Fraction(0))
        return sum((w*p(mask | (1<<u)|(1<<v)) for u,v,w in a),Fraction(0))/t
    return p(0),p.cache_info().currsize

def u_series(beta,M):
    a=[1.0]
    for m in range(1,M+1):
        a.append(a[-1]/(beta*m*(beta*(m-1)-1)))
    return a

def rho(beta):
    a=u_series(beta,110)
    def u(z):return sum(v*z**m for m,v in enumerate(a))
    lo,hi=0.0,beta*3
    assert u(lo)>0 and u(hi)<0
    for i in range(110):
        mid=(lo+hi)/2
        if u(mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

def main():
    checks=0
    for lam in [Fraction(1,3),Fraction(1,2),Fraction(1),Fraction(2),Fraction(5,2)]:
        for m in range(1,6):
            a,nstates=finite_graph(m,lam)
            b=formula(m,lam)[m]
            assert a==b,(m,lam,a,b)
            checks+=1
    for lam in [Fraction(1,3),Fraction(1),Fraction(3)]:
        beta=float(2*(1+lam))
        r=rho(beta)
        qs=formula(25,lam)
        for m in [8,12,16,20,24]:
            approx=beta*r**(-m-1)
            rel=float(qs[m])/approx
            assert abs(rel-1)<0.002,(lam,m,rel)
            checks+=1
    for lam in [0.1,0.4,1.,2.,7.,20.,100.]:
        r=rho(2*(1+lam))
        assert r>1
        checks+=1
    r0=rho(4.)
    assert abs(r0-3.475472691346290)<1e-12
    checks+=1
    vals=[rho(2*(1+x)) for x in [0.02,0.1,1.,3.,30.]]
    assert all(a<b for a,b in zip(vals,vals[1:]));checks+=1
    for lam in [0.5,1.,3.]:
        h=1e-5
        k=(rho(2*(1+lam+h))-rho(2*(1+lam-h)))/(2*h)/rho(2*(1+lam))
        assert k>0
        checks+=1
    print(f'PASS {checks} independent assertions; rho(lambda=1)={r0:.15f}; finite-state verification exact rational arithmetic')
if __name__=='__main__':main()
