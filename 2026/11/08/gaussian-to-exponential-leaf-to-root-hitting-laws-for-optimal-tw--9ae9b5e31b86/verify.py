#!/usr/bin/env python3
"""Standalone checks of an optimal two-offer tree hitting-time law."""
from fractions import Fraction
from math import isclose
import numpy as np

def levels(b,h):
    parent = [-1]
    depths = [0]
    frontier=[0]
    for dep in range(1,h+1):
        following=[]
        for v in frontier:
            for _ in range(b):
                parent.append(v);depths.append(dep);following.append(len(parent)-1)
        frontier=following
    adj=[[] for _ in parent]
    for v in range(1,len(parent)):
        u=parent[v];adj[v].append(u);adj[u].append(v)
    return parent,depths,adj

def params(b):
    p=Fraction(2*b+1,(b+1)**2);q=1-p
    return p,q

def mean_closed(b,h):
    p,q=params(b);delta=p-q;r=q/p
    return Fraction(h,1)/delta-2*p*q/delta**2*(1-r**h)

def pgf(b,h,z):
    p,q=params(b)
    J=z
    total=z
    for _ in range(h-1):
        J=z*p/(1-z*q*J)
        total*=J
    return total

def direct_mean(b,h):
    parent,depth,adj=levels(b,h)
    n=len(parent)
    mat=np.eye(n-1)
    rhs=np.ones(n-1)
    for v in range(1,n):
        deg=len(adj[v])
        for u in adj[v]:
            if u!=0:
                prob=(2*deg-1)/(deg*deg) if u==parent[v] else (deg-1)/(deg*deg)
                mat[v-1,u-1]-=prob
    sol=np.linalg.solve(mat,rhs)
    for v in range(1,n):
        if not isclose(sol[v-1],float(mean_closed(b,depth[v])) if depth[v]==h else float(_level_mean(b,h,depth[v])),rel_tol=1e-9,abs_tol=1e-8):
            raise AssertionError((b,h,v,sol[v-1]))
    return float(sol[-1])

def _level_mean(b,h,i):
    p,q=params(b)
    delta=p-q;r=q/p
    # d_j =1/delta - (2q/delta)*r**(h-j)
    return sum((1/delta-2*q/delta*r**(h-j) for j in range(1,i+1)),Fraction(0))

def finite_horizon_check(b,h,tmax=12):
    parent,depth,adj=levels(b,h)
    n=len(parent)
    optimal=[Fraction(int(v==0)) for v in range(n)]
    greedy=optimal[:]
    num=0
    for t in range(1,tmax+1):
        nxt_opt=optimal[:]
        nxt_greedy=greedy[:]
        for v in range(1,n):
            nbr=adj[v]; deg=len(nbr)
            nxt_opt[v]=sum((max(optimal[u],optimal[w]) for u in nbr for w in nbr),Fraction())/deg**2
            nxt_greedy[v]=sum((greedy[parent[v]] if parent[v] in (u,w) else greedy[u] for u in nbr for w in nbr),Fraction())/deg**2
        assert nxt_opt==nxt_greedy,(b,h,t)
        optimal=nxt_opt;greedy=nxt_greedy
        num+=n-1
    return num

def radial_pgf_check(b,h,z):
    # Independent linear tridiagonal system: F_0 =1, F_h=z F_{h-1}.
    import sympy as sp
    p,q=params(b);p=sp.Rational(p.numerator,p.denominator);q=sp.Rational(q.numerator,q.denominator)
    z=sp.Rational(z.numerator,z.denominator)
    mat=sp.eye(h); rhs=sp.zeros(h,1);rhs[0]=z*p
    for i in range(1,h+1):
        if i<h:
            if i>1:mat[i-1,i-2]-=z*p
            mat[i-1,i]-=z*q
        else:
            if i>1:mat[i-1,i-2]-=z
            else:rhs[0]=z
    exact=mat.inv()*rhs
    assert sp.Rational(pgf(b,h,Fraction(int(z.p),int(z.q))).numerator,pgf(b,h,Fraction(int(z.p),int(z.q))).denominator)==exact[-1]

if __name__=='__main__':
    checks=0
    for b,h in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(4,2),(4,3)]:
        m=direct_mean(b,h)
        assert isclose(m,float(mean_closed(b,h)),rel_tol=1e-9)
        count=finite_horizon_check(b,h,tmax=12)
        checks+=count
        radial_pgf_check(b,h,Fraction(1,2))
        radial_pgf_check(b,h,Fraction(2,3))
        checks+=2
        print(f'b={b}, h={h}, exact-mean={mean_closed(b,h)}, finite-horizon states={count} PASS')
    print('TOTAL exact strategy-horizon and PGF checks:',checks)
    for b in [2,3,4,5]:
        p,q=params(b)
        if b>=3:
            rho=p/q;ell=1+1/(q-p)
            for h in [10,20,40]:
                a=(1-rho)*rho**(h-1)/(1-rho**h)
                ratio=float(mean_closed(b,h)*a/ell)
                assert abs(ratio-1)<20/h
            print('metastability mean-cycle check:',b,'PASS')
        else:
            for h in [10,20,40]:
                assert 0<=float(Fraction(h,1)/(p-q)-mean_closed(b,h))<=41
            print('inward-drift bounded-reflection correction: PASS')
