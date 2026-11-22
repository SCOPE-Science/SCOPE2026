"""Independent finite consistency checks for regular ideal polygon radial law.

Requires Python 3 and mpmath (pip install mpmath). Finite checks are not proofs.
"""
from __future__ import annotations
import math
import random
import mpmath as mp
mp.mp.dps = 55


def profile(n, t):
    n = int(n); t=mp.mpf(t)
    if t <= 0: return mp.mpf('0')
    phi = mp.pi / n
    rho = mp.atanh(mp.cos(phi))
    disk = 2*(mp.cosh(t)-1)/(n-2)
    if t <= rho: return disk
    # Robust computation for moderate t; avoid large t cancellation.
    beta = mp.acos(mp.cos(phi)/mp.tanh(t))
    gamma = mp.acos(mp.cot(phi)/mp.sinh(t))
    return disk - 2*n*(mp.cosh(t)*beta-gamma)/((n-2)*mp.pi)


def angular_fraction(n,t):
    phi=mp.pi/n
    rho=mp.atanh(mp.cos(phi))
    return 1 if t <=rho else 1-n/mp.pi*mp.acos(mp.cos(phi)/mp.tanh(t))


def density(n,t):
    return 2*mp.sinh(t)/(n-2)*angular_fraction(n,t)


def limit(s):
    s=mp.mpf(s); b=2/mp.pi; y=mp.exp(s)
    if y <= b:return y
    return y-mp.sqrt(y*y-b*b)+b*mp.acos(b/y)


def close(got, exp, tol=mp.mpf('1e-28')):
    assert abs(got-exp) < tol, (mp.nstr(got,16),mp.nstr(exp,16))

# Pointwise integration avoids assuming the antiderivative used in the CDF proof.
for n in [3,4,5,7,12,32,256]:
    rho=mp.atanh(mp.cos(mp.pi/n))
    for t in [rho/3,rho, rho+mp.mpf('.1'),rho+mp.mpf('.6'),rho+2]:
        q=mp.quad(lambda z:density(n,z),[0,min(rho,t)])
        if t>rho:q+=mp.quad(lambda z:density(n,z),[rho,t])
        close(q,profile(n,t))
    assert 0<profile(n,rho)<1
    assert profile(n,rho+6)<1

# Triangle: area uniform independent sampling in the upper half-plane ideal triangle (0,1,infinity).
# Density of x is Beta(1/2,1/2); conditional height y=sqrt(x(1-x))/U, U uniform(0,1).
random.seed(3242)
N=150000
samples=[]
for j in range(N):
    x=math.sin(math.pi*random.random()/2)**2
    y=math.sqrt(x*(1-x))/random.random()
    r=math.acosh(1+((x-0.5)**2+(y-math.sqrt(3)/2)**2)/(math.sqrt(3)*y))
    samples.append(r)
for t in [.18,.4,.55,1.,1.8]:
    obs=sum(z<=t for z in samples)/N
    pred=float(profile(3,t))
    assert abs(obs-pred)<.013,(t,obs,pred)

# Limit for the regular polygons. Both the sub-critical and supercritical branches.
for s in [-2,-.9,-.4,0,.8,2]:
    vals=[float(profile(n, mp.log(n)+s)) for n in [500,2000,10000]]
    assert abs(vals[-1]-float(limit(s))) < .0015,(s,vals,float(limit(s)))
    assert abs(vals[2]-float(limit(s))) < abs(vals[0]-float(limit(s))) + 1e-9

b=2/mp.pi
close(limit(mp.log(b)),b)
close(limit(10)+b*b/(2*mp.exp(10)),1,mp.mpf('1e-9'))
for n in [3,4,7,15]:
    rho=mp.atanh(mp.cos(mp.pi/n))
    c=(4*n*mp.sqrt(2*mp.cos(mp.pi/n)))/(3*(n-2)*mp.pi)
    for h in [mp.mpf('1e-5'),mp.mpf('1e-6')]:
        deficit=2*(mp.cosh(rho+h)-1)/(n-2)-profile(n,rho+h)
        assert abs(deficit/h**mp.mpf('1.5')/c-1)<.01
print('REGULAR_IDEAL_POLYGON_CHECKS_OK: quadrature, independent area sampling, cusp and many-side limits')
