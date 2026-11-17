#!/usr/bin/env python3
"""Finite consistency checks of formulas in the accompanying mathematical note.

Proof of the all-dimension statements is in RESULT.md, not in this script.
This checker uses rational inequalities and numerical geodesics with fixed seed.
"""
from fractions import Fraction
from math import comb, sqrt, sin, cos
from random import Random

rng=Random(314159)
case_count = 0
rational_checks = 0
geodesic_checks=0
angular_checks=0

for N in range(3, 18):
    total = 0
    for t in range(1,N):
        s=N-t
        w=sqrt(N/(t*s))
        a=-sqrt(s/(N*t))
        b=sqrt(t/(N*s))
        assert abs((b-a)-w)<1e-12
        assert abs(t*a+s*b)<1e-11
        assert abs(t*a*a+s*b*b-1)<1e-11
        m=max(t*(t-1),s*(s-1))
        gamma=1/sqrt(m)
        total += comb(N,t)
        case_count+=1
        for _ in range(80):
            low=[rng.randrange(-11,12) for i in range(t-1)]
            low.append(-sum(low))
            high=[rng.randrange(-11,12) for i in range(s-1)]
            high.append(-sum(high))
            norm2=sum(x*x for x in low+high)
            if not norm2:continue
            max_hi=max(high)
            minus_min_lo=-min(low)
            deriv=max_hi+minus_min_lo
            assert deriv>=0
            assert m*deriv*deriv>=norm2
            rational_checks+=1
        # Explicit equality vector in the larger group.
        if s>=t:
            low=[0.0]*t
            high=[-(s-1)*gamma]+[gamma]*(s-1)
        else:
            high=[0.0]*s
            low=[(t-1)*gamma]+[-gamma]*(t-1)
        assert abs(sum(low+high))<1e-10
        assert abs(sum(v*v for v in low+high)-1)<1e-10
        assert abs(max(high)-min(low)-gamma)<1e-10
        # Geodesic first-order expansion and strict growth on a small circle.
        u=[a]*t+[b]*s
        v=low+high
        theta=1e-5
        u_theta=[cos(theta)*x+sin(theta)*y for x,y in zip(u,v)]
        width=max(u_theta)-min(u_theta)
        assert abs(width-(cos(theta)*w+sin(theta)*gamma))<1e-12
        assert width>w
        geodesic_checks+=1
        # Exact local angular profile over a positive guaranteed chamber.
        theta=0.3*__import__('math').atan(w/sqrt(2))
        predicted=w*cos(theta)+gamma*sin(theta)
        extremal=[cos(theta)*x+sin(theta)*y for x,y in zip(u,v)]
        assert abs(max(extremal)-min(extremal)-predicted)<1e-12
        for _ in range(40):
            vvlow=[rng.uniform(-1,1) for _ in range(t)]
            vvhigh=[rng.uniform(-1,1) for _ in range(s)]
            vvlow=[z-sum(vvlow)/t for z in vvlow]
            vvhigh=[z-sum(vvhigh)/s for z in vvhigh]
            vvv=vvlow+vvhigh
            q=sqrt(sum(x*x for x in vvv))
            if q<1e-12: continue
            vvv=[x/q for x in vvv]
            yy=[cos(theta)*x+sin(theta)*y for x,y in zip(u,vvv)]
            assert max(yy)-min(yy) >=predicted-1e-12
            angular_checks+=1
    assert total==2**N-2
print('SIMPLEX_WIDTH_LANDSCAPE_CHECKS_PASSED dimensions=15 orbit_ranks=%d exact_inequalities=%d sharp_geodesics=%d angular_tests=%d' % (case_count,rational_checks,geodesic_checks,angular_checks))
