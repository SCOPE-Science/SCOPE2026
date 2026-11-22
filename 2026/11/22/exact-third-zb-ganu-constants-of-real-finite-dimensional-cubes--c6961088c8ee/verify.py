#!/usr/bin/env python3
"""Diagnostic reproduction for a real finite-cube three-sign constant."""
import math
import random

def norm_inf(x):
    return max(map(abs, x))

def z3(vs):
    d = len(vs[0]); assert len(vs) == 3 and all(len(v) == d for v in vs)
    q = sum(norm_inf(v)**2 for v in vs)
    if q == 0:
        return 0.0
    p = 1.0
    for eps in (-1, 1):
        for eta in (-1, 1):
            p *= norm_inf([vs[0][k] + eps*vs[1][k] + eta*vs[2][k] for k in range(d)])
    return math.sqrt(max(0.0, p))/q

a = math.sqrt(6)-2
bounds = {1:1.0, 2:2.0, 3:1+math.sqrt(6)/2, 4:3.0, 5:3.0}
witnesses = {
    1:[[1.0],[0.0],[0.0]],
    2:[[1.0,1.0],[1.0,-1.0],[0.0,0.0]],
    3:[[-a,-a,0.0],[-1.0,1.0,1.0],[-1.0,1.0,-1.0]],
    4:[[1.0]*4,[1.0,1.0,-1.0,-1.0],[1.0,-1.0,1.0,-1.0]],
}
checks = 0
for d, v in witnesses.items():
    assert abs(z3(v)-bounds[d]) < 2e-13
    checks += 1
v5 = [v + [0.0] for v in witnesses[4]]
assert abs(z3(v5)-3.0) < 2e-13; checks += 1
assert abs(2*(2+a)/(a*a+2)-(1+math.sqrt(6)/2)) < 1e-14; checks += 1
rng = random.Random(22611019)
for d in range(1, 6):
    for _ in range(6500):
        v = [[rng.uniform(-2.0,2.0) for k in range(d)] for i in range(3)]
        assert z3(v) <= bounds[d] + 2e-12
        checks += 1
        if d == 3:
            radii = [norm_inf(x) for x in v]
            q=sum(t*t for t in radii)
            b=sum(radii)*(sum(radii)-min(radii))/q
            assert z3(v) <= b + 2e-12
            checks += 1
print('THIRD_CUBE_ZBAGANU_DIAGNOSTIC_OK', checks)
