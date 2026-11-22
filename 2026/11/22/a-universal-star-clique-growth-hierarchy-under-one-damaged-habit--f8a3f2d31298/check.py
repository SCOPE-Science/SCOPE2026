"""Numerical and exact-arithmetic supplementary checks of the stated spectral theorem.

Run: python3 check.py    (requires NumPy for the independent matrix test).
The analytic proof, not numerical enumeration, establishes the all-parameter claim.
"""
from fractions import Fraction
import math
import numpy as np


def bisect(fn, left, right, steps=100):
    assert fn(left) < 0 and fn(right) > 0
    for _ in range(steps):
        mid = (left + right) / 2
        if fn(mid) > 0:
            right = mid
        else:
            left = mid
    return (left + right) / 2


def reduced_roots(n, q):
    alpha = (n-2)/(n-1)
    beta = 1/(n-1)
    z_star_leaf = bisect(lambda z:z**3+q*z*z-z-alpha*q, math.sqrt(alpha), 1)
    z_clique = bisect(lambda z:(z+q)*(z-alpha)-beta, alpha, 1)
    z_star_hub = (-q + math.sqrt(q*q+4))/2 if q < 1e5 else 2/(q+math.sqrt(q*q+4))
    return z_star_leaf,z_clique,z_star_hub


def generator(n, q, kind):
    adj=np.zeros((n,n),dtype=float)
    if kind=='clique':
        adj[:,:]=1.0
        np.fill_diagonal(adj,0)
        damaged=0
    else:
        for v in range(1,n):
            adj[0,v]=adj[v,0]=1
        damaged=1 if kind=='star_leaf' else 0
    P=adj/adj.sum(axis=1)[:,None]
    M=P.T-np.eye(n)
    M[damaged,damaged]-=q
    return M


def run():
    tests=0
    for n in range(3,31):
        a=Fraction(n-2,n-1); b=1-a
        for j in range(1,10):
            z=a+(1-a)*Fraction(j,10)
            q=(1-z)*(z+b)/(z-a)
            P=z**3+q*z*z-z-a*q
            Q=z*(z+q)-1
            assert P==a*b*(z-1)/(z-a)<0
            assert Q==a*(1-z)/(z-a)>0
            tests+=2
    for n in range(3,201):
        for expo in range(-3,4):
            for k in (1.,2.,5.):
                q=k*10.**expo
                e,t,c=reduced_roots(n,q)
                assert e>t>c and 0<c<1 and 0<t<1 and 0<e<1,(n,q,e,t,c)
                tests+=5
    for n in (3,4,5,6,8,10,14,20):
        for q in (.01,.1,.5,1,2,10,100):
            roots=reduced_roots(n,q)
            for name,root in zip(('star_leaf','clique','star_hub'),roots):
                a=generator(n,q,name)
                actual=max(np.linalg.eigvals(a).real)
                assert abs(actual-(root-1))<2e-10,(n,q,name,actual,root-1)
                tests+=1
    for n in (3,4,5,10,31,101):
        a=(n-2)/(n-1)
        for q in (1e-7,5e-8):
            e,t,c=reduced_roots(n,q)
            assert abs((1-e)/q-1/(2*(n-1)))<2e-6
            assert abs((1-t)/q-1/n)<2e-6
            assert abs((1-c)/q-.5)<2e-6
            tests+=3
        e,t,c=reduced_roots(n,1e9)
        assert abs(e-math.sqrt(a))<1e-6
        assert abs(t-a)<1e-6
        assert abs(c)<1e-6
        tests+=3
    print(f'PASS: {tests} exact-arithmetic and numerical assertions')
    for n in (3,5,12):
        print('example n=',n,' q=1, z=(star leaf, clique, star hub)',
              tuple(round(x,12) for x in reduced_roots(n,1)))

if __name__=='__main__':
    run()
