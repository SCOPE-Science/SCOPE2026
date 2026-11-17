"""Independent finite diagnostics for the small-hole four-point convexity expansion.

Run: python check_sylvester_annulus.py (requires numpy). Simulation is
supporting evidence, not a proof of the asymptotic assertions.
"""
import math
import numpy as np

PI = math.pi
P0 = 1 - 35/(12*PI**2)
A1 = 1 - 19/(3*PI**2)
A2 = 1 - 95/(6*PI**2)
P1 = 3/4 - 4/(3*PI**2)
P2 = 1/2


def cross(a, b):
    return a.real*b.imag - a.imag*b.real


def in_triangle(p, a, b, c):
    v0, v1, v2 = b-a, c-a, p-a
    det = cross(v0, v1)
    l0 = cross(v2, v1)/det
    l1 = cross(v0, v2)/det
    return (l0 > 0) & (l1 > 0) & (l0+l1 < 1)


def convex_four(points):
    is_inside = np.zeros(points.shape[1], dtype=bool)
    for k in range(4):
        other = [points[i] for i in range(4) if i != k]
        is_inside |= in_triangle(points[k], *other)
    return ~is_inside


def uniform_disk(rng, n, radius=1.0):
    return radius*np.sqrt(rng.random(n))*np.exp(2j*PI*rng.random(n))


def uniform_annulus(rng, n, t):
    return np.sqrt(t+(1-t)*rng.random(n))*np.exp(2j*PI*rng.random(n))


def simulate_all(rng, t, n=700000, batch=100000):
    yes = 0
    for _ in range(n//batch):
        z = np.vstack([uniform_annulus(rng, batch, t) for j in range(4)])
        yes += np.count_nonzero(convex_four(z))
    return yes/n


def fixed_point_probability(rng, u, n=900000, batch=100000):
    yes = 0
    for _ in range(n//batch):
        z = np.vstack([np.full(batch, complex(u,0)),
                       *[uniform_disk(rng, batch) for j in range(3)]])
        yes += np.count_nonzero(convex_four(z))
    return yes/n


def two_inner_probability(rng, h, n=700000, batch=100000):
    yes=0
    for _ in range(n//batch):
        z=np.vstack([uniform_disk(rng,batch,h), uniform_disk(rng,batch,h),
                     uniform_disk(rng,batch), uniform_disk(rng,batch)])
        yes += np.count_nonzero(convex_four(z))
    return yes/n


def main():
    rng = np.random.default_rng(20261111)
    print('known disk baseline',P0)
    print('second-order law: first coefficient',A1,'second',A2)
    assert 0 < A1 < 1 and -1 < A2 < 0
    # The expressions below are algebraically equivalent (conditioned on
    # zero, one and two points in the excised disk).
    assert abs(A1 - (4*P0-4*P1)) < 1e-14
    assert abs(A2 - (10*P0 -16*P1+6*P2-8/PI**2))<1e-14
    print('CONDITIONAL_EXPANSION_ALGEBRA_OK')
    for u in [0.0, 0.15, 0.25]:
        obs=fixed_point_probability(rng,u)
        pred=P1+4*u*u/PI**2
        stderr=math.sqrt(obs*(1-obs)/900000)
        print('fixed point',u,'observed',round(obs,7),'Taylor',round(pred,7),'sigma',round(stderr,7))
        assert abs(obs-pred) < (6*stderr+0.0005+2.0*u**4)
    print('FIXED_POINT_LOCAL_EXPANSION_DIAGNOSTICS_OK')
    for h in [0.025,0.005]:
        obs=two_inner_probability(rng,h)
        stderr=math.sqrt(obs*(1-obs)/700000)
        print('two inner',h,'observed',round(obs,7),'target',0.5,'sigma',round(stderr,7))
        assert abs(obs-0.5)<(6*stderr+0.003)
    print('TWO_POINT_COLLISION_DIAGNOSTICS_OK')
    for t in [0.015,0.035,0.060]:
        obs=simulate_all(rng,t)
        pred=P0+A1*t+A2*t*t
        stderr=math.sqrt(obs*(1-obs)/700000)
        print('annulus',t,'observed',round(obs,7),'quadratic',round(pred,7),'sigma',round(stderr,7))
        assert abs(obs-pred)<(6*stderr+4*t**3)
    print('ANNULAR_CONVEX_POSITION_DIAGNOSTICS_OK')

if __name__=='__main__':
    main()
