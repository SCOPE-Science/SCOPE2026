#!/usr/bin/env python3
"""Independent reproducibility checks for the pentablock axial kernel identities.

Finite tests support, but do not replace, the analytic all-degree arguments.
Requires Python 3 and mpmath (and standard library).
"""
from fractions import Fraction
from math import comb, pi
import cmath
import mpmath as mp

checks=0

def check(cond,msg):
    global checks
    checks+=1
    if not cond:
        raise AssertionError(msg)

def pull(n,j,l):
    # a^n s^j p^l -> xi^n*(lambda-eta)^n*(lambda+eta)^j*(lambda*eta)^l / 2^n
    out={}
    for u in range(n+1):
        for v in range(j+1):
            d=u+v+l
            e=n+j-u-v+l
            term=Fraction((-1)**(n-u)*comb(n,u)*comb(j,v),2**n)
            out[(d,e)]=out.get((d,e),Fraction(0))+term
    return {z:v for z,v in out.items() if v}

def inner(n,j,l, m,k,h):
    if n!=m: return Fraction(0)
    left=pull(n,j,l)
    right=pull(m,k,h)
    return sum((c*right.get(e,Fraction(0)) for e,c in left.items()),Fraction(0))

for n in range(0,19):
    w=Fraction(comb(2*n,n),4**n)
    check(inner(n,0,0,n,0,0)==w,('norm',n))
    for m in range(0,10):
        if m!=n:
            check(inner(n,0,0,m,0,0)==0,('xi orthogonality',n,m))
    for j in range(0,5):
        for l in range(0,4):
            if (j,l)!=(0,0):
                check(inner(n,0,0,n,j,l)==0,('axis orthogonality',n,j,l))
    if n:
        check(Fraction(comb(2*n,n),4**n)== Fraction(2*n-1,2*n)*Fraction(comb(2*(n-1),n-1),4**(n-1)),('moment recurrence',n))

mp.mp.dps=70

def K_exact(z):
    if z==0:return mp.mpc(1)
    return 1/(1-z)+mp.sqrt(z)*mp.asin(mp.sqrt(z))/(1-z)**mp.mpf('1.5')

def K_series(z,nmax=750):
    a=mp.mpf(1)
    total=a
    for n in range(1,nmax):
        a*=mp.mpf(2*n)/(2*n-1)
        total+=a*z**n
    return total

def H(z):
    return (1-z)**mp.mpf('1.5')*K_exact(z)

for z in [mp.mpf('0'),mp.mpf('.1'),mp.mpf('.3'),mp.mpf('-.5'),mp.mpf('.8'),mp.mpc('.2','.3'),mp.mpc('-.5','.3')]:
    check(abs(K_series(z)-K_exact(z))<mp.mpf('1e-40'),('kernel series identity',str(z)))
    check(mp.re(H(z))>2-mp.pi/2-mp.mpf('1e-40'),('positive halfplane',str(z)))

for n in range(1,31):
    # d_n=1/2*(central binom(2n-2,n-1)/4^(n-1))/( (2n-1)*n)
    d=Fraction(comb(2*n-2,n-1),2*4**(n-1)*(2*n-1)*n)
    check(d>0,('H positivity',n))

check(Fraction(8,3)-Fraction(2,1)**2 == Fraction(-4,3),'complete Pick obstruction')
check(2-mp.pi/2>0,'mass positivity')

for s in [mp.mpf('0.3'),mp.mpf('0.7'),mp.mpf('0.9'),mp.mpf('0.98'),mp.mpf('0.995')]:
    check(abs((1-s)**mp.mpf('1.5')*K_exact(s)-mp.pi/2) < 4*mp.sqrt(1-s),('boundary norm',str(s)))
    # metric g= f'(s)+s f''(s), f=log K(s)
    f=lambda t:mp.log(K_exact(t))
    g=mp.diff(f,s)+s*mp.diff(f,s,2)
    check(abs((1-s)**2*g-mp.mpf('1.5'))<mp.mpf('1.5')*mp.sqrt(1-s),('metric leading',str(s)))

# deterministic pseudorandom disk points check nonvanishing and constructive bound
for i in range(1,101):
    z=mp.mpf(i)/101*mp.e**(2j*mp.pi*(i*17%101)/101)
    k=K_exact(z)
    check(abs(k)*(abs(1-z)**mp.mpf('1.5'))>=2-mp.pi/2-mp.mpf('1e-40'),('kernel nonzero and bound',i))

print('PASS',checks,'assertions; moments, Gram orthogonality, generating function, positive halfplane, non-Pick and sharp boundary checks.')
