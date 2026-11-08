#!/usr/bin/env python3
"""Independent finite-dimensional checks for Bell-reset age-mixture concurrence."""
import cmath
import math
import random

rng = random.Random(40638)
checks = 0

def assert_close(a, b, tol=2e-11):
    global checks
    assert abs(a-b) <= tol, (a,b)
    checks += 1

def su2(theta, axis):
    nx, ny, nz = axis
    co=math.cos(theta/2)
    si=math.sin(theta/2)
    return ((co-1j*si*nz, -1j*si*(nx-1j*ny)),
            (-1j*si*(nx+1j*ny), co+1j*si*nz))

def mul(U,v):
    return (U[0][0]*v[0]+U[0][1]*v[1], U[1][0]*v[0]+U[1][1]*v[1])

def concurrence(weights, theta, axis):
    U=su2(theta, axis)
    v=(math.sqrt(.5)+0j,math.sqrt(.5)+0j)
    off=0j
    for wm in weights:
        off += wm*v[0]*v[1].conjugate()
        v=mul(U,v)
    return 2*abs(off)

def cosine(weights, theta):
    return sum(w*math.cos(m*theta) for m,w in enumerate(weights))

for _ in range(300):
    mmax=rng.randint(2, 35)
    raw=[rng.random() for _ in range(mmax)]
    weights=[v/sum(raw) for v in raw]
    theta=rng.random()*2*math.pi
    raw_axis=[rng.gauss(0,1) for _ in range(3)]
    norm=math.sqrt(sum(x*x for x in raw_axis))
    axis=tuple(x/norm for x in raw_axis)
    f=cosine(weights,theta)
    c=concurrence(weights,theta,axis)
    assert c+1e-10 >= f-1e-10
    assert_close(concurrence(weights,theta,(0.,1.,0.)),abs(f))
    checks += 1

for k in range(2,45):
    deterministic=[1/k]*k
    assert_close(cosine(deterministic,2*math.pi/k),0,3e-14)
    assert_close(concurrence(deterministic,2*math.pi/k,(0.,1.,0.)),0,3e-14)
    p=1/k
    weights=[p*(1-p)**j for j in range(15000)]
    assert_close(sum(weights),1,2e-12)
    expected=p/(2-p)
    assert_close(cosine(weights,math.pi),expected,2e-12)
    assert_close(concurrence(weights,math.pi,(0.,0.,1.)),expected,2e-12)
    checks+=1

for _ in range(100):
    p=rng.uniform(0.03,1)
    weights=[p*(1-p)**j for j in range(1200)]
    theta=rng.random()*2*math.pi
    x=math.cos(theta)
    closed=p*(1-(1-p)*x)/(1-2*(1-p)*x+(1-p)**2)
    assert_close(cosine(weights,theta),closed,1e-11)
    assert cosine(weights,theta)+1e-12>=p/(2-p)
    checks+=1

# Logical z on the Bell reset toggles Bell + and Bell -: individual ages
# always have concurrence 1, while the two-age stationary average is separable.
assert_close(concurrence([.5,.5],math.pi,(0,0,1)),0)
assert_close(concurrence([1],math.pi,(0,0,1)),1)
assert_close(concurrence([0,1],math.pi,(0,0,1)),1)
print('PASS',checks,'independent finite-dimensional and clock checks')
