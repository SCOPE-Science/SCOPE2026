#!/usr/bin/env python3
"""Reproduce finite diagnostics for a numerical-range width perturbation theorem.
Uses Python standard library only. Infinite-dimensional/analytic claims require the written proof.
"""
import math, random

L=1/math.sqrt(2)

def eigs3(t,d):
    A=[[t*d[0],.5,0.],[.5,t*d[1],.5],[0.,.5,t*d[2]]]
    for _ in range(45):
        p,q=max(((0,1),(0,2),(1,2)),key=lambda z:abs(A[z[0]][z[1]]))
        if abs(A[p][q])<1e-14: break
        tau=(A[q][q]-A[p][p])/(2*A[p][q])
        rot=(1 if tau>=0 else -1)/(abs(tau)+math.sqrt(1+tau*tau))
        c=1/math.sqrt(1+rot*rot); s=rot*c
        app=A[p][p]; aqq=A[q][q]; apq=A[p][q]
        A[p][p]=app-rot*apq; A[q][q]=aqq+rot*apq
        A[p][q]=A[q][p]=0.
        for k in range(3):
            if k!=p and k!=q:
                akp=A[k][p];akq=A[k][q]
                A[k][p]=A[p][k]=c*akp-s*akq
                A[k][q]=A[q][k]=s*akp+c*akq
    return sorted(A[i][i] for i in range(3))

def coeff(d):
    return (4*(d[0]-d[2])**2+(d[0]+d[2]-2*d[1])**2)/(8*math.sqrt(2))

def oscillation(eps,d):
    return eigs3(eps,d)[2]+eigs3(-eps,d)[2]-math.sqrt(2)

random.seed(20261115)
tests=0
for i in range(180):
    d=[random.uniform(-2,2) for _ in range(3)]
    for eps in [0.005,0.0025]:
        actual=oscillation(eps,d)
        expected=coeff(d)*eps**2
        assert abs(actual-expected)<max(2e-8,1e-2*expected), (i,d,eps,actual,expected)
        assert actual>=-1e-10
        tests+=2
for i in range(120):
    d=[random.uniform(-2,2) for _ in range(3)]
    avg=sum(d)/3
    v=sum((z-avg)**2 for z in d)
    lower=3/(4*math.sqrt(2))*v
    upper=1/math.sqrt(2)*v
    assert lower-1e-10 <= coeff(d) <= upper+1e-10
    tests+=1
for eps in [0.01,.13,.48,1.5,3.2]:
    d=(1,-2,1)
    assert abs(oscillation(eps,d)-(math.sqrt(2+9*eps*eps)-math.sqrt(2)))<5e-12
    d=(1,0,-1)
    assert abs(oscillation(eps,d)-(math.sqrt(2+4*eps*eps)-math.sqrt(2)))<5e-12
    tests+=2
print('VERIFY_OK',tests,'finite assertions')
