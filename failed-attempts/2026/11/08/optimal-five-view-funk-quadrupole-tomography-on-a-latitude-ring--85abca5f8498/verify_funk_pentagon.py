#!/usr/bin/env python3
"""Independent numerical checks of five-view degree-two Funk sampling.

Uses only the Python standard library. The proof is algebraic; these checks
verify normalizations and representative inverse reconstructions.
"""
import cmath
import math
import random

TOL = 3e-11
SQRT = math.sqrt
PI = math.pi


def ordinate(m, t):
    c, s = SQRT(t), SQRT(1-t)
    if m == 0:
        return SQRT(5/(16*PI))*(3*t-1)
    if abs(m) == 1:
        return (-1 if m > 0 else 1)*SQRT(15/(8*PI))*s*c
    if abs(m) == 2:
        return SQRT(15/(32*PI))*s*s
    raise ValueError(m)


def matrix(t):
    return [[-.5*ordinate(m,t)*cmath.exp(2j*PI*j*m/5)
             for m in range(-2,3)] for j in range(5)]


def form_gram(M):
    return [[sum(M[j][m].conjugate()*M[j][n] for j in range(5))
             for n in range(5)] for m in range(5)]


def assert_near(x,y):
    assert abs(x-y) < TOL*(1+abs(y)), (x,y)


def square_condition(t):
    v=[(3*t-1)**2, 6*t*(1-t), 1.5*(1-t)**2]
    return max(v)/min(v)


def check():
    checks=0
    r=(5-SQRT(21))/4
    tstar=(6-SQRT(21))/15
    assert_near(r/(1+r), tstar);checks+=1
    assert_near(square_condition(tstar),(5+SQRT(21))/4);checks+=1
    assert_near(ordinate(0,tstar)**2,ordinate(1,tstar)**2);checks+=1
    for t in (.001,.05,.09,tstar,.13,.2,.28,.4,.5,.79,.95):
        M=matrix(t)
        G=form_gram(M)
        for u,m in enumerate(range(-2,3)):
            for v,n in enumerate(range(-2,3)):
                want = 1.25*ordinate(m,t)**2 if m==n else 0
                assert_near(G[u][v],want);checks+=1
        if abs(t-1/3)>1e-9:
            # Inverse using the five-point discrete Fourier transform.
            rng=random.Random(99)
            c=[complex(rng.uniform(-2,2),rng.uniform(-1,1)) for _ in range(5)]
            y=[sum(M[j][m]*c[m] for m in range(5)) for j in range(5)]
            for idx,m in enumerate(range(-2,3)):
                dft=sum(y[j]*cmath.exp(-2j*PI*j*m/5) for j in range(5))/5
                assert_near(-2*dft/ordinate(m,t),c[idx]);checks+=1
        # Compare operator singular-value ratio using the explicit five columns.
        diag=[G[m][m].real for m in range(5)]
        assert_near(max(diag)/min(diag),square_condition(t));checks+=1
    for j in range(1,1001):
        t=j/1001
        if abs(t-1/3)<1e-10:
            continue
        assert square_condition(t) + 1e-10 >= square_condition(tstar)
        checks+=1
    # Integrate a trace-free quadratic on great circles orthogonal to normals.
    # The moment identity is average(xx^T)=(I-nn^T)/2.
    for theta in (.3, .8, 1.4):
        for phi in (.1,1.1,2.8):
            n=(math.sin(theta)*math.cos(phi),math.sin(theta)*math.sin(phi),math.cos(theta))
            a=(-math.sin(phi), math.cos(phi), 0)
            b=(-math.cos(theta)*math.cos(phi),-math.cos(theta)*math.sin(phi),math.sin(theta))
            Q=((1,.5,-.4),(.5,-2,.2),(-.4,.2,1))
            def quadratic(v):
                return sum(v[i]*Q[i][j]*v[j] for i in range(3) for j in range(3))
            M=1200
            integ=sum(quadratic(tuple(math.cos(2*PI*k/M)*a[i]+math.sin(2*PI*k/M)*b[i] for i in range(3))) for k in range(M))/M
            assert_near(integ,-quadratic(n)/2);checks+=1
    print('CHECKS_PASS',checks)


if __name__=='__main__':
    check()
