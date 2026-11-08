"""Reproduce direct spherical pair simulation and independent Crofton quadrature.

Requires only the Python standard library.  Randomness is seeded.
No finite experiment is used as a proof of the continuum identity.
"""
import math
import random

PI = math.pi

def formula(beta):
    t = math.tan(beta/2)
    return t*(1-t)**2/2

def integration(beta, steps=8000):
    # Integrate over normals with q=sin(beta)*sin(theta), regular at endpoints.
    s=math.sin(beta)
    c=math.cos(beta)
    def f(theta):
        q=s*math.sin(theta)
        h=math.acos(max(-1.0,min(1.0,c/math.sqrt(1-q*q))))
        return (PI-2*h-math.sin(2*h))*s*math.cos(theta)
    step=(PI/2)/steps
    v=f(0)+f(PI/2)
    for j in range(1,steps):
        v+=(4 if j%2 else 2)*f(j*step)
    unconditional=(step*v/3)/(4*PI)
    mass=(1+c)/2
    return unconditional/mass**2

def sample(beta, n=240000, seed=70218):
    rng=random.Random(seed)
    lower=-math.cos(beta)
    fail=0
    for _ in range(n):
        z1=lower+(1-lower)*rng.random()
        z2=lower+(1-lower)*rng.random()
        a1=2*PI*rng.random()
        a2=2*PI*rng.random()
        r1=math.sqrt(1-z1*z1)
        r2=math.sqrt(1-z2*z2)
        dot=z1*z2+r1*r2*math.cos(a2-a1)
        alpha=math.acos(max(-1,min(1,dot)))
        if alpha<1e-12 or abs(alpha-PI)<1e-12:
            continue
        b=(z2-z1*math.cos(alpha))/math.sin(alpha)
        # z-coordinate along minor great circle: z1 cos u + b sin u.
        u=(math.atan2(b,z1)+PI)%(2*PI)
        zmin=(-math.hypot(z1,b) if u<alpha else min(z1,z2))
        if zmin<lower:
            fail+=1
    return fail/n

if __name__=='__main__':
    for i,beta in enumerate((.12,.35,2*math.atan(1/3),.92,1.3,1.48)):
        expected=formula(beta)
        via_integral=integration(beta)
        assert abs(via_integral-expected)<3e-7,(beta,via_integral,expected)
        empirical=sample(beta,seed=417+i)
        se=math.sqrt(expected*(1-expected)/240000)
        assert abs(empirical-expected)<5*se+0.00015,(beta,empirical,expected)
        print('beta=%.9f exact=%.9f integral=%.9f direct_MC=%.9f se=%.9f'%(beta,expected,via_integral,empirical,se))
    assert abs(formula(2*math.atan(1/3))-2/27)<1e-15
    print('SPHERICAL_CAP_SHARP_GEODESIC_NONCONVEXITY_OK')
