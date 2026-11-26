#!/usr/bin/env python3
"""Exact, dependency-free coefficient verification for a finite Blaschke witness.
All computations use fractions; global disk mapping/univalence use the paper proof.
"""
from fractions import Fraction as F

N=5
Z=F(0)

def c(a):
    out=[Z]*N
    for j,x in enumerate(a):
        if j<N: out[j]=F(x)
    return out

def add(a,b): return [a[i]+b[i] for i in range(N)]
def neg(a): return [-x for x in a]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    return [sum((a[j]*b[k-j] for j in range(k+1)),Z) for k in range(N)]
def div(a,b):
    assert b[0]
    q=[Z]*N
    for k in range(N):
        q[k]=(a[k]-sum((q[j]*b[k-j] for j in range(k)),Z))/b[0]
    return q

def power(a,k):
    r=c([1])
    for _ in range(k): r=mul(r,a)
    return r

z=c([0,1])
w=div(c([0,1,-3,9]),c([9,-3,1]))
assert w == c([0,F(1,9),F(-8,27),F(8,9),F(80,243)])
# Independent finite-Blaschke identity: w=z (a+z (z-t)/(1-t*z)) / (1+a*z*(z-t)/(1-t*z))
a=F(1,9);t=F(3,10)
w2=div(c([-t,1]),c([1,-t]))
w1=div(add(c([a]),mul(z,w2)),add(c([1]),mul(c([0,a]),w2)))
assert mul(z,w1)==w
p=sub(add(add(c([1]),w),[v/F(3) for v in power(w,2)]),[v/F(9) for v in power(w,3)])
assert p==c([1,F(1,9),F(-71,243),F(5687,6561),F(2792,6561)])
# If f(z)=z+b2*z²+b3*z³+b4*z⁴+b5*z⁵+..., then
# (z*f'(z))/(odd(f)) = 1+2b2*z+2b3*z²+(4b4-2b2*b3)*z³+(4b5-2b3²)*z⁴+...
b2=p[1]/2
b3=p[2]/2
b4=(p[3]+2*b2*b3)/4
b5=(p[4]+2*b3*b3)/4
assert [b2,b3,b4,b5]==[F(1,18),F(-71,486),F(11161,52488),F(55297,472392)]
f=c([0,1,b2,b3,b4])
# Directly verify the defining relation through coefficient z^4 using series of
# (f(z)-f(-z))/(2z)=1+b3*z²+b5*z⁴.
numer=c([1,2*b2,3*b3,4*b4,5*b5])
denom=c([1,0,b3,0,b5])
assert div(numer,denom)==p
H=2*b2*b3*b4-b3**3-b4**2+b3*b5-b2*b2*b5
assert H==F(-173595619,2754990144)
assert (-H-F(769,12288))==F(75810133,176319369216)>0
assert (-H-F(1,16))==F(1408735,2754990144)>0
print('PASS: rational Schwarz coefficients, finite-Blaschke expansion, defining series identity, four function coefficients, determinant, two strict bound violations')
print('H=',H)
print('|H|-769/12288=',-H-F(769,12288))
print('|H|-1/16=',-H-F(1,16))
