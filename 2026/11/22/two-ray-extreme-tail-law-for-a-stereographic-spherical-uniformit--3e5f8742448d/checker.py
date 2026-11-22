"""Standalone numerical checks for exact S^2 stereographic finite-sample tail constants."""
import math
import numpy as np
from scipy.integrate import quad

assertions = 0

def check(flag, msg):
    global assertions
    assertions += 1
    if not flag: raise AssertionError(msg)

# The one-pair variable Z = cot(theta/2) has F(z) = z^2/(1+z^2).
def single_tail(a, t):
    assert t > 2*math.sqrt(max(a,0))
    hi = 0.5*(t + math.sqrt(t*t - 4*a))
    if a > 0:
        lo = a/hi
        upper = 1/(1+hi*hi) + lo*lo/(1+lo*lo)
        lower = 0.0
    elif a == 0:
        upper = 1/(1+t*t)
        lower = 0.0
    else:
        lo = (-t + math.sqrt(t*t - 4*a))/2
        upper = 1/(1+hi*hi)
        lower = lo*lo/(1+lo*lo)
    return upper, lower

density = lambda z: 2*z/(1+z*z)**2
check(abs(quad(density,0,math.inf)[0]-1)<1e-11, "normalization")
check(abs(quad(lambda z:z*density(z),0,math.inf)[0]-math.pi/2)<1e-11,"mean")
for z in (0.5,1.,2.,5.):
    check(abs(quad(density,z,math.inf)[0]-1/(1+z*z))<1e-11, "upper cdf")
    check(abs(quad(density,0,1/z)[0]-1/(1+z*z))<1e-11, "reciprocal cdf")

for a in (-1.0,-0.75,-0.25,0.0,0.25,0.75,1.0):
    for t in (100.,1000.,10000.):
        up, down = single_tail(a,t)
        wanted_up = 1 + max(a,0)**2
        wanted_down = max(-a,0)**2
        # Error at t >=100 is O(1/t^2).
        check(abs(t*t*up-wanted_up)<0.002, f'upper a={a},t={t}')
        check(abs(t*t*down-wanted_down)<0.002, f'lower a={a},t={t}')

# Pairwise edge laws have the same marginals conditional on a shared vertex.
# Direct spherical sampling checks the new sum-tail coefficients at fixed n.
rng=np.random.default_rng(324241)
count=1_500_000
n=3
xyz=rng.standard_normal((count,n,3))
xyz/=np.linalg.norm(xyz,axis=2,keepdims=True)
pairs=((0,1),(0,2),(1,2))
D=np.stack([(xyz[:,i,:]*xyz[:,j,:]).sum(axis=1) for i,j in pairs],axis=1)
Z=np.sqrt((1+D)/(1-D))
for a in (-1.0, 0.0, 1.0):
    T=(2/n)*(Z+a/Z).sum(axis=1)-(n-1)*math.pi*(1+a)/2
    for t in (80.0,140.0):
        u=(T>t).mean()*t*t
        d=(T< -t).mean()*t*t
        cu=2*(n-1)/n*(1+max(a,0)**2)
        cd=2*(n-1)/n*max(-a,0)**2
        # Not an infinite proof: finite thresholds with binomial error and O(t^-1) remainder.
        check(abs(u-cu)<0.70, f'MC upper a={a},t={t} observed={u} expected={cu}')
        check(abs(d-cd)<0.70, f'MC lower a={a},t={t} observed={d} expected={cd}')
        print(f'n={n} a={a:+.0f} t={t:4.0f} positive:t^2 P={u:.5f} -> {cu:.5f} negative:{d:.5f} ->{cd:.5f}')
print(f'PASS {assertions} checks')
