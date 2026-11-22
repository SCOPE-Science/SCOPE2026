#!/usr/bin/env python3
"""Reproduce spectral and finite-instance checks for the gear-graph Kemeny theorem.

Dependencies: Python 3, NumPy, SymPy. All tested instances are finite;
analytic inequalities, not these tests, establish the infinite-family result.
"""
import math
import numpy as np
import sympy as sp

checks=0

def close(a,b,tol=2e-8):
    global checks
    assert abs(a-b) <= tol * max(1.0,abs(a),abs(b)), (a,b)
    checks += 1

def raw_value(n,x,y):
    assert x>0 and y>0
    base=((n+1)*x+4*y)/(2*(2*n+1)*x*y)
    return base+sum((x+4*y)/(2*x*y+4*y*y*math.sin(math.pi*j/n)**2)
                    for j in range(1,n))

def reduced(n,x):
    return 2/((2*n+1)*x)+(n+1)/((2*n+1)*(1-x))+sum(
        (2-x)/((1-x)*(x+(1-x)*math.sin(math.pi*j/n)**2))
        for j in range(1,n))

def derivative(n,x):
    # The formula is the derivative along y=(1-x)/2.
    z=-2/((2*n+1)*x*x)+(n+1)/((2*n+1)*(1-x)**2)
    for j in range(1,n):
        ss=math.sin(math.pi*j/n)**2
        dd=x+(1-x)*ss
        z+=((3-x)*dd-(2-x))/((1-x)**2*dd**2)
    return z

def matrix_value(n,x,y):
    N=2*n+1
    L=np.zeros((N,N),float)
    def edge(i,j,w):
        L[i,i]+=w; L[j,j]+=w; L[i,j]-=w; L[j,i]-=w
    for i in range(n):
        edge(0,1+i,x)
        edge(1+i,1+n+i,y)
        edge(1+(i+1)%n,1+n+i,y)
    p=np.eye(N)-L
    assert np.all(p>=-1e-12)
    assert np.allclose(p.sum(axis=1),1)
    eig=np.linalg.eigvalsh(L)
    assert abs(eig[0])<1e-9 and eig[1]>1e-12
    return float(sum(1/t for t in eig[1:]))

def exact_derivatives():
    t=sp.symbols('t')
    exact={3:sp.Rational(81,35),4:-sp.Rational(2176,2025),
           5:-sp.Rational(875,121),6:-sp.Rational(6063464,351975)}
    for n,expected in exact.items():
        F=2/((2*n+1)*t)+(n+1)/((2*n+1)*(1-t))
        for j in range(1,n):
            ss=sp.sin(sp.pi*j/n)**2
            F+=(2-t)/((1-t)*(t+(1-t)*ss))
        computed=sp.simplify(sp.diff(F,t).subs(t,sp.Rational(1,n)))
        assert sp.simplify(computed-expected)==0,(n,computed)
        global checks
        checks+=1
    g=2/(7*t)+4/(7*(1-t))+8*(2-t)/((1-t)*(3+t))
    p=9*t**4-40*t**3-16*t**2-4*t+3
    assert sp.simplify(sp.diff(g,t) - (-6*p/(7*t*t*(t-1)**2*(t+3)**2)))==0
    checks+=1

def root3():
    lo,hi=1e-7,1/3
    assert derivative(3,lo)<0<derivative(3,hi)
    for _ in range(65):
        mid=(lo+hi)/2
        if derivative(3,mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2

def main():
    exact_derivatives()
    r=root3()
    close(r,0.270681307640681,1e-12)
    for n in range(3,32):
        xs=[0.16/n,0.51/n,0.89/n,1/n]
        for x in xs:
            y=(1-x)/2
            close(raw_value(n,x,y),reduced(n,x))
            close(matrix_value(n,x,y),raw_value(n,x,y))
            h=1e-6*x
            close(derivative(n,x),(reduced(n,x+h)-reduced(n,x-h))/(2*h),4e-6)
        if n>=4:
            assert derivative(n,1/n)<0
            global checks
            checks+=1
            for w in [0.15,0.42,0.73,0.99]:
                assert reduced(n,1/n) < reduced(n,w/n)
                checks+=1
    for n in [7,8,10,20,100,1000,10000]:
        mean_d=(n+2)/(2*n)
        assert 1/mean_d > (3-1/n)/(2-1/n)
        checks+=1
    for n in [4,5,6,7,8,12,16,50,100,500,2000,10000]:
        x=1/n; y=(1-x)/2
        u=n*math.asinh(1/math.sqrt(n-1))
        k_exact= n*(3*n-1)/((2*n+1)*(n-1))+n*(2*n-1)/(n-1)*(math.sqrt(n)/math.tanh(u)-1)
        close(k_exact,raw_value(n,x,y),2e-8)
        k_max=raw_value(n,1/n,1/n)
        assert k_max>k_exact
        checks+=1
    n=10000
    k_opt=raw_value(n,1/n,(1-1/n)/2)
    k_md=raw_value(n,1/n,1/n)
    assert abs(k_opt/n**1.5-2)<0.025
    assert abs(k_md/n**2-5/(2*math.sqrt(3)))<0.0005
    assert abs((k_md/k_opt)/math.sqrt(n)-5/(4*math.sqrt(3)))<0.03
    checks+=3
    print('PASS: ',checks,'finite assertions; n=3 interior x=',format(r,'.15g'))
    print('Analytic proof is required for the all-n and asymptotic statements.')

if __name__=='__main__':
    main()
