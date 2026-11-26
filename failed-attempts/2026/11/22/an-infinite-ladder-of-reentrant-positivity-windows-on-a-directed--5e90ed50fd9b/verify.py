"""Numerical regression checks for fractional directed triangle sign windows.
Run: python verify.py   (Python >=3.9, NumPy and SciPy)
These finite checks supplement, but cannot replace, the analytic proof.
"""
import math
import cmath
import random
import numpy as np
from scipy.linalg import expm

PI=math.pi
P=np.array([[0.,1.,0.],[0.,0.,1.],[1.,0.,0.]])
L=np.eye(3)-P
OMEGA=cmath.exp(2j*PI/3)
F=np.array([[OMEGA**(j*k) for k in range(3)] for j in range(3)],complex)


def params(alpha):
    theta=PI*alpha/6
    radius=3**(alpha/2)
    return theta,radius,1/math.tan(theta)


def q(alpha,t):
    theta,radius,delta=params(alpha)
    s=radius*math.sin(theta)*t
    return np.array([(1+2*math.exp(-delta*s)*math.cos(s-2*PI*j/3))/3 for j in range(3)])


def independent_exp(alpha,t):
    theta,radius,_=params(alpha)
    lambdas=np.array([0, radius*cmath.exp(-1j*theta),radius*cmath.exp(1j*theta)])
    lpower=(F@np.diag(lambdas)@F.conj().T)/3
    return expm(-t*lpower)


def H(n,delta):
    gamma=PI/3 + 2*PI*n/3
    return math.log(2/math.sqrt(1+delta*delta))-delta*(gamma-math.atan(delta))


def threshold(n):
    assert n>=1
    lo,hi=0.0,math.sqrt(3)
    for _ in range(95):
        mid=(lo+hi)/2
        if H(n,mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def window_count(delta):
    B=math.atan(delta)+math.log(2/math.sqrt(1+delta*delta))/delta
    return math.ceil(3*(B-PI/3)/(2*PI))

checks=0
for alpha in [.2,.5,1.,1.001,1.5,2.,2.4,2.570230659,2.6,2.745,2.8,2.9,2.99,3.]:
    for t in [.001,.04,.17,.7,1.5,3.0,9.0,30.0]:
        row=q(alpha,t)
        actual=independent_exp(alpha,t)
        assert max(abs(actual[0,j]-row[j]) for j in range(3))<3e-10
        assert abs(sum(row)-1)<1e-12
        assert sum(x < -1e-12 for x in row)<=1
        if alpha<=1:assert min(row)>-1e-12
        checks+=4

for n in range(1,40):
    delta=threshold(n)
    assert abs(H(n,delta))<1e-12
    assert H(n,max(delta-1e-5,0))>=0
    assert H(n,delta+1e-5)<=0
    alpha=6*math.atan(1/delta)/PI
    gamma=PI/3+2*PI*n/3
    sp=gamma-math.atan(delta)
    tp=sp/(3**(alpha/2)*math.sin(PI*alpha/6))
    component=(n+2)%3 # n=1 -> j=0, n=2 -> j=1, n=3 -> j=2
    assert abs(q(alpha,tp)[component])<1e-10
    checks+=5

rng=random.Random(20261117)
for _ in range(200):
    alpha=rng.uniform(1.001,2.998)
    theta,radius,d=params(alpha)
    N=window_count(d)
    assert N>=1
    for n in range(min(N+2,160)):
        gamma=PI/3+2*PI*n/3
        s=gamma-math.atan(d)
        if s<=0:continue
        qt=q(alpha,s/(radius*math.sin(theta)))
        j=(n+2)%3
        if n<N:assert qt[j]<0, (alpha,n,N,qt[j])
        elif n>N:assert qt[j]>0
        else:assert qt[j]>=-1e-12
        checks+=1

for alpha in [2.9,2.99,2.999]:
    theta,rad,d=params(alpha)
    N=window_count(d)
    approx=3*math.log(2)/(2*PI*d)
    assert abs(N/approx-1)<.15
    checks+=1

print('PASS',checks,'supplementary assertions')
print('First reentry order',6*math.atan(1/threshold(1))/PI)
