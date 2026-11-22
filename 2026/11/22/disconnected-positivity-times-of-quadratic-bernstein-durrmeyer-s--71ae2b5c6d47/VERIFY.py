#!/usr/bin/env python3
"""Exact rational spectral identities and finite checks for Durrmeyer power positivity.
This script is supplementary; the continuum and real-exponent theorem has an analytic proof.
"""
from fractions import Fraction as F
import math

checks = 0

def check(value, message):
    global checks
    assert value, message
    checks += 1

def add(a, b):
    r = [F(0)] * max(len(a), len(b))
    for i, c in enumerate(a): r[i] += c
    for i, c in enumerate(b): r[i] += c
    return r

def scale(a, t):
    return [t*c for c in a]

def mul(a, b):
    r = [F(0)]*(len(a)+len(b)-1)
    for i, c in enumerate(a):
        for j, d in enumerate(b): r[i+j] += c*d
    return r

def integral(a):
    return sum((v/F(i+1) for i,v in enumerate(a)), F(0))

def bernstein(n):
    if n == 1: return [[F(1),F(-1)],[F(0),F(1)]]
    if n == 2: return [[F(1),F(-2),F(1)],[F(0),F(2),F(-2)],[F(0),F(0),F(1)]]
    raise ValueError('n=1 or n=2')

def kernel(n):
    B = bernstein(n)
    out = {}
    for p in B:
        for i,c in enumerate(p):
            for j,d in enumerate(p):
                out[i,j] = out.get((i,j), F(0)) + (n+1)*c*d
    return out

def eig_check(K,p,lam):
    q = [F(0)] * (max(i for i,j in K)+1)
    for (i,j),c in K.items():
        for k,d in enumerate(p): q[i] += c*d/F(j+k+1)
    check(q[:len(p)] == scale(p,lam) and all(v==0 for v in q[len(p):]),f'bad eigen {p}: {q}')

p1=[F(-1),F(2)]
p2=[F(1),F(-6),F(6)]
K1 = kernel(1)
K2 = kernel(2)
eig_check(K1,[F(1)],F(1));eig_check(K1,p1,F(1,3))
eig_check(K2,[F(1)],F(1));eig_check(K2,p1,F(1,2));eig_check(K2,p2,F(1,10))

for n,K in [(1,K1),(2,K2)]:
    B = bernstein(n)
    check(all(integral(b)==F(1,n+1) for b in B),'Bernstein integrals')
    check(all(K[i,j]==K[j,i] for i,j in K),'symmetry')
    check(all(sum((c/F(j+1) for (ii,j),c in K.items() if ii==i), F(0)) == (F(1) if i==0 else F(0)) for i,j in K),'row mass')

# Independently reconstruct the whole integer-power kernels via polynomial compositions.
def compose(K,L):
    out = {}
    for (i,j), a in K.items():
        for (k,l), b in L.items():
            out[i,l] = out.get((i,l), F(0)) + a*b/F(j+k+1)
    return out

def spectrum(n,t):
    lam = [F(1),F(1,3) if n==1 else F(1,2)]
    pol = [[F(1)],p1]
    norms=[F(1),F(3)]
    if n==2:
        lam.append(F(1,10));pol.append(p2);norms.append(F(5))
    out = {}
    for val,p,norm in zip(lam,pol,norms):
        for i,c in enumerate(p):
            for j,d in enumerate(p):
                out[i,j] = out.get((i,j), F(0)) + norm*(val**t)*c*d
    return out

for n,K in ((1,K1),(2,K2)):
    power = K
    for t in range(1,5):
        S = spectrum(n,t)
        check(all(power.get(key,F(0))==S.get(key,F(0)) for key in set(power)|set(S)),f'power n={n},t={t}')
        power = compose(power,K)

def a(t): return 2.0**(-t)
def b(t): return 10.0**(-t)
def lower(t): return 1.0 - 2.5*b(t) - .3*(2.5**t)
def upper(t): return 1.0 - 3.0*a(t) + 5.0*b(t)
def kernel_power(t,x,y):
    u=2*x-1;v=2*y-1
    return 1+3*a(t)*u*v+1.25*b(t)*(3*u*u-1)*(3*v*v-1)
def minimum(t): return lower(t) if t<=1 else upper(t)

def bisect(fun,lo,hi):
    flo=fun(lo)
    check(flo*fun(hi)<0,'invalid root bracket')
    for _ in range(150):
        mid=(lo+hi)/2
        if fun(mid)*flo <=0: hi=mid
        else: lo=mid; flo=fun(mid)
    return (lo+hi)/2

lo=bisect(lower,.8,.95)
hi=bisect(upper,1.05,1.3)
check(abs(lo-.8912898099509343)<2.e-14,'lower root')
check(abs(hi-1.1309462648000736)<2.e-14,'upper root')
check(abs(lower(lo))<2e-14 and abs(upper(hi))<2e-14,'root residuals')

for t in (.1,.6,.8,.9,1.,1.05,1.1,1.2,1.5,2.,3.,5.):
    p=min(1.,5.**(t-1.))
    witness=kernel_power(t,1.,(1.-p)/2.)
    check(abs(witness-minimum(t))<3e-14,f'wrong minimizer {t}')
    for i in range(51):
        for j in range(51):
            x=i/50;y=j/50
            check(kernel_power(t,x,y) >= minimum(t)-2e-14, f'bound violated {t}:{x},{y}')

for t,expected in ((.5,False),(.9,True),(1.,True),(1.05,False),(1.2,True),(2.,True)):
    check((minimum(t)>=-1e-14)==expected,f'wrong sign {t}')

# Degree one has one connected positivity interval.
for t in (.25,.5,1.,1.01,2.,3.):
    mn=1-3**(1-t)
    check((mn>=-1e-14)==(t>=1.),'degree-one threshold')

print(f'VERIFIED {checks} checks; transitions tau-={lo:.15f}, tau+={hi:.15f}')
