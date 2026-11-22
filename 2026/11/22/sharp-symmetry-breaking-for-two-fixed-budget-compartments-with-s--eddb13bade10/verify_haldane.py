#!/usr/bin/env python3
"""Standalone exact-algebra and deterministic numerical checks for a two-compartment
Haldane response with fixed total substrate. Requires sympy for exact symbolic replay.
This program is supporting finite verification; the global theorem follows from the proof.
"""
import math
import random
import sympy as sp

a,m,d,z=sp.symbols('a m d z', real=True, positive=True)
def f(x):
    return x/(1+a*x+x*x)
B=1+a*m+m*m
F=sp.cancel(f(m-d)+f(m+d))
P=(a+m)*z*z-2*m*B*z+B*(m**3-3*m-a)
Dminus=1+a*(m-d)+(m-d)**2
Dplus=1+a*(m+d)+(m+d)**2
checks=0

def assert_eq(l, r):
    global checks
    assert sp.cancel(l-r)==0, f'failed: {sp.factor(l-r)}'
    checks+=1

assert_eq(sp.diff(F,d),4*d*P.subs(z,d*d)/(Dminus**2*Dplus**2))
assert_eq(P.subs(z,m*m),-(a*a*m+4*a*m*m+a+4*m**3+3*m))
assert_eq(sp.discriminant(P,z),4*(a+2*m)**2*B)
assert_eq(sp.diff(f(m),m,2),2*(m**3-3*m-a)/(1+a*m+m*m)**3)
assert_eq(sp.diff(f(m),m), (1-m*m)/(1+a*m+m*m)**2)

rng=random.Random(20261120)
for _ in range(600):
    aa=sp.Rational(rng.randint(1,20),rng.randint(1,10))
    mm=sp.Rational(rng.randint(1,50),rng.randint(1,10))
    dd=mm*sp.Rational(rng.randint(0,100),100)
    subs={a:aa,m:mm,d:dd}
    actual=F.subs(subs)
    assert actual>=0
    assert_eq(actual,f(mm-dd).subs(a,aa)+f(mm+dd).subs(a,aa))

for aval in [0.05,0.2,0.5,1,2,5,10,30,100]:
    lo,hi=math.sqrt(3),max(5,aval+5)
    while hi**3-3*hi-aval<=0:hi*=2
    for _ in range(90):
        mid=(lo+hi)/2
        if mid**3-3*mid-aval<0:lo=mid
        else:hi=mid
    mc=(lo+hi)/2
    for rel in [0.15,0.4,0.9,0.999,1.001,1.01,1.1,1.5,2,5,20]:
        M=mc*rel
        bb=1+aval*M+M*M
        if M>mc:
            zm=(M*bb-(aval+2*M)*math.sqrt(bb))/(aval+M)
            assert zm>0 and zm<M*M
            dst=math.sqrt(zm)
        else:dst=0
        Fnum=lambda D:(M-D)/(1+aval*(M-D)+(M-D)**2)+(M+D)/(1+aval*(M+D)+(M+D)**2)
        optimum=Fnum(dst)
        for k in range(101):
            D=M*k/100
            assert Fnum(D)<=optimum+5e-12, (aval,M,D,dst, Fnum(D),optimum)
            checks+=1
        if M>mc:
            assert Fnum(dst)>Fnum(0)
            checks+=1

# Exact closed-form rational example at a=1, mean=3: numerical output only.
M=3.0;alpha=1.0;BB=1+alpha*M+M*M
zmin=(M*BB-(alpha+2*M)*math.sqrt(BB))/(alpha+M)
D=math.sqrt(zmin)
response=lambda x:x/(1+alpha*x+x*x)
print('symbolic-and-grid checks:',checks)
print('example a=1, m=3: d =',f'{D:.12f}', 'concentrations =',f'{M-D:.12f}',f'{M+D:.12f}')
print('equal total response =',f'{2*response(M):.12f}','optimal response =',f'{response(M-D)+response(M+D):.12f}')
print('relative gain percent =',f'{100*((response(M-D)+response(M+D))/(2*response(M))-1):.9f}')
print('All symbolic identities and deterministic grid assertions passed.')
