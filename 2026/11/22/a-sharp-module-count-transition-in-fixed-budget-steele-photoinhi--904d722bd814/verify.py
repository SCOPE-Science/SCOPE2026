#!/usr/bin/env python3
"""Standalone deterministic numerical checks for a fixed-load Steele photoinhibition allocation theorem.

All global claims in the accompanying manuscript are established analytically;
these finite numerical checks are not substitutes for its proof.
Requires only the Python standard library. Run: python verify.py
"""
import math
import random

CHECKS = 0

def verify(p, description=''):
    global CHECKS
    CHECKS += 1
    if not p:
        raise AssertionError(f'{description} (check {CHECKS})')

def f(x):
    return x * math.exp(-x)

def fp(x):
    return (1.0-x) * math.exp(-x)

def fpp(x):
    return (x-2.0) * math.exp(-x)

def u(d):
    return d/math.expm1(d)

def up(d):
    t=math.expm1(d)
    return (t-d*(t+1.0))/(t*t)

def upp(d):
    e=math.exp(d)
    return e*((d-2.0)*e+d+2.0)/(e-1.0)**3

def S(n,d):
    return n+d+n*u(d)

def Q(n,d):
    a=1.0+u(d)
    b=a+d
    total=S(n,d)
    return (n-1)*f(a)+f(b)-n*f(total/n)

def bisect(fn,lo,hi,positive_to_right=True):
    flo=fn(lo)
    fhi=fn(hi)
    verify(flo < 0 < fhi if positive_to_right else flo > 0 > fhi,
           f'bracket {lo=} {hi=} {flo=} {fhi=}')
    for _ in range(90):
        md=(lo+hi)/2.0
        v=fn(md)
        if (v>0)==positive_to_right:
            hi=md
        else:
            lo=md
    return (lo+hi)/2.0

def fold(n):
    return bisect(lambda d:1+n*up(d),0.001,20.0)

def jump(n):
    df=fold(n)
    return bisect(lambda d:Q(n,d),df,40.0)

def best(n,s):
    eq=n*f(s/n)
    if n==2:
        if s<=4.0:
            return eq,[s/2.0]*2
        d=bisect(lambda d:S(n,d)-s,1e-7,max(s,15.0))
        a=1+u(d)
        return f(a)+f(a+d),[a,a+d]
    df=fold(n)
    sc=S(n,jump(n))
    if s<=sc:
        return eq,[s/n]*n
    d=bisect(lambda d:S(n,d)-s,df,max(s,30.0))
    a=1+u(d)
    return (n-1)*f(a)+f(a+d),[a]*(n-1)+[a+d]

for n in range(2,36):
    for d in (0.002,0.01,0.1,0.25,0.4,0.9,1.3,2.0,3.0,5.0,9.0):
        verify(upp(d)>0,'u curvature')
        a=1+u(d)
        b=a+d
        verify(abs(fp(a)-fp(b))<5e-12,'stationarity balance')
        verify(1<a<2 and b>2,'stationary branch domain')
        verify(abs(S(n,d)-(n-1)*a-b)<3e-12,'conservation')
    if n==2:
        for s in [0.5,1.5,3.9,4.0,4.001,4.1,5,10,20]:
            opt,arr=best(n,s)
            verify(abs(sum(arr)-s)<1e-9,'budget')
            verify(opt>=n*f(s/n)-1e-12,'dominates equal')
        continue
    df=fold(n)
    dc=jump(n)
    sf=S(n,df)
    sc=S(n,dc)
    verify(0<df<dc,'branch ordering')
    verify(n<sf<sc<2*n,'critical load bounds')
    verify(abs(Q(n,dc))<1e-11,'equal/unequal crossover')
    verify(1+n*up(df)<1e-10 and 1+n*up(df)>-1e-10,'fold equation')
    verify(Q(n,df)<0,'fold below equal')
    verify(Q(n,2*n)>0 or 2*n<sf,'finite supercritical example')
    for frac in (0.1,0.25,0.5,0.75,1.0,1.2,1.5,2.0,3.0):
        s=(n if frac<1 else sf) + frac*(sc-sf if frac<1 else n)
        if s<=0: continue
        opt,arr=best(n,s)
        verify(abs(sum(arr)-s)<1e-9,'budget')
        verify(opt>=n*f(s/n)-1e-10,'opt dominates equal')
        if s>sc+1e-7:
            verify(max(arr)>2 and min(arr)<2,'symmetry broken')

r=random.Random(453333)
for n in range(2,11):
    svals=[1,2,3,4,5,n,n*1.2,n*1.7,n*2,n*2.8,n*4,50]
    for s in svals:
        opt,arr=best(n,s)
        verify(abs(sum(arr)-s)<5e-9)
        verify(abs(sum(map(f,arr))-opt)<2e-12)
        for _ in range(1250):
            zz=[r.expovariate(1) for _ in range(n)]
            den=sum(zz)
            zz=[s*x/den for x in zz]
            verify(sum(map(f,zz))<=opt+4e-10,'random simplex global check')

n=3
df=fold(n)
dc=jump(n)
sc=S(n,dc)
verify(abs(df-1.0356584794018922)<5e-12)
verify(abs(S(n,df)-5.745643576732724)<5e-12)
verify(abs(dc-1.3974995195938766)<5e-12)
verify(abs(sc-5.774313471725124)<5e-12)
opt,arr=best(3,7)
verify(abs(opt-0.7718350579247905)<5e-12)
verify(abs((opt/(3*f(7/3))-1)*100-13.70518053865979)<5e-10)
print(f'PASS {CHECKS} deterministic assertions')
print(f'n=3 fold d={df:.15f}, S_f={S(n,df):.15f}')
print(f'n=3 jump d={dc:.15f}, S_c={sc:.15f}')
print(f'n=3 S=7 allocation={arr} optimal F={opt:.15f}, equal F={3*f(7/3):.15f}')
