"""Finite reproducibility checks for a three-coset Fourier determinant theorem.
No third-party packages; sampled checks supplement, rather than prove, asymptotics.
"""
import cmath
import math
import random

TWO_PI = 2.0 * math.pi

def det3(a):
    return (a[0][0] * (a[1][1]*a[2][2] - a[1][2]*a[2][1])
            - a[0][1] * (a[1][0]*a[2][2] - a[1][2]*a[2][0])
            + a[0][2] * (a[1][0]*a[2][1] - a[1][1]*a[2][0]))

def direct(m, tau):
    v = [[cmath.exp(1j*TWO_PI*a*s*tau) for s in range(3)]
         for a in (0,m,m+1)]
    return abs(det3(v))**2

def formula(m, tau):
    return 64.0 * math.prod(math.sin(math.pi*j*tau)**2
                            for j in (1,m,m+1))

def locate(m):
    c = (1/3) if m%3==0 else (-1/3)
    center=1/3+c/(m+0.5)
    left=center-0.05/m
    right=center+0.05/m
    # Golden-section refinement within the predicted local peak; used only for samples.
    gr=(math.sqrt(5)-1)/2
    a,b=left,right
    x=b-gr*(b-a);y=a+gr*(b-a)
    fx,fy=formula(m,x),formula(m,y)
    for _ in range(90):
        if fx < fy:
            a=x;x=y;fx=fy;y=a+gr*(b-a);fy=formula(m,y)
        else:
            b=y;y=x;fy=fx;x=b-gr*(b-a);fx=formula(m,x)
    return (a+b)/2

def run():
    n=0
    rng=random.Random(11329)
    for m in range(3,90):
        for _ in range(24):
            t=rng.uniform(.003,.997)
            a,b=direct(m,t),formula(m,t)
            assert abs(a-b) < 1e-7 + 1e-7*abs(b),(m,t,a,b)
            assert -1e-10 <= b <= 27+1e-9,(m,t,b)
            n+=2
        if m%3==1:
            for t in (1/3,2/3):
                assert abs(formula(m,t)-27) < 1e-9,(m,t)
                n+=1
    for m in (30,32,60,62,90,92,120,122,300,302):
        t=locate(m); d=formula(m,t)
        assert 0<d<27
        assert abs((27-d)*m*m-6*math.pi**2)<4.0, (m,d)
        c=(1/3) if m%3==0 else -1/3
        assert abs(t-(1/3+c/(m+0.5)))<1/m**2,(m,t)
        assert abs(formula(m,t)-formula(m,1-t))<1e-8
        n+=4
    print('THREE_COSET_ARITHMETIC_DETERMINANT_CHECKS_PASSED',n)

if __name__ == '__main__': run()
