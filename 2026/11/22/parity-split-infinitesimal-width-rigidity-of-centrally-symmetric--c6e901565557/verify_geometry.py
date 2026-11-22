#!/usr/bin/env python3
"""Independent finite numerical cross-checks for the equilateral zonogon theorem.
The analytic proof, rather than these experiments, establishes the all-m statement.
No network or non-standard Python dependencies.
"""
import math
import random
import cmath

TAU = math.tau


def angles_from_gaps(gaps):
    a = [0.0]
    for g in gaps[:-1]:
        a.append(a[-1] + g)
    return a


def facet_widths(angles):
    m = len(angles)
    ext = angles + [v + math.pi for v in angles]
    return [sum(math.sin(ext[i+k] - ext[i]) for k in range(1,m)) for i in range(m)]


def direct_normal_widths(angles):
    return [sum(abs(math.sin(aj-ai)) for aj in angles) for ai in angles]


def directional_width(angles, phi):
    return sum(abs(math.cos(aj-phi)) for aj in angles)


def derivative_vector(v):
    m=len(v)
    return [sum(math.cos(k*math.pi/m)*(v[(i+k)%m]-v[i]) for k in range(1,m)) for i in range(m)]


def eigenvalue(q,m):
    return sum(math.cos(k*math.pi/m)*(cmath.exp(2j*math.pi*q*k/m)-1) for k in range(1,m))


def eigenvalue_closed(q,m):
    return .5j*(1/math.tan((2*q-1)*math.pi/(2*m))+1/math.tan((2*q+1)*math.pi/(2*m)))


def assert_close(x,y,atol=1e-9,rtol=1e-8):
    if abs(x-y) > atol+rtol*max(abs(x),abs(y)):
        raise AssertionError(f'{x!r} != {y!r}')


def run():
    rng = random.Random(203744)
    checks=0
    for m in range(2,24):
        a_regular=[i*math.pi/m for i in range(m)]
        bound=1/math.tan(math.pi/(2*m))
        for x in facet_widths(a_regular):
            assert_close(x,bound)
            checks+=1
        for q in range(m):
            assert_close(eigenvalue(q,m),eigenvalue_closed(q,m))
            checks+=1
            if q==0 or (m%2==0 and q==m//2):
                assert abs(eigenvalue(q,m))<1e-10
            else:
                assert abs(eigenvalue(q,m))>1e-5
            checks+=1
        for _ in range(24):
            raw=[rng.uniform(.2,2) for i in range(m)]
            gaps=[math.pi*r/sum(raw) for r in raw]
            a=angles_from_gaps(gaps)
            fs=facet_widths(a)
            direct=direct_normal_widths(a)
            for x,y in zip(fs,direct):
                assert_close(x,y)
                checks+=1
            assert min(fs)<=bound+1e-10
            checks+=1
            # Dense non-facet normals cannot improve on the exact facet minimum.
            sampled_min=min(directional_width(a,math.pi*j/713) for j in range(713))
            assert sampled_min>=min(fs)-1e-9
            checks+=1
        for _ in range(7):
            v=[rng.uniform(-2,2) for i in range(m)]
            t=1e-6
            shifted=[a_regular[i]+t*v[i] for i in range(m)]
            if any(shifted[i]>=shifted[i+1] for i in range(m-1)):
                raise AssertionError('Invalid perturbation')
            rhs=min(derivative_vector(v))
            lhs=(min(facet_widths(shifted))-bound)/t
            assert_close(lhs,rhs,atol=7e-5)
            checks+=1
            assert abs(sum(derivative_vector(v))) < 1e-9
            checks+=1
        if m%2==0:
            for t in [0.0, 0.0001, .05, math.pi/(4*m)]:
                ang=[a_regular[i]+t*((-1)**i) for i in range(m)]
                exact=bound-2*(1/math.sin(math.pi/m))*math.sin(t)**2
                assert_close(min(facet_widths(ang)),exact)
                for fi in facet_widths(ang):
                    assert_close(fi,exact)
                    checks+=1
    print('PASS checks:',checks, 'm=2,...,23, 24 random configurations/order, 7 perturbations/order')

if __name__=='__main__':
    run()
