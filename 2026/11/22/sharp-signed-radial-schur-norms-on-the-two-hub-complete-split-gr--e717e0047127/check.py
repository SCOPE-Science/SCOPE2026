#!/usr/bin/env python3
"""Exact rational checks and independent finite-dimensional numerical tests.

Run with Python 3.10 or later: python check.py
No third-party libraries are needed. Finite tests supplement, not replace, the proof.
"""
from fractions import Fraction as F
import math
import random


def exact_constant(n, t):
    t=F(t)
    a=(1+t)/2
    b=F(1,n)
    k=t*t-a*b
    return F(1) if k<=0 else F(1)+2*k/(a+b+2*abs(t))


def jacobi_eigenvalues(mat):
    m=len(mat)
    a=[[float(x) for x in row] for row in mat]
    for _ in range(100*m*m):
        p,q=max(((i,j) for i in range(m) for j in range(i+1,m)),key=lambda ij:abs(a[ij[0]][ij[1]]))
        if abs(a[p][q])<1e-13:
            break
        tau=(a[q][q]-a[p][p])/(2*a[p][q])
        sgn=1 if tau>=0 else -1
        tangent=sgn/(abs(tau)+math.sqrt(1+tau*tau))
        c=1/math.sqrt(1+tangent*tangent)
        s=tangent*c
        app,aqq,apq=a[p][p],a[q][q],a[p][q]
        a[p][p]=app-tangent*apq
        a[q][q]=aqq+tangent*apq
        a[p][q]=a[q][p]=0
        for j in range(m):
            if j not in (p,q):
                x,y=a[j][p],a[j][q]
                a[j][p]=a[p][j]=c*x-s*y
                a[j][q]=a[q][j]=s*x+c*y
    else:
        raise AssertionError('Jacobi failed to converge')
    return [a[i][i] for i in range(m)]


def matrix_trace_norm(n,t,p):
    size=n+2
    A=[]
    for i in range(size):
        row=[]
        for j in range(size):
            x=1 if i==j else (0 if i>=2 and j>=2 else t)
            row.append(x*math.sqrt(p[i]*p[j]))
        A.append(row)
    return sum(abs(x) for x in jacobi_eigenvalues(A))


def run():
    total=0
    for n in range(2,31):
        for k in range(-24,25):
            t=F(k,24)
            a=(1+t)/2; b=F(1,n)
            kap=t*t-a*b
            q=a+b+2*abs(t)
            assert q>0
            if kap>0:
                C=2*kap/q
                sstar=(b+abs(t))/q
                assert 0<sstar<1
                for j in range(13):
                    s=F(j,12); w=1-s
                    rad=(a*s-b*w)**2+4*t*t*s*w
                    lhs=(a*s+b*w+C)**2-rad
                    rhs=4*kap*(s-sstar)**2
                    assert lhs==rhs, (n,t,s,lhs,rhs)
                    total+=1
                assert exact_constant(n,t)==1+C
            else:
                for j in range(13):
                    s=F(j,12); w=1-s
                    assert s*w*(a*b-t*t)>=0
                    total+=1
                assert exact_constant(n,t)==1
            assert exact_constant(n,t)>=1
            total+=2
    rng=random.Random(271828)
    for n in range(2,12):
        for k in range(-10,11):
            t=k/10
            a=(1+t)/2; b=1/n
            kap=t*t-a*b
            q=a+b+2*abs(t)
            val=float(exact_constant(n,F(k,10)))
            if kap>0:
                s=(b+abs(t))/q
                p=[s/2,s/2]+[(1-s)/n]*n
                assert abs(matrix_trace_norm(n,t,p)-val)<3e-9, (n,t,val)
                total+=1
            for _ in range(3):
                y=[rng.expovariate(1) for _ in range(n+2)]
                p=[v/sum(y) for v in y]
                assert matrix_trace_norm(n,t,p)<=val+2e-9,(n,t,val)
                total+=1
    for n in (2,3,4,10,100,1000):
        cplus=exact_constant(n,F(1))
        cminus=exact_constant(n,F(-1))
        assert cplus==F(5*n-1,3*n+1)
        assert cminus==F(4*n+1,2*n+1)
        assert cminus>cplus
        total+=3
    print(f'PASS: {total} exact-rational and numerical assertions; no assertion implies an infinite proof.')


if __name__=='__main__':
    run()
