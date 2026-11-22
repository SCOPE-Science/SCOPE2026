"""Numerical cross-checks for the spectral-norm-ball projection theorem.

Usage: python3 checker.py (NumPy required).
Analytic inequalities and the dimension limit are proved in RESULT.md.
"""
import math
import numpy as np


def proj(a):
    u, s, vh = np.linalg.svd(a, full_matrices=False)
    return (u * np.minimum(s, 1.0)) @ vh


def vectors(m, n, x, y):
    u = np.r_[x, np.full(m-1, math.sqrt(max(0.,1-x*x)/(m-1)))]
    v = np.r_[y, np.full(n-1, math.sqrt(max(0.,1-y*y)/(n-1)))]
    return u, v


def tangent_value(m, n, x, y):
    A = math.sqrt(m-1)
    B = math.sqrt(n-1)
    return 1 + x*y*((x+A*math.sqrt(1-x*x))*(y+B*math.sqrt(1-y*y))-2*x*y)


def row_value(g, i, j):
    a = abs(g[i, j])
    return 1 + a*np.sum(np.abs(g)) - 2*a*a


def checks():
    rng = np.random.default_rng(31073)
    assertions = 0
    for m,n in [(2,2), (3,3), (4,7), (8,8), (2,10)]:
        low = .5+(1+math.sqrt(m-1))*(1+math.sqrt(n-1))/4
        upper = (1+math.sqrt(m*n))/2
        assert low<=upper+1e-12
        assertions+=1
        if (m,n)==(2,2):
            assert low==upper==1.5
            assertions+=1
        u,v=vectors(m,n,1/math.sqrt(2),1/math.sqrt(2))
        g=np.outer(u,v)
        assert abs(row_value(g,0,0)-low)<1e-10
        assertions+=1
        h=-np.sign(g)
        h[0,0]=1
        s=1e-5
        eps=1e-8
        z=(1+s)*g
        ratio=((proj(z+eps*h)-proj(z-eps*h))/(2*eps))[0,0]
        assert abs(ratio-low)<2e-4,(m,n,ratio,low)
        assertions+=1
        for _ in range(60):
            x,y=rng.uniform(0,1,2)
            uu,vv=vectors(m,n,x,y)
            gg=np.outer(uu,vv)
            assert abs(row_value(gg,0,0)-tangent_value(m,n,x,y))<1e-12
            assertions+=1
        for _ in range(60):
            a=rng.normal(size=(m,n))*rng.uniform(.1,2)
            b=rng.normal(size=(m,n))*rng.uniform(.1,2)
            quotient=np.max(np.abs(proj(a)-proj(b)))/np.max(np.abs(a-b))
            assert quotient<=upper+2e-12,(m,n,quotient,upper)
            assertions+=1
    for n in [3,5,10,20,50,100]:
        lower=.5+(1+math.sqrt(n-1))**2/4
        upper=(1+n)/2
        assert lower<=upper
        assertions+=1
    print('PASS:',assertions,'numerical assertions; no infinite proof inferred')


if __name__=='__main__':
    checks()
