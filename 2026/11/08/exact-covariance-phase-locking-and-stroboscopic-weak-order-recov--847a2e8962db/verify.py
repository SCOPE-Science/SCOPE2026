#!/usr/bin/env python3
"""Reproduce exact finite-step moment identities and numerical asymptotic witnesses.

All exact tests use fractions and the update formula of the oscillator scheme.
The infinite-family and small-step results require the analytic argument in RESULT.md.
"""
from fractions import Fraction as F
from math import atan, cos, sin, pi, isclose

checks=0

def check(flag, label):
    global checks
    checks += 1
    if not flag:
        raise AssertionError(label)

def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def transpose(A):
    return [[A[j][i] for j in range(2)] for i in range(2)]

def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]

def scl(c,A):
    return [[c*A[i][j] for j in range(2)] for i in range(2)]

def add2(z,w):
    return z[0]+w[0],z[1]+w[1]

def cmul(z,w):
    return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]

def step(h,q,p,kick):
    psi=(p+kick-h*q/2)/(1+h*h/4)
    return q+h*psi,p+kick-h*(q+h*psi/2)

zero=F(0); one=F(1)
for h in [F(1,4), F(1,2), F(1), F(3,2), F(2), F(3), F(4)]:
    den=one+h*h/4
    c=(one-h*h/4)/den
    s=h/den
    R=[[c,s],[-s,c]]
    check(step(h,one,zero,zero)==(c,-s),'basis q')
    check(step(h,zero,one,zero)==(s,c),'basis p')
    check(step(h,zero,zero,one)==(s,c),'noise kick')
    check(c*c+s*s==one,'unitary Cayley')
    w=(c,s)
    C=[[zero,zero],[zero,zero]]
    trig=(one,zero)
    for N in range(1,21):
        b=[[s*s,s*c],[s*c,c*c]]
        C=add(mul(mul(R,C),transpose(R)),scl(h,b))
        cos_sum=sin_sum=zero
        trig=(one,zero)
        w2=cmul(w,w)
        for j in range(1,N+1):
            trig=cmul(trig,w2)
            cos_sum += trig[0]
            sin_sum += trig[1]
        predicted=scl(h/2,[[N-cos_sum,sin_sum],[sin_sum,N+cos_sum]])
        for i in range(2):
            for j in range(2):
                check(C[i][j]==predicted[i][j],'exact covariance entry')
        check(C[0][0]+C[1][1]==h*N,'trace drift')
        discriminant=(C[0][0]-C[1][1])**2+4*C[0][1]**2
        thetaN=(one,zero)
        for j in range(N): thetaN=cmul(thetaN,w)
        check(discriminant*(s*s)==h*h*thetaN[1]**2,'exact spectral gap')
        check((C[0][0]==C[1][1] and C[0][1]==zero)==(thetaN[1]==zero),'isotropy iff resonance')
        if h==2:
            check((C[0][0]==C[1][1] and C[0][1]==zero)==(N%2==0),'exact rational resonances')

# Reproduce fixed-physical-time small-step coefficient limits from the closed form.
def cov(h,N):
    th=2*atan(h/2)
    co=sum(cos(2*j*th) for j in range(1,N+1))
    si=sum(sin(2*j*th) for j in range(1,N+1))
    return [[h*(N-co)/2,h*si/2],[h*si/2,h*(N+co)/2]]

def cov_exact(T):
    return [[T/2-sin(2*T)/4,(1-cos(2*T))/4],
            [(1-cos(2*T))/4,T/2+sin(2*T)/4]]

T=1.0
N=4096
h=T/N
C=cov(h,N); E=cov_exact(T)
check(abs((C[0][0]-E[0][0])/h-sin(T)**2/2)<0.00015,'generic first-order diagonal')
check(abs((C[0][1]-E[0][1])/h-sin(T)*cos(T)/2)<0.00015,'generic first-order cross term')

T=pi
for N in [256,1024,2048]:
    h=T/N
    C=cov(h,N); E=cov_exact(T)
    check(abs((C[0][0]-E[0][0])/h**2-T/24)<0.00007,'resonant second-order diagonal')
    check(abs((C[1][1]-E[1][1])/h**2+T/24)<0.00007,'resonant second-order opposite')
    check(abs((C[0][1]-E[0][1])/h**2)<0.007,'resonant cross goes to zero')

N=3; h=1000000.0
C=cov(h,N)
check(abs(C[0][0]/(N*h))<0.00001,'large-step rank-one q')
check(abs(C[1][1]/(N*h)-1)<0.00001,'large-step rank-one p')
check(abs(C[0][1]/(N*h))<0.00001,'large-step rank-one cross')
print(f'VERIFY_OK checks={checks}')
print('exact_cayley_covariance=PASS; spectral_identity=PASS; isotropy=PASS')
print('weak_error_coefficients=PASS; extreme_step_rank_one=PASS')
