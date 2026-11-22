#!/usr/bin/env python3
"""Separate algebraic and scattering checks for a magnetic triangular bouquet.
Run with Python 3 standard library; tests verify examples, not the all-size proof.
"""
import cmath
import math


def solve(a, b):
    n=len(b)
    a=[list(row) for row in a]; b=list(b)
    for j in range(n):
        p=max(range(j,n), key=lambda i: abs(a[i][j]))
        assert abs(a[p][j])>1e-11
        a[j],a[p]=a[p],a[j]; b[j],b[p]=b[p],b[j]
        s=a[j][j]
        for k in range(j,n): a[j][k]/=s
        b[j]/=s
        for i in range(n):
            if i==j:continue
            s=a[i][j]
            if not s:continue
            for k in range(j,n):a[i][k]-=s*a[j][k]
            b[i]-=s*b[j]
    return b


def direct_scattering(m, phi, energy):
    # Eliminate only lead amplitudes, retaining all 2m+1 internal vertices.
    n=2*m+1
    matrix=[[0j]*n for _ in range(n)]
    for j in range(n):matrix[j][j]=complex(energy)
    w=cmath.exp(1j*phi)
    for j in range(m):
        a=1+2*j; b=a+1
        matrix[0][a]=matrix[a][0]=-1
        matrix[0][b]=-w
        matrix[b][0]=-w.conjugate()
        matrix[a][b]=matrix[b][a]=-1
    v=math.sqrt(4-energy*energy)
    matrix[0][0]+=1/(1j*v)
    rhs=[0j]*n; rhs[0]=1
    x=solve(matrix,rhs)
    transmission=1-x[0]/(1j*v)
    return abs(transmission)**2


def analytic_scattering(m,phi,e):
    c=math.cos(phi)
    f=e**3-(2*m+1)*e-2*m*c
    q=(4-e*e)*f*f
    d=(e*e-1)**2
    return q/(q+d)


def bisection(fn,a,b,iterations=90):
    fa=fn(a); fb=fn(b)
    assert fa*fb<0,(a,b,fa,fb)
    for _ in range(iterations):
        t=(a+b)*.5; ft=fn(t)
        if ft*fa>0: a=t; fa=ft
        else:b=t;fb=ft
    return (a+b)*.5


checks=0
for m in (1,2,3,4,5,8):
    for phi in (.13,.7,1.8,2.9):
        for e in (-1.8,-1.4,-.7,0,.6,1.4,1.85):
            direct=direct_scattering(m,phi,e)
            expected=analytic_scattering(m,phi,e)
            assert abs(direct-expected)<2e-9,(m,phi,e,direct,expected)
            checks+=1
        c=math.cos(phi)
        f=lambda e:e**3-(2*m+1)*e-2*m*c
        root=bisection(f,-1,1)
        assert -1<root<1 and abs(analytic_scattering(m,phi,root))<1e-24
        # Signed endpoint tests classify the other reflection roots.
        assert f(-1)>0 and f(1)<0
        left_inside=(f(-2)<0)
        right_inside=(f(2)>0)
        expect=(m==1 or (m==2 and c>.5),m==1 or (m==2 and c<-.5))
        assert (left_inside,right_inside)==expect,(m,phi,c)
        checks+=5

for m in (3,4,5,9):
    am=m-1; t0=m/am
    sm=m/(am+1/math.sqrt(3)); sp=m/(am-1/math.sqrt(3))
    for phi in (.08,.04,.02):
        eps=1-math.cos(phi)
        c=math.cos(phi)
        f=lambda e:e**3-(2*m+1)*e-2*m*c
        root=bisection(f,-1,1)
        R=lambda e:1-analytic_scattering(m,phi,e)
        left=bisection(lambda e:R(e)-.5,-1,root)
        right=bisection(lambda e:R(e)-.5,root,-1+4*eps)
        error=max(abs((root+1)/eps-t0),abs((left+1)/eps-sm),abs((right+1)/eps-sp))
        assert error<10*phi*phi,(m,phi,error)
        checks+=3

# Localized eigenstate count is m-1 per eigenvalue when both coupling
# amplitudes 1+w and 1-w are nonzero; a vanishing amplitude gives m.
for m in (1,2,3,4,5,8,11):
    for w,expected in [(1,(m-1,m)),(-1,(m,m-1)),(1j,(m-1,m-1))]:
        plus=m if 1+w==0 else m-1
        minus=m if 1-w==0 else m-1
        assert (plus,minus)==expected
        checks+=1
print('ALL_CHECKS_PASSED',checks)
