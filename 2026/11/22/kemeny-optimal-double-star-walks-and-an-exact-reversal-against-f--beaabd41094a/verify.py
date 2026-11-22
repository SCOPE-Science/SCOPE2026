"""Independent, reproducible checks for double-star Kemeny optimization.

The proof of global optimality is analytic. Tests check numerical implementation,
spectral normalization, a related known mixing optimizer, and graph-size limits.
"""
from fractions import Fraction
from math import sqrt, isclose
from random import Random
import numpy as np
import sympy as sp

SQRT2 = sp.sqrt(2)


def graph_laplacian(p, q, a_edges, b_edges, bridge):
    n = p + q + 2
    L = sp.zeros(n)
    for u, v, w in [(0,1,bridge)]+[(0,2+i,a_edges[i]) for i in range(p)]+[(1,2+p+i,b_edges[i]) for i in range(q)]:
        L[u,u] += w; L[v,v] += w; L[u,v] -= w; L[v,u] -= w
    return L


def trace_pseudoinverse(L):
    n = L.rows
    return sp.trace((L+sp.ones(n)/n).inv()) - 1


def resistance_sum(p,q,a,b,z):
    n=p+q+2
    return ((n-1)*(sum(1/w for w in a)+sum(1/w for w in b))+(p+1)*(q+1)/z)/n


def optimum(p, q):
    n=p+q+2
    A=sp.Rational(n-1,n)*(p*p+q*q)
    B=sp.Rational((p+1)*(q+1),n)
    z=sp.sqrt(B)/(sp.sqrt(A)+sp.sqrt(B))
    a=(1-z)/p; b=(1-z)/q
    K=(sp.sqrt(A)+sp.sqrt(B))**2
    return A,B,z,a,b,K


def mixing_balanced(k):
    D = 1 + k*(3+2*SQRT2)
    leaf = (2+SQRT2)/D
    bridge = (1+k*(1+SQRT2))/D
    return leaf,bridge


def run():
    checks=0
    for p in range(1,5):
        for q in range(1,5):
            # Exact rationals, including heterogeneous leaves
            a=[sp.Rational(1,4*p+i+3) for i in range(p)]
            b=[sp.Rational(1,4*q+j+4) for j in range(q)]
            z=sp.Rational(1,8)
            assert sum(a)+z<=1 and sum(b)+z<=1
            L=graph_laplacian(p,q,a,b,z)
            assert sp.simplify(trace_pseudoinverse(L)-resistance_sum(p,q,a,b,z))==0
            checks+=1
            A,B,zopt,aa,bb,K=optimum(p,q)
            assert sp.simplify(p*aa+zopt-1)==0
            assert sp.simplify(q*bb+zopt-1)==0
            assert isclose(float(K),float(resistance_sum(p,q,[aa]*p,[bb]*q,zopt)),rel_tol=2e-12)
            checks+=3

    rng=Random(1771)
    for t in range(1800):
        p=rng.randrange(1,9);q=rng.randrange(1,9)
        A,B,zopt,aa,bb,K=optimum(p,q)
        z=rng.uniform(.015,.93)
        sa=[rng.random()+.01 for _ in range(p)]
        sb=[rng.random()+.01 for _ in range(q)]
        ra=rng.uniform(.01,1-z);rb=rng.uniform(.01,1-z)
        sa=[ra*x/sum(sa) for x in sa]
        sb=[rb*x/sum(sb) for x in sb]
        val=((p+q+1)*(sum(1/x for x in sa)+sum(1/x for x in sb))+(p+1)*(q+1)/z)/(p+q+2)
        assert val+1e-8>=float(K), (t,p,q,val,float(K))
        checks+=1
    # Fixed-size balancing: complete scan for small sums
    for s in range(4,65):
        costs=[]
        for p in range(2,s-1):
            q=s-p
            K=float(optimum(p,q)[-1]);costs.append((p*q,K))
        costs.sort()
        assert all(costs[j][1]>costs[j+1][1] for j in range(len(costs)-1) if costs[j][0]!=costs[j+1][0])
        checks+=1
    # Exact algebra for the mixing-optimal symmetric assignment
    for k in range(1,40):
        a,z=mixing_balanced(k)
        assert sp.simplify(k*a+z-1)==0
        Kf=sp.simplify(resistance_sum(k,k,[a]*k,[a]*k,z))
        Ko=float(optimum(k,k)[-1]); Km=float((sp.Rational(5,2)*k*k+2*k+sp.Rational(1,2)))
        assert float(Kf)+1e-9>=Ko
        if k>=8:assert float(Kf)>Km
        checks+=2
    # Asymptotic comparison by symbolic limits; k positive real symbol
    k=sp.symbols('k', positive=True)
    A=k*k*(2*k+1)/(k+1);B=(k+1)/2
    D=1+k*(3+2*SQRT2)
    am=(2+SQRT2)/D;zm=(1+k*(1+SQRT2))/D
    Kf=A/(1-zm)+B/zm
    Km=sp.Rational(5,2)*k*k+2*k+sp.Rational(1,2)
    certificate=k*(8+5*SQRT2)*(k-1)*(7*k*k+(3*SQRT2-2)*k+SQRT2-3)/(14*(4+3*SQRT2)*(k+1)*(k-1+SQRT2))
    assert sp.simplify(Kf-Km-certificate)==0
    checks+=1
    assert sp.simplify(sp.limit(Kf/k**2,k,sp.oo)-(2+SQRT2))==0
    assert sp.simplify(sp.limit((sp.sqrt(A)+sp.sqrt(B))**2/k**2,k,sp.oo)-2)==0
    assert sp.simplify(sp.limit((sp.Rational(5,2)*k**2+2*k+sp.Rational(1,2))/k**2,k,sp.oo)-sp.Rational(5,2))==0
    assert sp.simplify(sp.limit(zm,k,sp.oo)-(SQRT2-1))==0
    checks+=4
    print('VERIFY_OK:',checks,'independent exact/numerical checks; bridge and Kemeny asymptotic limits')

if __name__=='__main__': run()
