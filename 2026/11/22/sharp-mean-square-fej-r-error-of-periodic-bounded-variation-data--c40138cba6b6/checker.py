"""Standalone mathematical checks for the Fejer variation-error asymptotic.
No external data, network connections or mutable state are required.
"""
from fractions import Fraction as Q
from math import factorial, pi, sin, cos, sqrt
from scipy.special import sici
from scipy.optimize import brentq
import numpy as np


def atan_interval(z, terms):
    s=sum(((-1)**j * z**(2*j+1)/Q(2*j+1) for j in range(terms)), Q(0))
    rem=z**(2*terms+1)/Q(2*terms+1)
    return (s-rem,s) if terms%2 else (s,s+rem)

lo5,hi5=atan_interval(Q(1,5),12)
lo239,hi239=atan_interval(Q(1,239),12)
pl,pu=16*lo5-4*hi239,16*hi5-4*lo239
assert Q(314159,100000)<pl<pu<Q(314160,100000)
# Alternating sine-integral series at pi; bound each positive term using exact rational arithmetic.
sil=Q(0);siu=Q(0)
for j in range(13):
    tlo=pl**(2*j+1)/Q((2*j+1)*factorial(2*j+1))
    thi=pu**(2*j+1)/Q((2*j+1)*factorial(2*j+1))
    if j%2==0:sil+=tlo;siu+=thi
    else:sil-=thi;siu-=tlo
# The first omitted term (j=13) is negative.
nextterm=pu**27/Q(27*factorial(27))
sil-=nextterm
lhs_lower=1+pl*pl/2-pu*siu
rhs_upper=1/(pl*pl)
assert lhs_lower > rhs_upper
print('Exact rational comparison F(pi) > F(infty) + 1/(4 pi^4): PASS')

def FiniteE(N,d):
    k=np.arange(1,N,dtype=float)
    finite=np.sum((1/N**2-1/k**2)*(1-np.cos(2*pi*k*d))) if N>1 else 0
    return d*(1-d)/4 + finite/(4*pi*pi)

def LimitF(q):
    return (2-sin(q)/q-cos(q)+q*(pi/2-sici(q)[0]))/(4*pi*pi)

def LimitD(q):
    return pi/2-sici(q)[0]+(sin(q)-q*cos(q))/q**2
qstar=brentq(LimitD,pi,4.0,xtol=1e-14)
fstar=LimitF(qstar)
assert 3.34431<qstar<3.34433
assert .0537105<fstar<.0537106
assert 0.53226<qstar/(2*pi)<0.53227
# Verify the exact finite Fourier-Bernoulli summation independently with a truncated Fourier tail.
checks=0
for N in [1,2,3,4,7,11,20]:
    kk=np.arange(1,150001,dtype=float)
    aa=np.minimum(kk/N,1)
    for d in [1/(2*N+2),0.07,0.19,0.31,0.5]:
        e1=FiniteE(N,d)
        e2=np.sum(aa*aa*(1-np.cos(2*pi*kk*d))/(kk*kk))/(4*pi*pi)
        assert abs(e1-e2)<3.5e-7,(N,d,e1,e2)
        checks+=1
# Positive finite peak against asymptotic and localization; no finite experiments prove the limit.
for N in [5,10,30,100,300]:
    ds=np.linspace(0,.5,10001)
    vals=np.array([FiniteE(N,d) for d in ds])
    d=ds[vals.argmax()]
    assert abs(N*d-qstar/(2*pi))<0.025
    assert abs(N*vals.max()-fstar)<0.001
    checks+=1
print('Finite checks:',checks,'PASS')
print('qstar:',qstar,'scale:',qstar/(2*pi),'sharp squared coefficient:',fstar,'sharp norm coefficient:',sqrt(fstar))
