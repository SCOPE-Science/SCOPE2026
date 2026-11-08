#!/usr/bin/env python3
"""Independent arithmetic/numerical spot checks of the two-ray intensity reconstruction identities.
Only Python standard library is needed. This finite test is not the proof for all degrees.
"""
import cmath
import math
import random
from fractions import Fraction
import mpmath as mp
mp.mp.dps=90

rng = random.Random(283746)
checks = 0


def coefficients_from_values(nodes, values):
    """Lagrange coefficient interpolation in floating point; input arrays length m."""
    out = [mp.mpf(0)] * len(nodes)
    for j, xj in enumerate(nodes):
        basis = [mp.mpf(1)]
        denom = mp.mpf(1)
        for k, xk in enumerate(nodes):
            if k == j:
                continue
            nxt = [mp.mpf(0)] * (len(basis) + 1)
            for e, a in enumerate(basis):
                nxt[e] -= a * xk
                nxt[e+1] += a
            basis = nxt
            denom *= xj - xk
        for t, a in enumerate(basis):
            out[t] += (values[j] / denom) * a
    return out


def times_polynomial(nodes):
    a = [mp.mpf(1)]
    for x in nodes:
        b = [mp.mpf(0)] * (len(a)+1)
        for e, ce in enumerate(a):
            b[e] -= ce*x
            b[e+1] += ce
        a = b
    return a


def intensity_coeffs(a, ang):
    d = len(a)-1
    out = [mp.mpf(0)]*(2*d+1)
    for j in range(d+1):
        for k in range(d+1):
            out[j+k] += (a[j]*a[k].conjugate()*mp.exp(mp.j*(j-k)*ang)).real
    return out


def poly(a, x):
    z=0
    for c in reversed(a):
        z=z*x+c
    return z


def evaluate_coeffs(a,x):
    res=mp.mpf(0)
    for c in reversed(a):
        res=res*x+c
    return res

for d in range(1,7):
    theta=mp.pi/(d+1)
    n=2*d
    r0 = [(mp.mpf(2*j+1)/2)/(4*d+7) for j in range(1,n+1)]
    r1 = [(mp.mpf(2*j+3)/2)/(4*d+7) for j in range(1,n+1)]
    v0=times_polynomial(r0)
    v1=times_polynomial(r1)
    assert abs(v0[0]-v1[0])>mp.mpf("1e-70")
    for sample in range(20):
        a=[mp.mpc(rng.randint(-10,10)/11, rng.randint(-10,10)/11) for _ in range(d+1)]
        I0=coefficients_from_values(r0,[abs(poly(a,r))**2 for r in r0])
        I1=coefficients_from_values(r1,[abs(poly(a,r*mp.exp(mp.j*theta)))**2 for r in r1])
        c=(I1[0]-I0[0])/(v0[0]-v1[0])
        assert abs(c-abs(a[d])**2)<mp.mpf("1e-65"), (d,sample,c,abs(a[d])**2)
        for k in range(2*d+1):
            expected0=intensity_coeffs(a,0)[k]
            expected1=intensity_coeffs(a,theta)[k]
            got0=(I0[k] if k<2*d else 0)+c*v0[k]
            got1=(I1[k] if k<2*d else 0)+c*v1[k]
            assert abs(got0-expected0)<mp.mpf("1e-65"), (d,k,got0,expected0)
            assert abs(got1-expected1)<mp.mpf("1e-65"), (d,k,got1,expected1)
            checks+=2
        for _ in range(8):
            t=mp.mpf(rng.randint(1,35))/100
            for theta_i,I,V in [(0,I0,v0),(theta,I1,v1)]:
                got=evaluate_coeffs(I,t)+c*evaluate_coeffs(V,t)
                exp=abs(poly(a,t*mp.exp(mp.j*theta_i)))**2
                assert abs(got-exp)<mp.mpf("1e-65"),(d,t,got,exp)
                checks+=1

# Necessary angular boundary, including every resonance order and off-grid radii.
for d in range(1,9):
    for m in range(1,d+1):
        theta=math.pi/m
        for j in range(21):
            t=(j+1)/25
            p=lambda z: 1+1j*z**m
            q=lambda z: 1-1j*z**m
            assert abs(abs(p(t))**2-abs(q(t))**2)<1e-10
            z=t*cmath.exp(1j*theta)
            assert abs(abs(p(z))**2-abs(q(z))**2)<1e-10
            checks+=2

# Exact rational identity on ray at theta=pi/2 when d=1.
from fractions import Fraction as F
x=[F(1,7),F(2,7)]
y=[F(2,7),F(3,7)]
# p(z)=1+(2+3i)z, so |p(t)|^2=1+4t+13t^2; |p(it)|^2=1-6t+13t^2.
def lagrange2(nodes,values):
    t0,t1=nodes
    a=(values[1]-values[0])/(t1-t0)
    b=values[0]-a*t0
    return [b,a]
C0=[F(1),F(4),F(13)]
C1=[F(1),F(-6),F(13)]
I0=lagrange2(x,[sum(c*t**k for k,c in enumerate(C0)) for t in x])
I1=lagrange2(y,[sum(c*t**k for k,c in enumerate(C1)) for t in y])
V0=[x[0]*x[1],-(x[0]+x[1]),F(1)]
V1=[y[0]*y[1],-(y[0]+y[1]),F(1)]
c=(I1[0]-I0[0])/(V0[0]-V1[0])
assert c==13
assert [I0[k]+c*V0[k] for k in range(2)]+[c]==C0
assert [I1[k]+c*V1[k] for k in range(2)]+[c]==C1
checks+=3
print('TWO_RAY_PROFILE_CHECKS_PASS',checks,'degrees 1..6 plus resonant boundaries 1..8')
