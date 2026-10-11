#!/usr/bin/env python3
import math

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def prop(L,k):
    c=math.cos(k*L); s=math.sin(k*L)
    return [[c,s/k],[-k*s,c]]

def delta(alpha):
    return [[1.0,0.0],[alpha,1.0]]

def scalar(alpha,a,k):
    b=2*math.pi-a
    return k*(math.tan(k*a/2)+math.tan(k*b/2))-alpha

def root(alpha,a):
    b=2*math.pi-a
    lo=0.0
    hi=math.pi/max(a,b)
    for _ in range(120):
        mid=(lo+hi)/2
        if scalar(alpha,a,mid)<0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

def periodic_trace_residual(alpha,a,k):
    b=2*math.pi-a
    M=matmul(delta(alpha),matmul(prop(b,k),matmul(delta(alpha),prop(a,k))))
    return (M[0][0]+M[1][1])-2.0

alphas=[0.05,0.2,1.0,3.0,10.0,100.0]
fracs=[0.15,0.3,0.5,0.7,0.85]
for alpha in alphas:
    ka=root(alpha,math.pi)
    assert 0<ka<1
    assert abs(scalar(alpha,math.pi,ka))<2e-11
    assert abs(periodic_trace_residual(alpha,math.pi,ka))<2e-9
    for frac in fracs:
        a=frac*math.pi
        k=root(alpha,a)
        assert 0<k<math.pi/max(a,2*math.pi-a)
        assert abs(scalar(alpha,a,k))<2e-10
        assert abs(periodic_trace_residual(alpha,a,k))<2e-8
        assert k < ka
print('VERIFY_OK')
