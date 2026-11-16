#!/usr/bin/env python3
"""Exact rational checks for polynomially modulated Hamming heat kernels.
Only finite cases are checked; the mathematical proof covers all dimensions.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb

def spectra(n,r):
    alpha=r/(1+r); beta=r/(1-r)
    P=[]
    for k in range(n+1):
        u=(n-k)*alpha-k*beta
        v=(u*u-(n-k)*alpha*alpha-k*beta*beta)/2
        P.append((u,v))
    return P

def vertex(p,q):
    u,v=p; w,z=q
    D=u*z-w*v
    assert D
    return (v-z)/D,(w-u)/D

def kernel_value(n,r,a,b,x,y):
    h=sum(i!=j for i,j in zip(x,y))
    return r**h*(1+a*h+b*h*(h-1)/2)

def chars(x,s):
    v=1
    for i,b in enumerate(x):
        if (s>>i)&1: v*=x[i]
    return v

def check(n,r):
    P=spectra(n,r)
    weight=[F(comb(n,k))*(1+r)**(n-k)*(1-r)**k for k in range(n+1)]
    assert sum(w*p[0] for w,p in zip(weight,P))==0
    assert sum(w*p[1] for w,p in zip(weight,P))==0
    # Strict parabola, exact arithmetic: (u_i-u_j)^2=2(v_i-v_j)-(beta-alpha)(u_i-u_j).
    alpha=r/(1+r);beta=r/(1-r)
    assert all(2*v == u*u+(beta-alpha)*u-n*alpha*beta for u,v in P)
    points=list(product((-1,1), repeat=n))
    pairs=list(zip(range(n), range(1,n+1)))+[(0,n)]
    for i,j in pairs:
        a,b=vertex(P[i],P[j])
        q=[1+a*u+b*v for u,v in P]
        assert q[i]==q[j]==0
        assert all(v>=0 for v in q)
        assert all((v==0)==(k in (i,j)) for k,v in enumerate(q))
        # Exact diagonalization, every column of the full 2**n Walsh matrix.
        vals=[kernel_value(n,r,a,b,(1,)*n,x) for x in points]
        for s in range(1<<n):
            k=s.bit_count()
            lam=sum(v*chars(x,s) for v,x in zip(vals,points))
            assert lam == weight[k]*q[k]/comb(n,k)
        # Construct an equality-support witness at every adjacent vertex.
        if j==i+1:
            m=min(i,n-i-1)
            def f(x):
                y=F(1)
                for k in range(m): y*=x[2*k]+x[2*k+1]
                for k in range(2*m,i+m): y*=x[k]
                y*=1+x[i+m]
                return y
            target=2**max(i,n-i-1)
        else:
            def f(x):return F(1)+F(1)*__import__('math').prod(x)
            target=2**(n-1)
        entries=[f(x) for x in points]
        assert sum(v!=0 for v in entries)==target
        for x in points:
            assert sum(kernel_value(n,r,a,b,x,y)*f(y) for y in points)==0
    # Pure Walsh degree-k minimum support construction for every facet.
    for k in range(n+1):
        m=min(k,n-k)
        def f(x):
            y=F(1)
            for i in range(m): y*=x[2*i]+x[2*i+1]
            for i in range(2*m,k+m): y*=x[i]
            return y
        assert sum(f(x)!=0 for x in points)==2**max(k,n-k)
    return len(pairs),len(points)

if __name__=='__main__':
    total_v=0;total_p=0
    for n in range(2,7):
        for r in (F(1,4),F(1,3),F(1,2),F(2,3),F(3,4)):
            v,p=check(n,r);total_v+=v;total_p+=v*p
    print('PASS: 25 dimension/scale pairs,',total_v,'exact polygon vertex and full Walsh-spectrum tests;',total_p,'vertex-grid witness values; pure-shell witnesses checked.')
