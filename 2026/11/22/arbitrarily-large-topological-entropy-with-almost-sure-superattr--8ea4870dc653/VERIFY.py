#!/usr/bin/env python3
"""Independent elementary identity and finite-sample checks for resonant sine maps.
Finite tests corroborate, but do not replace, the analytic arguments.
"""
import math, random

rng = random.Random(943251)
checks = 0
for m in [3,5,7,9,13,21]:
    k = math.pi*m/2
    d = 1/(k*k)
    lam = math.sqrt(2-1/(k*k))
    assert lam > 1
    checks += 1
    f = lambda x: math.sin(k*x)
    # Exact branch geometry has m-1 interior turning points, all at odd/m.
    crit = [(2*j+1)/m for j in range(-(m-1)//2, (m-1)//2)]
    assert len(crit)==m-1 and all(-1 < v < 1 for v in crit)
    checks += 1
    # At the critical values: f(crit)=+/-1.
    assert all(abs(abs(f(v))-1)<3e-14 for v in crit)
    checks += 1
    parity = 1 if m%4==1 else -1
    assert abs(f(1)-parity)<4e-14 and abs(f(-1)+parity)<4e-14
    checks += 1
    # Every closed monotonic lap runs across the full invariant interval.
    endpoints = [-1]+crit+[1]
    vals = [f(v) for v in endpoints]
    assert all(abs(abs(v)-1)<4e-14 for v in vals)
    assert all(vals[j]*vals[j+1] < 0 for j in range(len(vals)-1))
    checks += 1
    # Check trapping inequality for points at a range of endpoint distances.
    for q in [0.00001,0.01,0.1,0.33,0.5,0.99,1.0]:
        v=d*q
        assert 1-abs(f(1-v))<=k*k*v*v/2+1e-12
        checks+=1
    # For every sample whose image avoids the attracting neighborhoods,
    # numerical derivative must exceed the analytic expansion floor.
    for j in range(500):
        x=rng.uniform(-1,1)
        y=f(x)
        if abs(y)<=1-d-1e-11:
            assert (k*math.cos(k*x))**2 >= lam**2-1e-8
            checks+=1
    # Illustrative simulated trapping; do not claim exhaustive verification.
    captured=0
    for _ in range(200):
        x=rng.uniform(-1,1)
        for _ in range(2000):
            if abs(x)>1-d:
                captured+=1
                break
            x=f(x)
    assert captured==200, (m,captured)
    checks+=1
print('PASS:', checks,'finite checks; analytic theorems are separate')
